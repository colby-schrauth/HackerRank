from __future__ import division

n = int(raw_input())
z = map(int, raw_input().strip().split(' '))

pos_count = 0
neg_count = 0
zer_count = 0

for i in z:
    if i > 0:
        pos_count += 1
    elif i < 0:
        neg_count += 1
    else:
        zer_count += 1

print pos_count / n
print neg_count / n
print zer_count / n
