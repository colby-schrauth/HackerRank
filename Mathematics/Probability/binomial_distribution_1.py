from __future__ import division

x = []

num_steps = int(raw_input())

for i in range(num_steps):
    num_written = int(raw_input())
    x.append(num_written)

print round((sum(x)/2),1)
