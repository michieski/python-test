# Last updated: 2026-02-04 07:44:34

def fibonacci(n):    if n <= 1:        return n    return fibonacci(n-1) + fibonacci(n-2)if __name__ == "__main__":    for i in range(10):        print(f"F({i}) = {fibonacci(i)}")
