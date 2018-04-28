#Uses python3
import math
import random
import sys


def cartesian(p1,p2):
    dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return dist


def shortest(X, Y, lo, hi):
    if hi < lo: # something has gone wrong
        print("hi < lo")
        return None 
    n = hi - lo + 1
    if n < 2: # something has gone wrong
        print("n<2")
        return None
    if n <= 3: # the base case, use brute force algorithm
        return nieve_minimum_distance(X)
    
    # calculate the dividing line, x coordinate, based on halving 
    # the number of points in each area
    mid = lo + int((hi-lo)/2)

    # find the shortest distance for the points with indicies lo to hi
    d1 = shortest(X, Y, lo, mid)
    d2 = shortest(X, Y, mid+1, hi)
    delta = min(d1,d2)

    # gather the points from Y that are <d from the mid x coordinate
    x_line = X[mid][0]
    nearline = [p for p in Y if abs(p[0] - x_line) < delta]
    m = len(nearline)

    # compare each point to its neighbors with y-coordinate closer than delta
    for i in range(m):
        # a geometric packing argument shows that this loop iterates at most 7 times
        for j in range(i+1,m):
            if nearline[j][1] - nearline[i][1] < delta:
                dist = cartesian(nearline[i], nearline[j])
                if dist < delta:
                    delta = dist
            #print(j,end='')
    # return the shortest distance found within the two groups of points
    return delta
    
    
def smart_minimum_distance(points):
    # create Px, sorted by x coordinate
    Px = sorted(points,key=lambda point: (point[0],point[1]) )
    n = len(points)
    # check for coincident points
    for i in range(1,n):
        if Px[i-1] == Px[i]:
            d_min = 0
            return d_min
        
    # create Py, sorted by y coordinate
    Py = sorted(points,key=lambda point: (point[1],point[0]) )

    # use divide and conquer algorithm to find minimum distance
    d_min = shortest(Px,Py, 0, n-1)
    return d_min


def nieve_minimum_distance(points):
    d_min = sys.maxsize
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            xdiff = points[i][0] - points[j][0]
            ydiff = points[i][1] - points[j][1]
            d = math.sqrt(xdiff**2 + ydiff**2)
            d_min = min(d,d_min)
            
    return d_min


def test():
    random.seed(36963)
    R = 10
    loop_count = 0
    while(True):
        #create random points
        random_ints = [random.randint(1,100) for _ in range(2*R)]
        points = [(a,b) for a,b in zip(random_ints[:R], random_ints[R:])]
        #print(points[0:5])
        nieve = nieve_minimum_distance(points)
        fast = smart_minimum_distance(points)
        if nieve == fast:
            loop_count += 1
            if loop_count == 10:
                print("OK ",end='')
                loop_count = 0
        else:
            print("points=", points)
            print("nieve =", nieve)
            print("fast = ", fast)
            break


import time
if __name__ == '__main__':
    data_input = sys.stdin.read()
    #data_input = input("data in : ")
    data = list(map(int, data_input.split()))
    n = data[0]
    if n == 0:
        test()
    else:
        x = data[1::2]
        y = data[2::2]
        points = [(i,j) for i,j in zip(x,y)]
        #print("{0:.4f}".format(nieve_minimum_distance(points)))

        #timeit.repeat(stmt="smart_minimum_distance(points)",
        #              setup="from __main__ import smart_minimum_distance", 
        #              number=3)
        #ans = smart_minimum_distance(points)
        
        #start = time.time()
        #for _ in range(1000):
        #    smart_minimum_distance(points)
        #end = time.time()
        #print(end - start)
        print("{0:.4f}".format(smart_minimum_distance(points)))


'''
The python implementation of the closest points algorithm uses concepts found at

    https://algs4.cs.princeton.edu/99hull/ClosestPair.java.html 
    (Authors: R Sedgewick, K Wayne)

Note: could speed it up by comparing square of Euclidean distances 
instead of Euclidean distances.
'''
