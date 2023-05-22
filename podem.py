input_values = []
assigned = []
def podem(gates, fault_gate, fault_line, fault_value):
    global assigned
    global input_values
    max_num = 0
    for k in gates:
        for i in k:
            if k[i] > max_num:
                max_num = k[i]
    max_line_number = max_num
    # max_line_number = max(max((gate['input1'], gate['input2'], gate['output']) for gate in gates))

    # 初始化输入值
    input_values = [None] * (max_line_number + 1)
    assigned = [False] * (max_line_number + 1)

    # 执行算法
    if recursive_backtrack(gates, fault_gate, fault_line, fault_value):
        print("Test vector found:")
        print(input_values)
    else:
        print("No test vector found.")

def recursive_backtrack(gates, fault_gate, fault_line, fault_value):
    global assigned
    global input_values

    result, gates = check_and_propagate(gates, fault_gate, fault_line, fault_value)

    if result:
        return True
    elif all(assigned):
        # 所有结果都被标记
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

def check_and_propagate(gates, fault_gate, fault_line, fault_value):
    global input_values

    # 计算每一个门的输出
    for i in range(len(gates)):
        input1 = input_values[gates[i]["input1"]]
        input2 = input_values[gates[i]["input2"]]

        if gates[i]["type"] == 1:  # AND gate
            output = min(input1, input2) if input1 is not None and input2 is not None else None
        elif gates[i]["type"] == 2:  # OR gate
            output = max(input1, input2) if input1 is not None and input2 is not None else None
        elif gates[i]["type"] == 3:  # XOR gate
            output = input1 ^ input2 if input1 is not None and input2 is not None else None

        if i == fault_gate and gates[i]["output"] == fault_line:
            output = output ^ fault_value if output is not None else None

        input_values[gates[i]["output"]] = output

    # Check if the error propagated to the output
    if None in input_values:
        return False, gates
    else:
        return input_values[-1] != 0, gates
#这个电路包含两个AND门和一个OR门。类型为1的门表示AND门，类型为2的门表示OR门。input1和input2是每个门的输入线序号，output是输出线序号。
# gates = [
#     {"type": 1, "input1": 0, "input2": 1, "output": 3},
#     {"type": 1, "input1": 2, "input2": 3, "output": 4},
#     {"type": 2, "input1": 1, "input2": 4, "output": 5}
# ]
# fault_gate = 1
# fault_line = 4
# fault_value = 1
#这个电路包含一个AND门（类型：1）和一个OR门（类型：2）。输入线有2条（编号0和1），输出线有1条（编号3）。
#我们需要扩展input_values和assigned数组的长度。它们的长度应该等于最大线序号加1，以确保所有线都能得到表示。在此示例中，最大线序号为3，因此数组长度应为4。
gates = [
    {"type": 1, "input1": 0, "input2": 1, "output": 2},
    {"type": 2, "input1": 0, "input2": 2, "output": 3}
]
fault_gate = 0
fault_line = 2
fault_value = 1

podem(gates, fault_gate, fault_line, fault_value)
