#include <iostream>
#include <bitset>

bool system_function(bool A, bool B, bool C) {
    return A && (B || C);
}

int main() {
    for (int test_vector = 0; test_vector <= 7; ++test_vector) {
        std::bitset<3> inputs(test_vector);
        bool A = inputs[2];
        bool B = inputs[1];
        bool C = inputs[0];

        bool expected_output = system_function(A, B, C);

        // Simulate Faulty AND Gate with Stuck-at-0 fault
        bool faulty_output_0 = (!A) && (B || C);

        // Simulate Faulty AND Gate with Stuck-at-1 fault
        bool faulty_output_1 = A || (B || C);

        std::cout << "Test Vector: " << inputs << " | Expected Output: " << expected_output << " | Faulty Output (Stuck-at-0): " << faulty_output_0 << " | Faulty Output (Stuck-at-1): " << faulty_output_1 << std::endl;

        // Fault Diagnosis
        if (expected_output != faulty_output_0) {
            std::cout << "Fault detected: AND gate stuck-at-0" << std::endl;
        }

        if (expected_output != faulty_output_1) {
            std::cout << "Fault detected: AND gate stuck-at-1" << std::endl;
        }
    }

    return 0;
}