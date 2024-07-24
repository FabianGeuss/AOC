import tools
import math    


CONST_RESULT_EXAMPLE1 = 514579
CONST_RESULT_EXAMPLE2 = 241861950


#function that returns result of part 1
def part_1(in_list):
		
	for number_one in in_list:
		for number_two in in_list:
			if number_one + number_two == 2020:
				result = number_one * number_two
				print(result)
				return result				

#function that returns result of part 2
def part_2(in_list):

	for number_one in in_list:
		for number_two in in_list:
			for number_three in in_list:
				if number_one + number_two + number_three == 2020:
					result = number_one * number_two * number_three
					print(result)
					return result


if __name__ == "__main__":
	raw_example1 = tools.read_file("Example/2020d1e1.txt")
	clean_example1 = tools.prep_numlist(raw_example1)
	final_example1 = part_1(clean_example1)
	tools.assert_test(final_example1, CONST_RESULT_EXAMPLE1)

	raw_input1 = tools.read_file("Input/2020d1input.txt")
	clean_input1 = tools.prep_numlist(raw_input1)
	final_input1 = part_1(clean_input1)

	raw_input2 = tools.read_file("Input/2020d1input.txt")
	clean_input2 = tools.prep_numlist(raw_input1)
	final_input2 = part_2(clean_input2)
	
	print("Part 1:", final_input1)
	print("Part 2:", final_input2)
	