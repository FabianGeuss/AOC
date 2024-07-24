import computer
import tools

CONST_EXAMPLE1 = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]  

CONST_EXAMPLE2 = ([1,1,1,4,99,5,6,0,99], [30, 1, 1, 4, 2, 5, 6, 0, 99])

CONST_EXAMPLE3 = ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99])

CONST_EXAMPLE4 = [2, 3, 0, 6, 99]

CONST_EXAMPLE5 = ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801])

#function that returns solution for part 1
def part_one(in_list):
	handle_computer = computer.Computer()
	handle_computer.load(in_list)
	handle_computer.run()
	return handle_computer.memory_tape


if __name__ == "__main__":
	
	raw_input1 = tools.read_file("Input/2019d2input.txt")
	clean_input1 = tools.map_list_to_ints(tools.prep_from_comma_list(raw_input1))
	clean_input1[1] = 12
	clean_input1[2] = 2
	final_input1 = part_one(clean_input1) 

	
	#everything down here is for part 2
	list1_possible_numbers = list(range(100))
	list2_possible_numbers = list(range(100))
	noun = []
	verb = []
	for parameter1 in list1_possible_numbers:
		for parameter2 in list2_possible_numbers:
			raw_input2 = tools.read_file("Input/2019d2input.txt")
			clean_input2 = tools.map_list_to_ints(tools.prep_from_comma_list(raw_input2))
			clean_input2[1] = parameter1
			clean_input2[2] = parameter2
			final_input2 = part_one(clean_input2)

			
			control_number = final_input2[0]
			if control_number == 19690720:
				noun.append(parameter1)
				verb.append(parameter2)
				break
			else:
				continue

	print("Noun:", noun)
	print("Verb:", verb)


	tools.assert_test(part_one(CONST_EXAMPLE2[0]), CONST_EXAMPLE2[1])
	tools.assert_test(part_one(CONST_EXAMPLE3[0]), CONST_EXAMPLE3[1])
	tools.assert_test(part_one(CONST_EXAMPLE5[0]), CONST_EXAMPLE5[1])
	

	print(final_input1)
	print("Part 1:", final_input1[0])
	print("Part 2:", 100 * noun[0] + verb[0])

	