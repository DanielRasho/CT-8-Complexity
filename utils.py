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
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(input_sizes, times, marker='o')

    # Create a table at the bottom
    table_data = list(zip(input_sizes, times))
    table = ax.table(cellText=table_data, colLabels=['Input Size', 'Average Time (seconds)'],
                     cellLoc='center', loc='bottom', bbox=[0.1, -0.5, 0.8, 0.3])

    # Adjust the plot limits and aesthetics
    ax.set_title(f'Execution Time Analysis of {func.__name__}')
    ax.set_xlabel('Input Size')
    ax.set_ylabel('Average Time (seconds)')
    ax.grid(True)

    # Save the figure as an image file
    plt.savefig(plot_path, bbox_inches='tight')  # Save the figure including the table

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