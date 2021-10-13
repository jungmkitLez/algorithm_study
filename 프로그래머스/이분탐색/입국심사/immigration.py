def solution(n, times):

    answer = 0

    sorted_times = sorted(times)
    min_time = sorted_times[0]
    max_time = n*sorted_times[-1]



    while min_time <= max_time:
        mid = int((min_time+max_time)/2)
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            answer = mid
            max_time = mid-1
        else:
            min_time = mid+1

    return answer



n = 6
times = [7,10]

print(solution(n,times))
