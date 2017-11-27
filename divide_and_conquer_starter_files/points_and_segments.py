# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    n_p = len(points)
    n_s = len(starts)
    count = [0] * len(points)
    segments = [(i,j) for i,j in zip(starts,ends)]
    end_sorted = sorted(segments,
                        key=lambda e: e[1],
                        reverse=True)
    start_end_sorted = sorted(end_sorted,
                              key=lambda e: e[0],
                              reverse=True)
    
    p_i = 0 # points index
    while p_i < n_p:
        
        start_i=0 # start index
        
        # skip segments with start greater than p
        while start_i < n_s and start_end_sorted[start_i][0] > points[p_i]:
            start_i += 1

        # the segments now have start is less than or equal to p
        # count segments with end greater than or equal to p
        while start_i < n_s and start_end_sorted[start_i][1] >= points[p_i]:
            count[p_i] += 1
            start_i += 1 # examine the next segment
                   
        p_i += 1 # move on to the next point

        ## count segments where end is greater than p
        #end_sorted = sorted(start_sorted[start_i:],
        #                    key=lambda e: e[1]-e[0])
        #n_partial = len(end_sorted)
        #end_i=0
        #while end_i < n_partial and points[p_i] < end_sorted[end_i][1]:
        #    count[p_i] += 1
        #    end_i += 1
            
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
    #
    #print()

    #use fast_count_segments
    count = fast_count_segments(starts, ends, points)
    for x in count:
        print(x, end=' ')
