"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
s_caller = set([i[0] for i in calls])
s_send_tx = set([i[0] for i in texts])
s_rec_tx = set([i[1] for i in texts])
s_rec_call = set([i[1] for i in calls])
print("These numbers could be telemarketers: ")
for i in  sorted(list(s_caller - s_send_tx|s_rec_tx|s_rec_call)):
	print(i)
