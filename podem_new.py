def propagate_value(gates, values):
    new_values = values.copy()
    for gate in gates:
        input1_value = new_values[gate["input1"]]
        input2_value = new_values[gate["input2"]]
        
        if gate["type"] == 1:  # AND gate
            result = input1_value and input2_value
        elif gate["type"] == 2:  # OR gate
            result = input1_value or input2_value
        
        new_values[gate["output"]] = result
    
    return new_values

def find_test_vectors(gates, fault_gate, fault_line, fault_value):
    test_vectors = []

    for i1 in [0, 1]:
        for i2 in [0, 1]:
            input_values = {0: i1, 1: i2}
            good_circuit_values = propagate_value(gates, input_values)
            
            faulty_gates = gates.copy()
            faulty_gates[fault_gate] = faulty_gates[fault_gate].copy()
            faulty_gates[fault_gate][fault_line] = fault_value
            
            faulty_circuit_values = propagate_value(faulty_gates, input_values)
            
            if good_circuit_values != faulty_circuit_values:
                test_vectors.append((i1, i2))
    
    return test_vectors

gates = [
    {"type": 1, "input1": 0, "input2": 1, "output": 2},
    {"type": 2, "input1": 0, "input2": 2, "output": 3}
]
fault_gate = 1
fault_line = "input2"
fault_value = 1

test_vectors = find_test_vectors(gates, fault_gate, fault_line, fault_value)
print("All possible test vectors:", test_vectors)
