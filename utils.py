import time
import matplotlib.pyplot as plt
from problem1 import function_1  # Importa function_1 desde problem1.py
from problem2 import function_2  # Importa function_2 desde problem2.py
from problem3 import function_3  # Importa function_3 desde problem3.py

def average_execution_time(func, *args, runs=10, **kwargs):
    total_time = 0.0
    for _ in range(runs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / runs

def analyze_execution_time(plot_path, func, params_list, runs=10):
    times = []
    for params in params_list:
        avg_time = average_execution_time(func, *params, runs=runs)
        times.append(avg_time)

    input_sizes = [params[0] for params in params_list]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(input_sizes, times, marker='o')
    table_data = list(zip(input_sizes, times))
    table = ax.table(cellText=table_data, colLabels=['Input Size', 'Average Time (seconds)'],
                     cellLoc='center', loc='bottom', bbox=[0.1, -0.5, 0.8, 0.3])
    ax.set_title(f'Execution Time Analysis of {func.__name__}')
    ax.set_xlabel('Input Size')
    ax.set_ylabel('Average Time (seconds)')
    ax.grid(True)
    plt.savefig(plot_path, bbox_inches='tight')
    plt.show()

    return times

# Lista de tamaños de entrada para las pruebas
inputs = [(1,), (10,), (100,), (1000,), (10000,), (100000,)]  # Lista de tamaños de entrada original
# inputs = [(1,), (10,), (100,), (1000,)]  # Lista test

# Graficar los tiempos de ejecución de function_1
print("====REALIZANDO GRAFICAS INTUT VS TIEMPO====")
analyze_execution_time("./plots/test_function1.png", function_1, inputs, runs=10)

# Graficar los tiempos de ejecución de function_2
analyze_execution_time("./plots/test_function2.png", function_2, inputs, runs=10)

# Graficar los tiempos de ejecución de function_3
analyze_execution_time("./plots/test_function3.png", function_3, inputs, runs=10)
print("====FINALIZANDO GRAFICAS INTUT VS TIEMPO====")

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