import bisect

sorted_list = [4, 4, 4, 4, 6, 6, 6, 7, 9, 10]

leftIndex = bisect.bisect_left(sorted_list, 4)
rightIndex = bisect.bisect_right(sorted_list, 6)
print(str(leftIndex) + " " + str(rightIndex));
bisect.insort(sorted_list, 5);
bisect.insort(sorted_list, 7);
print(sorted_list)