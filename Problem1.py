from utils import analyze_execution_time

def problema1 ( n : int ) :
    counter = 0                             # t = c1
    i = 0                                   # t = c1
    j = 0                                   # t = c1
    k = 0                                   # t = c1
    for i in range(1, n // 2 + 1) :         # t = n/2 * (X)
        for j in range(1, n//2 + 1):        # t = n/2 * (X)
            for k in range(1, n//2 + 1):    # t = n/2 * (X)
                counter += 1                # t = c1
    

params_list = [(1,), (10,), (1000,), (10000,)]
analyze_execution_time('./plots/problem1.png', problema1, params_list, 1)