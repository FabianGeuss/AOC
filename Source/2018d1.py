import tools  
import fileinput

# create a list of lines (strings) from the input file
lines = list(fileinput.input("Input/2018d1input.txt"))

CONST_RESULT_EXAMPLE1 = 3
CONST_RESULT_EXAMPLE2 = 2

#returns result of exercise part 1
def part_1(in_list):

	result = 0
	for frequency in in_list:
		result = result + frequency

	return result
	
#returns result of exercise part 2
def part_2(in_list):
	
	result = 0

	all_values = {result}

	while True:
		for frequency in in_list:
			result = result + frequency

			if result in all_values:
				print(result)
				return result
			all_values.add(result)
			continue 


if __name__ == "__main__":
	raw_example1 = tools.read_file("Example/2018d1e1.txt")
	clean_example1 = tools.prep_numlist(raw_example1)
	final_example1 = part_1(clean_example1)
	tools.assert_test(final_example1, CONST_RESULT_EXAMPLE1)

	raw_input1 = tools.read_file("Input/2018d1input.txt")
	clean_input1 = tools.prep_numlist(raw_input1)
	final_input1 = part_1(clean_input1)

	raw_input2 = tools.read_file("Input/2018d1input.txt")
	clean_input2 = tools.prep_numlist(raw_input2)
	final_input2 = part_2(clean_input2)

	print("Part 1:", final_input1)
	print("Part 2:", final_input2)
	