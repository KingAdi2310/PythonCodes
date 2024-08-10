# Function to generate Fibonacci series
def fibonacci(n):
    fib_series = [0, 1]  # Starting elements
    for i in range(2, n):
        next_number = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_number)
    return fib_series
 #Taking input from user
n = int(input("Enter the number of terms: "))

#P rint the Fibonacci series
if n > 0:
    print(f"Fibonacci series with {n} terms: {fibonacci(n)}")
else:
    print("Please enter a positive integer.")
