import copy

def initialize_circuit(gates):
    max_line = max([max(gate.values()) for gate in gates])
    return {i: None for i in range(max_line + 1)}

def propagate_fault(circuit, fault_line, fault_value):
    circuit[fault_line] = fault_value

def is_fault_detected(circuit):
    return circuit[3] is not None

def extract_test_vector(circuit):
    return (circuit[0], circuit[1])

def objective(circuit, fault_value):
    if circuit[2] is None:
        if fault_value == 1:
            return 1, 1
        else:  # fault value is 0
            return 0, 1
    else:
        return None, None

def backtrace(node, value):
    if node == 0 or node == 1:
        for v in (0, 1):  # For this simple example, we just yield the target values
            yield v

def simulate(circuit, gates):
    for gate in gates:
        input1 = circuit[gate["input1"]]
        input2 = circuit[gate["input2"]]

        if input1 is not None and input2 is not None:
            if gate["type"] == 1:  # AND gate
                circuit[gate["output"]] = input1 & input2
            elif gate["type"] == 2:  # OR gate
                circuit[gate["output"]] = input1 | input2

def backtrack(circuit, node, backtrace_val):
    circuit[node] = None

def podem(gates, fault_line, fault_value, circuit=None):
    if circuit is None:
        circuit = initialize_circuit(gates)
        propagate_fault(circuit, fault_line, fault_value)

    if is_fault_detected(circuit):
        return extract_test_vector(circuit)

    node, value = objective(circuit, fault_value)
    if node is None:
        return None

    for backtrace_val in backtrace(node, value):
        if backtrace_val is None:
            continue

        circuit_copy = copy.deepcopy(circuit)
        circuit_copy[node] = backtrace_val

        simulate(circuit_copy, gates)

        result = podem(gates, fault_line, fault_value, circuit_copy)
        if result is not None:
            return result

        backtrack(circuit, node, backtrace_val)

    return None

def main():
    gates = [
        {"type": 1, "input1": 0, "input2": 1, "output": 2},
        {"type": 2, "input1": 0, "input2": 2, "output": 3}
    ]

    fault_line = 2
    fault_value = 1  # stuck-at-1 fault

    test_vector = podem(gates, fault_line, fault_value)
    print("Test vector:", test_vector)

if __name__ == "__main__":
    main()