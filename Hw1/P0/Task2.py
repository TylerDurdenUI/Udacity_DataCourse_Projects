"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
d = {}

for val in calls:
	year = val[2][6:10]
	month = val[2][3:5]
	caller = val[0]
	reciever = val[1]
	duration = val[3]
	if year == '2016' and month == '09':
		d[caller] = d.get(caller,0)+int(duration)
		d[reciever] = d.get(reciever,0)+ int(duration)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max(d),d[max(d)]))


