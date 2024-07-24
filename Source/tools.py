#tools for advent of code exercises
def read_file(in_path):
    handle_file = open(in_path, "r")
    return handle_file.read()

def prep_numlist(in_raw):
	out_split = in_raw.split("\n")
	out_list = list(map(int, out_split))
	return out_list

def prep_strlist(in_raw):
	out_split = in_raw.split("\n")
	return out_split

def prep_from_comma_list(in_raw):
      out_split = in_raw.split(",")
      return out_split

def map_list_to_ints(in_list):
    out_list = list(map(int, in_list))
    return out_list

def assert_test(in_a, in_b):
    if in_a != in_b:
        print(f"FAIL {in_a} : {in_b}")
    else:
        print(f"SUCCESS {in_a} : {in_b}")