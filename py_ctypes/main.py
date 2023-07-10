import ctypes

# load the shared library
lib = ctypes.CDLL('./example.so')

# declare the function signature
lib.add_numbers.restype = ctypes.c_int
lib.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]

# main function
def main():
    result = lib.add_numbers(3, 4)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()