import time
import matplotlib
import matplotlib.pyplot as plt

def average_execution_time(func, *args, runs=10, **kwargs):
    """
    Measures the average execution time of a function over a number of runs.

    Parameters:
    func: function to time
    *args: positional arguments for the function
    runs: how many times to run the function (default is 10)
    **kwargs: keyword arguments for the function

    Returns:
    Average execution time in seconds
    """
    total_time = 0.0

    # Measure execution time over multiple runs
    for _ in range(runs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        total_time += (end_time - start_time)

    # Calculate average time
    avg_time = total_time / runs
    return avg_time

def analyze_execution_time(plot_path, func, params_list, runs=10):
    """
    Analyzes the average execution time of a function with different parameters and plots the results.

    Parameters:
    func: function to time
    params_list: a list of tuples containing the parameters for each run
    runs: how many times to run the function for each parameter set (default is 10)
    
    Returns:
    A list of average execution times for each parameter set
    """
    times = []
    
   # Measure execution time for each set of parameters
    for params in params_list:
        avg_time = average_execution_time(func, *params, runs=runs)
        times.append(avg_time)
    
    # Plot the results
    input_sizes = [params[0] for params in params_list]  # Assuming the first param is the input size
    plt.plot(input_sizes, times, marker='o')

    # Annotate each point with its coordinates
    for i, (x, y) in enumerate(zip(input_sizes, times)):
        plt.text(x, y, f"({x}, {y:.3f})", fontsize=9, ha='left')

    plt.title(f'Execution Time Analysis of {func.__name__}')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.grid(True)
    plt.savefig(plot_path)

    return times

'''
# Example Usage
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Analyze execution times for increasing input sizes
params_list = [(1000,), (5000,), (10000,), (50000,), (100000,)]
analyze_execution_time("./plots/test.png", example_function, params_list, runs=10)
'''