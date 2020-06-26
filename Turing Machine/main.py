from tape import Direction
from turing_machine import TuringMachine

states = {"q0","q1","q2","q3","q4"}
alphabet = {"0","1"}
tape_symbols = {"0","1","X","Y","B"}
transition_function = {("q0","0"):("q1", "X", Direction.RIGHT),
                       ("q0","Y"):("q3", "Y", Direction.RIGHT),
                       ("q1","0"):("q1", "0", Direction.RIGHT),
                       ("q1","1"):("q2", "Y", Direction.LEFT),
                       ("q1","Y"):("q1", "Y", Direction.RIGHT),
                       ("q2","0"):("q2", "0", Direction.LEFT),
                       ("q2","X"):("q0", "X", Direction.RIGHT),
                       ("q2","Y"):("q2", "Y", Direction.LEFT),
                       ("q3","Y"):("q3", "Y", Direction.RIGHT),
                       ("q3","B"):("q4", "B", Direction.RIGHT)
                    }

start_state = "q0"
final_states = {"q4"}
blank_symbol = "B"

t = TuringMachine(states, 
                alphabet, 
                tape_symbols, 
                transition_function, 
                start_state, 
                final_states, 
                blank_symbol)

tape_input = "0000111"
t.simulate(tape_input, True)

tape_input = "011"
t.simulate(tape_input, True)

tape_input = "0011"
t.simulate(tape_input, True)

#tape_input = "0011"
#t.simulate(tape_input, False)

