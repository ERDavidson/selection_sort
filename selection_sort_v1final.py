import random, datetime, time
list_size = 100
mess = []
for index in range(list_size):
	mess.append(random.randint(1,10000))
print "Original list: " + str(mess)
if_count = 0
start_time = time.clock()
for focus_index in range(0, list_size-2):
	current_min_index = focus_index
	for comparison_index in range(focus_index+1, list_size-1):
		if_count += 1
		if mess[current_min_index] < mess[comparison_index]:	
			current_min_index = comparison_index	
	(mess[current_min_index], mess[focus_index]) = (mess[focus_index], mess[current_min_index])
end_time = time.clock()
print "Sorted version is" , mess
print str(datetime.timedelta(start_time, end_time))
print str(if_count) + " if statements"