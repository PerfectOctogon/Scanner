import os
class DFA:
    def __init__(self):
        print("")
    def reset(self):
        print()
    def transition(self, char):
        print()
    def is_valid(self, string):
        #some implementation
        print()

    # Your code ends here, do not modify code below
    def process_string(self, input_string):
        #Process each character in the input string
        self.reset()
        for char in input_string:
            self.transition(char)
            if self.state == "invalid":
                return False
            return self.is_accepting()

def main():
    for i in range(1, 11):
        file_name = f"test{i:02d}.txt"
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                input_string = file.read().strip()
                dfa = DFA()
                if dfa.process_string(input_string):
                    print(f"{file_name}: Valid")
                else:
                    print(f"{file_name}: Invalid")
        else:
            print(f"{file_name}: File not found")

if __name__ == "__main__":
    main()