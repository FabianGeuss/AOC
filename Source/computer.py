#class Computer for 2019d2
class Computer:

    memory_tape = []
    memory_pointer = 0
    command_list = {
        "add": { "offset": 4 },
        "multiply": { "offset": 4 },
    }


    def load(self, in_tape):
        self.memory_tape = in_tape.copy()
        self.memory_pointer = 0
        return
    
    def get_direct(self, in_offset):
        return self.memory_tape[self.memory_pointer + in_offset]

    def get_indirect(self, in_offset):
        return self.memory_tape[self.memory_tape[self.memory_pointer + in_offset]]
    
    def step(self):
        current_command = self.memory_tape[self.memory_pointer]
        if current_command == 1:
            x = self.get_indirect(1)
            y = self.get_indirect(2)
            z = self.get_direct(3)
            self.memory_tape[z] = x + y
            self.memory_pointer += self.command_list["add"]["offset"]
        if current_command == 2:
            x = self.get_indirect(1)
            y = self.get_indirect(2)
            z = self.get_direct(3)
            self.memory_tape[z] = x * y
            self.memory_pointer += self.command_list["multiply"]["offset"]
        if current_command == 99:
            self.memory_pointer = len(self.memory_tape)
            return

    def run(self, flag_debug=False):
        while self.memory_pointer < len(self.memory_tape):
            if flag_debug:
                print("step:", self.memory_pointer, self.memory_tape[self.memory_pointer], self.memory_tape)
            self.step()
        return
