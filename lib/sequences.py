#!/usr/bin/env python3
def print_fibonacci(length):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    result = []

    # Handle edge cases
    if length <= 0:
        print(result)
        return
    elif length == 1:
        result.append(a)
        print(result)
        return
    elif length == 2:
        result.extend([a, b])
        print(result)
        return

    # Generate Fibonacci sequence
    result.extend([a, b])
    for _ in range(2, length):
        a, b = b, a + b
        result.append(b)
    
    print(result)
