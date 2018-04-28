# Uses python3
import random
import sys
from functools import partial


def scan(scan_list,count):
    current_segments = 0
    for tup in scan_list:
        if tup[1] == 'L':
            current_segments += 1
        elif tup[1] == 'R':
            current_segments -= 1
        elif tup[1] == 'P':
            count[tup[2]] += current_segments
        else:
            assert("scan() : error while scanning list")
    return count

    
def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    #point_dict = {p:i for i,p in zip(points,range(len(points)))}
    #scan_list = [(p,'P',i) for p,i in point_dict]
    scan_list = [(p,'P',i) for p,i in zip(points,range(len(points)))]
    scan_list.extend([(s,'L') for s in starts])
    scan_list.extend([(e,'R') for e in ends])
    
    #scan_list = scan_list * 10**5
    #print(timeit.Timer(scan_list.sort).repeat(1,1))
    scan_list.sort()
    
    #print(timeit.Timer(partial(scan,scan_list,count,point_dict)).repeat(1,1))
    count = scan(scan_list,count)
    return count


def nieve_count_segments(starts, ends, points):
    count = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                count[i] += 1
    return count


def test():
    random.seed(36963)
    R = 1000
    loop_count = 0
    while(True):
        #create random points
        random_ints = [random.randint(1,sys.maxsize) for _ in range(3*R)]
        starts = random_ints[0::3]
        length = random_ints[1::3]
        ends = [s+e for (s,e) in zip(starts,length)]
        points = random_ints[2::3]
        #print(random_ints[0:15])
        #print(starts[0:5])
        #print(ends[0:5])
        #print(points[0:5])
        nieve = nieve_count_segments(starts, ends, points)
        fast = fast_count_segments(starts, ends, points)
        if nieve == fast:
            loop_count += 1
            if loop_count == 10:
                print("OK ",end='')
                loop_count = 0
        else:
            print("starts=", starts).format()
            print("ends  =", ends)
            print("points=", points)
            print("nieve =", nieve)
            print("fast = ", fast)


if __name__ == '__main__':
    data_input = sys.stdin.read()
    #data_input = input("s, p, segs, points : ")
    data = list(map(int, data_input.split()))
    n = data[0]
    if n == 0:
        test()
    else:
        m = data[1]
        starts = data[2:2*n + 2:2]
        ends   = data[3:2*n + 2:2]
        points = data[2*n + 2:]
    
        ##use nieve_count_segments
        #count = nieve_count_segments(starts, ends, points)
        #for x in count:
        #    print(x, end=' ')
        #print()
    
    
        #use fast_count_segments
        count = fast_count_segments(starts, ends, points)
        for x in count:
            print(x, end=' ')
