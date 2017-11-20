# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    n = len(weights)
    density = [v/w for (v,w) in zip(values,weights)] # make a list of the densitys
    den_idx = [(density[i],i) for i in range(n)] # add an index for post-sort retrieval of values and weights
    den_idx.sort(reverse=True)
    
    value_sum = 0
    for (d,i) in den_idx:
        if capacity > 0:
            if weights[i] <= capacity:
                capacity -= weights[i]
                value_sum += values[i]
            else:
                value_sum += d * capacity
                capacity = 0
                
    return value_sum


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
