import tools

#function that returns an prepared list to work with
def prep_input(in_list):
	out_list = []
	for temp_string in in_list:
		pair_string = temp_string.split(" ")
		out_list.append((pair_string[0], int(pair_string[1])))
	return out_list
	
#function that returns solution for part 1
def part_1(in_list):
	
	forward = []
	up = []
	down = []
	
	test = in_list[0]
	test2 = test[0]


	for elements in in_list:
		if elements[0] == 'forward':
			forward.append(elements[1])
		elif elements[0] == 'up':
			up.append(elements[1])
		elif elements[0] == 'down':
			down.append(elements[1])

	horizontal_position = sum(forward)
	depth = sum(down) - sum(up)

	out_num = horizontal_position * depth 
	print(out_num)
	return out_num

#function that returns solution for part 2
def part_2(in_list):
	
	aim = 0
	depth = 0
	horizontal_position = 0
	
	test = in_list[0]
	test2 = test[0]

	for elements in in_list:
		if elements[0] == 'forward':
			horizontal_position += elements[1]
			depth += aim * elements[1]
		elif elements[0] == 'up':
			aim -= elements[1]
		elif elements[0] == 'down':
			aim += elements[1]

	
	out_num = horizontal_position * depth 
	return out_num

if __name__ == "__main__":
	raw_example1 = tools.read_file("Example/2021d2e1.txt")
	clean_example1 = tools.prep_strlist(raw_example1)
	prep_example1 = prep_input(clean_example1)
	final_example1 = part_1(prep_example1)

	raw_input1 = tools.read_file("Input/2021d2input.txt")
	clean_input1 = tools.prep_strlist(raw_input1)
	prep_input1 = prep_input(clean_input1)
	final_input1 = part_1(prep_input1)
	
	raw_input2 = tools.read_file("Input/2021d2input.txt")
	clean_input2 = tools.prep_strlist(raw_input1)
	prep_input2 = prep_input(clean_input1)
	final_input2 = part_2(prep_input1)
	
	print("Part 1:", final_input1)
	print("Part 2:", final_input2)