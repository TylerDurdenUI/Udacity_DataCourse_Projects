import heapq
def getFreq(message):
    d = {}
    for i in message:
        d[i] = d.get(i,0)+1
    return d.items()

def buildtree(freq):
    """
    Input: freq is list of tuple, of which 1st element is freq, and 2nd ele is letter
    Output: heap tree, a nested list of tuples
    """

    heap = list()
    for _ in freq:
        heapq.heappush(heap,[_])#each node is a list
    while len(heap)>1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        freqleft,labelleft = left[0]
        freqrigh,labelrigh = right[0]
        merge_node = [(freqleft+freqrigh,labelleft+labelrigh),left,right]
        heapq.heappush(heap,merge_node)
    return heap[0]

def getCode(tree,d={},cur_code = ''):
    """
    Input: tree to be traversed,d is an initially empty dict and record the code as recursive progress
    Output: a list 0 and 1
    """
    if len(tree)==1: # base condition
        freq,letter = tree[0]
        d[letter] = cur_code
    else:
        value, left, right = tree
        getCode(left,d,cur_code+'0')
        getCode(right,d,cur_code+'1')
    return d
def encoding(message):
    if message=='':
        raise ValueError( "Input must not be EMPTY!")
    freq = getFreq(message)
    if len(freq)==1:
        letter = [i[0] for i in freq][0]
        letter_freq = [i[1] for i in freq][0]
        return '1'*letter_freq,[(1,letter)]
    tree = buildtree([i[::-1] for i in freq])
    code = getCode(tree)
    encode =  ''.join([code[letter] for letter in message])
    return encode,tree

def decoding(encode,tree):
    if len(tree)==1:
        return tree[0][1]*len(encode)
    pointer = tree
    message = []
    for ele in encode:
        if ele=='0':
            pointer = pointer[1]
        else:
            pointer = pointer[2]
        # check if it is leaf node
        if len(pointer)==1:
            message.append(pointer[0][1])
            pointer = tree
    return(''.join(message))

# testing case
import sys
if __name__ == "__main__":
    print('========\n Test 1 \n========')
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print('========\n Test 2 \n========')
    codes = {}

    a_great_sentence = "How are you today"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print('========\n Test 3 \n========')
    codes = {}

    a_great_sentence = "This is a crazy year"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('========\n Test 4 \n========')
    codes = {}

    a_great_sentence = "AAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('========\n Test 5 \n========')
    codes = {}

    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))