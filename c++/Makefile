FOLDER      = ./c++
TARGET		= bst

CC			= g++
CPPVERSION  = -std=c++11
CCFLAGS		= -Wall -Wextra
SLFLAGS		= -shared -fPIC
INCLUDES	= `python3 -m pybind11 --includes`
SLSUFFIX	= `python3-config --extension-suffix`

HEADER		= $(TARGET).h
OUTPUT      = -o $(TARGET)$(SLSUFFIX)

default:
	$(CC) $(CPPVERSION) $(CCFLAGS) $(SLFLAGS) $(INCLUDES) $(HEADER) $(OUTPUT)