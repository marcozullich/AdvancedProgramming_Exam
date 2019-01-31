#include <iostream>
#include <pybind11/pybind11.h>

using namespace std;

//K for key, V for value, C for comparing
template<typename K, typename V, typename C = less<K>>
class bst{
    //this one just to force the constructor to do sth
    bst(){
        cout << "Hello World!";
    }
};


namespace py = pybind11;

PYBIND11_MODULE(BST, m){
    //Binding an int-string dict
    py::class_<bst<int,string>>(m, "bst")
        //.def(py::init<std::array<std::vector<unsigned int>,10> &>())
        .def(py::init<>());
        //.def("getScore", &Game::getScore);
}
