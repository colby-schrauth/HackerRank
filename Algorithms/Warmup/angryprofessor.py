t = int(raw_input())

for i in t:
    class_params = map(int, raw_input().strip().split(' '))

    n = class_params[0]
    k = class_params[1]

    arrival_times = map(int, raw_input().strip().split(' '))

    on_time = 0
    late = 0

    for x in arrival_times:
        if x <= 0:
            on_time += 1
        else:
            late += 1

    if on_time < k:
        print "YES"
    else:
        print "NO"
