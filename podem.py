input_values = []
assigned = []

def propagate(gates, values):
    new_values = values.copy()
    for gate in gates:
        input1_value = new_values[gate['input1']]
        input2_value = new_values[gate['input2']]

        if gate['type'] == 1:  # AND gate
            result = input1_value and input2_value
        elif gate['type'] == 2:  # OR gate
            result = input1_value or input2_value
        elif gate['type'] == 3:  # XOR gate
            result = input1_value ^ input2_value

        new_values[gate['output']] = result
    
    return new_values

def print_test_vector(input_values):
    relevant_inputs = [input_values[0], input_values[1]]
    relevant_inputs = [input_values[0], input_values[1], input_values[2]]
    print("Test vector found:", relevant_inputs)

def podem(gates, fault_gate, fault_line, fault_value):
    max_num = 0
    for k in gates:
        for i in k:
            if k[i] > max_num:
                max_num = k[i]
    max_line_number = max_num
    
    # max_line_number = max(max((gate['input1'], gate['input2'], gate['output']) for gate in gates))

    global input_values
    global assigned

    input_values = [None] * (max_line_number + 1)
    assigned = [False] * (max_line_number + 1)

    if recursive_backtrack(gates, fault_gate, fault_line, fault_value):
        print_test_vector(input_values)
    else:
        print("No test vector found.")

def recursive_backtrack(gates, fault_gate, fault_line, fault_value):
    global input_values
    global assigned

    good_circuit_values = propagate(gates, input_values)

    faulty_gates = gates.copy()
    faulty_gates[fault_gate] = faulty_gates[fault_gate].copy()
    faulty_gates[fault_gate][fault_line] = fault_value
    faulty_circuit_values = propagate(faulty_gates, input_values)

    if good_circuit_values != faulty_circuit_values:
        return True
    elif all(assigned):
        return False
    else:
        index = assigned.index(False)
        for val in [0, 1]:
            assigned[index] = True
            input_values[index] = val

            if recursive_backtrack(gates, fault_gate, fault_line, fault_value):
                return True

            assigned[index] = False

        return False
gates = [
    {"type": 1, "input1": 0, "input2": 1, "output": 3},
    {"type": 1, "input1": 2, "input2": 3, "output": 4},
    {"type": 2, "input1": 1, "input2": 4, "output": 5}
]
fault_gate = 1
fault_line = 'input1'
fault_value = 1
# [0,0,None]

# gates = [
#     {"type": 1, "input1": 0, "input2": 1, "output": 2},
#     {"type": 2, "input1": 0, "input2": 2, "output": 3}
# ]

# fault_gate = 1
# fault_line = 'input1'
# fault_value = 1

podem(gates, fault_gate, fault_line, fault_value)
