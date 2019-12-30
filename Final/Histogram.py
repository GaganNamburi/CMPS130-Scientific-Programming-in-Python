
file_open = open('data.txt', 'r')
nums = []
line_counter = 0
for num in file_open:
	num = int(num)
	nums.append(num)
	line_counter += 1

for i in nums:
	average1 = sum(nums[0])/line_counter
	average2 = sum(nums[1])/line_counter
	average3 = sum(nums[2])/line_counter

#The code does not work because I ran out of time to debug it.
