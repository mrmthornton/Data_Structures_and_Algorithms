#Uses python3
import sys
import math


def minimum_distance(points):
    n = len(points)
    manhattan = [0] * n
    for i in range(n):
        manhattan = p[i][0] + p[i][1]
        xdiff = points[i][0] - points[i][0]
        ydiff = points[i][1] - points[j][1]
        d = math.sqrt(xdiff**2 + ydiff**2)
    return 10 ** 18


def nieve_minimum_distance(points):
    d_min = sys.maxsize
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            xdiff = points[i][0] - points[j][0]
            ydiff = points[i][1] - points[j][1]
            d = math.sqrt(xdiff**2 + ydiff**2)
            d_min = min(d,d_min)
    return d_min


if __name__ == '__main__':
    #data_input = sys.stdin.read()
    data_input = input("data in : ")
    data = list(map(int, data_input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = [(i,j) for i,j in zip(x,y)]
    print("{0:.9f}".format(nieve_minimum_distance(points)))
    #print("{0:.9f}".format(minimum_distance(points)))
