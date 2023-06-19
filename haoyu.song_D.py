'''该代码首先定义了正常数字电路和两种故障电路（SA1和SA0）。
然后，函数generate_test_vectors()生成所有可能的输入向量。
接下来，diagnostic_algorithm()函数使用这些输入向量对正常和故障电路进行测试，
以检测SA1和SA0故障。'''
def normal_circuit(a, b, c):
    return a and (b or c)

def faulty_circuit_sa1(a, b, c):
    return 1

def faulty_circuit_sa0(a, b, c):
    return 0

def generate_test_vectors():
    test_vectors = [(a, b, c) for a in range(2) for b in range(2) for c in range(2)]
    return test_vectors

def diagnostic_algorithm(test_vectors):
    sa1_fault_detected = False
    sa0_fault_detected = False

    for vector in test_vectors:
        a, b, c = vector
        normal_output = normal_circuit(a, b, c)
        sa1_output = faulty_circuit_sa1(a, b, c)
        sa0_output = faulty_circuit_sa0(a, b, c)

        if normal_output != sa1_output:
            sa1_fault_detected = True
            print(f"SA1 fault detected with test vector {vector}")
        
        if normal_output != sa0_output:
            sa0_fault_detected = True
            print(f"SA0 fault detected with test vector {vector}")

        if sa1_fault_detected and sa0_fault_detected:
            break

test_vectors = generate_test_vectors()
diagnostic_algorithm(test_vectors)