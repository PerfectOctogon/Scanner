import os

class State:
    state_name = ''
    is_final = False
    # stores all the states that can transition from this state
    valid_transitions = {}

    # constructor
    def __init__(self, state_name, is_final):
        self.state_name = state_name
        self.is_final = is_final

    # assigns the valid transitions that this state can make
    def assign_valid_transitions(self, valid_transitions):
        self.valid_transitions = valid_transitions

    # returns whether the transition that is being made from this state is valid
    def can_transition(self, transition_state):
        if transition_state in self.valid_transitions:
            return True
        return False


class DFA:
    # all states in the DFA
    # all states in the DFA
    q0 = State("", False)
    q1 = State("", False)
    q2 = State("", False)
    q3 = State("", False)

    # initial setup
    states = [q0, q1, q2, q3]
    state = "Valid"
    initial_state = State("", False)
    current_state = State("", False)

    # what are operators and what are brackets
    operators = ["+", "-", "*", "/"]
    brackets = ["[", "(", ")", "]"]

    #constructor
    def __init__(self):

        # initializing states
        self.q0 = State("q0", False)
        self.q1 = State("q1", True)
        self.q2 = State("q2", False)
        self.q3 = State("q3", True)

        # assigning valid transitions to states
        self.q0.assign_valid_transitions({self.q1, self.q2, self.q3})
        self.q1.assign_valid_transitions({self.q1, self.q2, self.q3})
        self.q2.assign_valid_transitions({self.q1, self.q3})
        self.q3.assign_valid_transitions({self.q1, self.q2, self.q3})

        # initializing initial and current state variables
        self.states = [self.q0, self.q1, self.q2, self.q3]
        self.initial_state = self.q0
        self.current_state = self.initial_state

    # sets the current state to the initial state
    def reset(self):
        self.current_state = self.initial_state

    # transitions from state to state. If a transition is invalid, sets the state param to Invalid
    def transition(self, char):
        # reading a number
        if char.isdigit():
            if self.current_state.can_transition(self.q1):
                self.state = "Valid"
            else:
                self.state = "Invalid"
            return self.state

        # reading an operator
        if char in self.operators:
            if self.current_state.can_transition(self.q2):
                self.state = "Valid"
            else:
                self.state = "Invalid"
            return self.state

        # reading a bracket
        if char in self.brackets:
            if self.current_state.can_transition(self.q3):
                self.state = "Valid"
            else:
                self.state = "Invalid"
            return self.state

    # returns if the current state is final
    def is_accepting(self):
        if self.current_state.is_final:
            return True
        return False

    # don't know what this does yet
    def is_valid(self, string):
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