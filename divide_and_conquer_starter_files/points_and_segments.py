# Uses python3
import sys
import timeit
from functools import partial


def scan(scan_list,count,point_dict):
    current_segments = 0
    for tup in scan_list:
        if tup[1] == 'l':
            current_segments += 1
        elif tup[1] == 'r':
            current_segments -= 1
        elif tup[1] == 'p':
            count[point_dict[tup[0]]] += current_segments
        else:
            assert("scan() : error while scanning list")
    return count

    
def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    point_dict = {p:i for i,p in enumerate(points)}
    scan_list = [(p,'p') for p in points]
    scan_list.extend([(s,'l') for s in starts])
    scan_list.extend([(e,'r') for e in ends])
    
    #scan_list = scan_list * 10**5
    #print(timeit.Timer(scan_list.sort).repeat(1,1))
    scan_list.sort()
    
    #print(timeit.Timer(partial(scan,scan_list,count,point_dict)).repeat(1,1))
    count = scan(scan_list,count,point_dict)
    return count


def naive_count_segments(starts, ends, points):
    count = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                count[i] += 1
    return count


if __name__ == '__main__':
    data_input = sys.stdin.read()
    #data_input = input("s, p, segs, points : ")
    data = list(map(int, data_input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2*n + 2:2]
    ends   = data[3:2*n + 2:2]
    points = data[2*n + 2:]
    
    ##use nieve_count_segments
    #count = naive_count_segments(starts, ends, points)
    #for x in count:
    #    print(x, end=' ')
    #print()


    #use fast_count_segments
    count = fast_count_segments(starts, ends, points)
    for x in count:
        print(x, end=' ')
