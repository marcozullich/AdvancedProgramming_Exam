#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

int sub(int i, int j) {
    return i - j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
    m.def("sub2", &sub, "A function which subtracts two numbers");
}
