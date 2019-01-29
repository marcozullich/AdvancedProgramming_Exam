appname := example`python3-config --extension-suffix` 

CXX := c++
CXXFLAGS := -O3 -Wall -shared -std=c++11


objects  := example.cpp
pythonFlags := `python3 -m pybind11 --includes`


all: $(appname)

$(appname):
	$(CXX) $(CXXFLAGS) -fPIC $(pythonFlags) $(objects) -o $(appname) $(LDLIBS) 


