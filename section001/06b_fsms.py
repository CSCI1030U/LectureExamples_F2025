# Finite State Machines/Automata

current_state = 'Start'
user_action = 'insert $1 coin'
open_gate = False

if current_state == 'Start':
    if user_action == 'insert $1 coin':
        current_state = '$1'
    elif user_action == 'insert $2 coin':
        current_state = '$2'
elif current_state == '$1':
    if user_action == 'insert $1 coin':
        current_state = '$2'
    elif user_action == 'insert $2 coin':
        current_state = '$3'
        open_gate = True
elif current_state == '$2':
    if user_action == 'insert $1 coin':
        current_state = '$3'
        open_gate = True
    elif user_action == 'insert $2 coin':
        current_state = '$3'
        open_gate = True
