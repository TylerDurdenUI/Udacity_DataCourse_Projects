# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    
    def __init__(self,handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self,value):
        # Insert the node as before
        sefl.children[value] = self.children.get(value,RouteTrieNode())


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler=handler)
        
    def insert(self,url,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        ls = [i for i in url.split('/') if i!='']
        node = self.root
        for ele in ls:
            node.children[ele] = node.children.get(ele,RouteTrieNode())
            node = node.children[ele]
        node.handler = handler

    def find(self,url):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        ls = [i for i in url.split('/') if i!='']
        node = self.root
        for i in ls:
            if i not in node.children:
                return None
            node = node.children[i]
        return node.handler
            
            
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, handler404='404 page not found'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routetrie = RouteTrie(handler)
        self.handler404 = handler404

    def add_handler(self, handler, path):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routetrie.insert(path, handler)
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.routetrie.find(path)
        if handler==None:
            return self.handler404
        else:
            return handler
    def split_path(self):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path = path.strip("/")
        return path.split("/") if path else []


# test


# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler( "about handler","/home/about")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one