import tools
import math

INPUT_RESULT_EXAMPLE_1 = 159
INPUT_RESULT_EXAMPLE_2 = 135

#Function that prepairs the input list
def prep_inputlist(in_list):
	prep_list = []
	for element in in_list:
		direction = element[0]
		distance = int(element[1:])
		prep_list.append((direction, distance))
	return prep_list

MAP_DIR = {
	"U": (0, 1),
	"R": (1, 0),
	"D": (0, -1),
	"L": (-1, 0),
}

def wire_set(in_list):
	return set(wire_1(in_list).keys())

#Function that creates a set with all the coordinates of wire 1
def wire_1(in_list):
	all_coordinates_wire_1 = dict()

	x_coordinate = 0
	y_coordinate = 0
	totalcounter = 1

	for movements in in_list:
		counter = movements[1]
		direction = movements[0]
		while counter != 0:
			x_coordinate += MAP_DIR[direction][0]
			y_coordinate += MAP_DIR[direction][1]
			pair_coordinate = (x_coordinate, y_coordinate)
			if pair_coordinate not in all_coordinates_wire_1:
				all_coordinates_wire_1[pair_coordinate] = totalcounter
			totalcounter += 1
			counter -= 1
	return all_coordinates_wire_1

infinity = math.inf	

#function that finds the lowest distance
def find_lowest(in_list):
	lowest = infinity
	for position in in_list:
		distance = math.sqrt(pow(position[0],2)+pow(position[1],2))
		if distance < lowest:
			lowest = distance
	return lowest


#function that finds the lowest sum of steps
def final_loop(in_set, in_wire1, in_wire2):
	lowest = infinity
	for pos in in_set:
		zahl_1 = in_wire1[pos]
		zahl_2 = in_wire2[pos]
		temp = zahl_1 + zahl_2	
		if temp < lowest:
			lowest = temp
			
	return lowest

	
if __name__ == "__main__":
	
	#DEFINE EXAMPLES:
	raw_example1_1 = tools.read_file("Example/2019d3e1.1.txt")
	clean_example1_1 = tools.prep_from_comma_list(raw_example1_1)
	prep_example1_1 = prep_inputlist(clean_example1_1)
	final_example1_1 = wire_set(prep_example1_1)

	raw_example1_2 = tools.read_file("Example/2019d3e1.2.txt")
	clean_example1_2 = tools.prep_from_comma_list(raw_example1_2)
	prep_example1_2 = prep_inputlist(clean_example1_2)
	final_example1_2 = wire_set(prep_example1_2)

	#IMPORTANT DEFINITIONS FOR PART 2:
	schnittmenge_1 = wire_1(prep_example1_1)
	schnittmenge_2 = wire_1(prep_example1_2)
	i = final_example1_1.intersection(final_example1_2) 
	last_step = find_lowest(i)
	result = final_loop(i, schnittmenge_1, schnittmenge_2)

	#DEFINE ACTUAL WIRES:
	raw_input1 = tools.read_file("Input/2019d3input1.txt")
	clean_input1 = tools.prep_from_comma_list(raw_input1)
	prep_input1 = prep_inputlist(clean_input1)
	final_input1 = wire_set(prep_input1)

	raw_input2 = tools.read_file("Input/2019d3input2.txt")
	clean_input2 = tools.prep_from_comma_list(raw_input2)
	prep_input2 = prep_inputlist(clean_input2)
	final_input2 = wire_set(prep_input2)
	
	schnittmenge_1 = wire_1(prep_input1)
	schnittmenge_2 = wire_1(prep_input2)

	i = final_input1.intersection(final_input2) 
	last_step = find_lowest(i)
	result = final_loop(i, schnittmenge_1, schnittmenge_2)

	print("Solution Part 1:", last_step)
	print("Solution Part 2:", result)
