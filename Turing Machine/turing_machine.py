from tape import Tape

class TuringMachine():
    def __init__(self, 
                states, 
                alphabet, 
                tape_symbols, 
                transition_function, 
                start_state, 
                final_states, 
                blank_symbol = 'B' ):

        self.state = start_state

        self.states = states
        self.alphabet = alphabet
        self.tape_symbols = tape_symbols
        self.transition_function = transition_function
        self.start_state = start_state
        self.final_states = final_states
        self.blank_symbol = blank_symbol

    def _step(self, tape):
        transition_input = (self.state, tape.get_head_symbol())

        if transition_input in self.transition_function:
            transition_output = self.transition_function[transition_input]

            self.state = transition_output[0]
            tape.set_head_symbol(transition_output[1], transition_output[2])
        else:
            raise KeyError("Turing Machine halted in a Reject state")

    def _final_state(self):
        return self.state in self.final_states

    def simulate(self, tape_input, print_configurations = False):
        self.state = self.start_state
        tape = Tape(tape_input, self.blank_symbol)
        while not self._final_state():
            if print_configurations:
                tape.print_configuration(self.state)

            try:
                self._step(tape)
            except KeyError as error:
                print(error)
                return
        print("Turing Machine halted in an Accepting state")

