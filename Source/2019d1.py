import tools
import math    

CONST_EXAMPLE1 = sum([2, 2, 654, 33583])
CONST_EXAMPLE2 = ([1969], 966)
CONST_EXAMPLE3 = ([100756], 50346)

#returns result of exercise part 1
def part_one(in_list):
	
	result_list = []
	for number in in_list:
		step = (math.floor(number/3)-2)
		
		
		result_list.append(step)
		
	return sum(result_list)
	
#returns result of exercise part 2
def part_two(in_list):
	result_mass = []
	for itr_mass in in_list:
		mass_current = itr_mass
		while mass_current > 0:
			mass_current = math.floor(mass_current/3)-2
			if mass_current < 0:
				break
			result_mass.append(mass_current)
	return sum(result_mass)

if __name__ == "__main__":
	raw_example1 = tools.read_file("Example/2019d1e1.txt")
	clean_example1 = tools.prep_numlist(raw_example1)
	final_example1 = part_one(clean_example1)
	tools.assert_test(final_example1, CONST_EXAMPLE1)

	raw_input1 = tools.read_file("Input/2019d1input.txt")
	clean_input1 = tools.prep_numlist(raw_input1)
	final_input1 = part_one(clean_input1)

	tools.assert_test(part_two(CONST_EXAMPLE2[0]), CONST_EXAMPLE2[1])
	tools.assert_test(part_two(CONST_EXAMPLE3[0]), CONST_EXAMPLE3[1])

	final_input2 = part_two(clean_input1)
	print("Part 1:", final_input1)
	print("Part 2:", final_input2)
	