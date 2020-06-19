from collections import namedtuple
# Data type that handy to store the current state
import heapq
# Semi order all the path, so that accessing the optimal(lowest cost) path is constant time

COST = namedtuple('COST',['f','g','h']) 
# f is the total cost, 
# g is the traversed path distance to origin
# and h is the optimistic estimation distance to goal.

PATH = namedtuple('PATH',['cost','city_traversed','second_last','frontier'])
# cost is the f = g+h
# city_traversed is the list of cities traversed, or current path
# second_last is the second to last city in current city_traversed, to avoid path going back
# frontier is the current path frontier

def dist(city1:[float,float],city2:[float,float])->float:
    """
    Goal: handy function to compute distance between two 2-D points
    Input:
    city 1 and city 2 are the x, y coordinates,respectively
    Output:
    The distance between city 1 and city 2
    """
    return ((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)**.5

def updater(input_map, path, frontier_new, destination):
    """
    Goal: Update the path in each iteration
    Input:
    input_map: the input map object
    path: the PATH named tuple
    frontier_new: the city to be added as new frontier city
    destination: the goal city
    """
    distance_delta = dist(city1 = input_map.intersections[path.frontier],city2 = input_map.intersections[frontier_new])
    g_new = distance_delta + path.cost.g
    h_new = dist(city1 = input_map.intersections[frontier_new], city2 = input_map.intersections[destination])
    f_new = g_new + h_new
    city_traversed_new = path.city_traversed+[frontier_new]
    # previous frontier become the second to last
    # frontier_new is the latest frontier for updated path
    return PATH(COST(f_new,g_new,h_new),city_traversed_new,path.frontier,frontier_new)
    
def shortest_path(input_map,origin,destination):
    """
    Input:
    input_map: the input map object
    origin: the starting city
    destination: the goal city
    """
    # Edge case
    if origin == destination:
        return [destination]
    all_path = []
    
    # Initialization
    path_optimal = None # the optimal path--- list of cities, which will be updated by each iteration
    path_optimal_cost = float('inf') # the f(total cost) of optimal path
    distance_init = dist(input_map.intersections[origin],input_map.intersections[destination]) 
    path = PATH(COST(distance_init,0,distance_init),[origin],origin,origin)
    heapq.heappush(all_path,path)
    
    while len(all_path) >= 1:
        path_best = heapq.heappop(all_path)
        # iterate through all possible candidate new frontier cities
        for candidate_frontier in input_map.roads[path_best.frontier]:
            if candidate_frontier != path_best.second_last: # Avoid going backward
                path_new = updater(input_map,path_best,candidate_frontier,destination)
                if candidate_frontier != destination: # Not reach destination yet
                    if (not path_optimal) or (path_new.cost.f<path_optimal_cost):
                        heapq.heappush(all_path,path_new)
                else: # only track the shorter, better one
                    if path_new.cost.f < path_optimal_cost:
                        path_optimal_cost = path_new.cost.f
                        path_optimal = path_new.city_traversed                
    return path_optimal if path_optimal else -1