#include <iostream>

extern "C" {
    int add_numbers(int a, int b) {
        return a + b;
    }
}