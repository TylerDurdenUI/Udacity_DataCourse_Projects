class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    def to_list(self):
        cur_head = self.head
        opt = []
        while cur_head:
            opt.append(cur_head.value)
            cur_head = cur_head.next
        return opt

def union(llist_1, llist_2):
    # Your Solution Here
    l1 = llist_1.to_list()
    l2 = llist_2.to_list()
    opt_llist = LinkedList()
    for ele in set(l1).union(set(l2)):
        opt_llist.append(ele)
    return opt_llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    l1 = llist_1.to_list()
    l2 = llist_2.to_list()
    opt_llist = LinkedList()
    for ele in set(l1).intersection(set(l2)):
            opt_llist.append(ele)
    return opt_llist



## Test 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
test1_result = union(linked_list_1, linked_list_2)
test1_answer = "32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> "

test2_result = intersection(linked_list_1, linked_list_2)
test2_answer = "4 -> 21 -> 6 -> "

print ("Pass" if (str(test1_result) == test1_answer) else "Fail")
print ("Pass" if (str(test2_result) == test2_answer) else "Fail")

## Test 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

test3_result = union(linked_list_3, linked_list_4)
test3_answer = "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> "

test4_result = intersection(linked_list_3, linked_list_4)

print ("Pass" if (str(test3_result) == test3_answer) else "Fail")
print ("Pass" if (str(test4_result) == "") else "Fail")


## Test 3

linked_list5 = LinkedList()
linked_list6 = LinkedList()

element_1 = [None,2,3,4]
element_2 = [1,2,3,5,7,9]

for i in element_1:
    linked_list5.append(i)

for i in element_2:
    linked_list6.append(i)

test5_result = union(linked_list5, linked_list6)
test5_answer = "1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 9 -> None -> "
test6_result = intersection(linked_list5, linked_list6)
print ("Pass" if (str(test6_result) == "2 -> 3 -> ") else "Fail")

## Test 4 Both are empty LinkedList object

linked_list7 = LinkedList()
linked_list8 = LinkedList()


test7_result = union(linked_list7, linked_list8)
test7_answer = ""
test8_result = intersection(linked_list7, linked_list8)
test8_answer = ""
print ("Pass" if (str(test7_result) == test7_answer) else "Fail")
print ("Pass" if (str(test8_result) == test8_answer) else "Fail")