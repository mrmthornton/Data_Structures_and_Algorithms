# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort()
    #print(segments)
    points = []
    i = 0
    n = len(segments)
    
    if n ==1:
        points.append(segments[0].end)
        return(points)
    
    in_common = [segments[0].start,segments[0].end] # the initial common segment
    
    # for each new segment, if the start is less than the common end,
    # select the greater of the two starts, and the lesser of the two ends.
    for i in range(1,n):
        if in_common[1] >= segments[i].start:
            in_common[0] = max(in_common[0],segments[i].start)
            in_common[1] = min(in_common[1],segments[i].end)
            #print("loop1",in_common)
            if i == n-1:
                points.append(in_common[1])
        else:
            points.append(in_common[1])
            in_common = [segments[i].start,segments[i].end]
            if i == n-1:
                points.append(in_common[1])
            #print("loop2",in_common)
            
    return(points)
    
    #print(points)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    for p in segments:
        if p.start > p.end:
            print("ERROR:segment order wrong")
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

    #print("Done")
    #sys.stdin.read()  # When using windows command line terminal.