
import os
os.system ("make -f ./mix/examplePybind11/Makefile")
import example

print(example.add(1, 2))
print(example.sub2(1, 2))

def test_answer():
    assert example.add(1,1) == 2
