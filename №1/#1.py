""""""
a = int(input(""))
b = int(input(""))
c = int(input(""))
listik = [a, b, c]
sr_ar = (a + b + c) / 3  # arithmetic mean
print(sr_ar)

import statistics

listik = [a, b, c]
fk = statistics.harmonic_mean(listik)
point = "{:.7}".format(fk)
print(point)

big = max(a, b, c)
small = min(a, b, c)
first_task = big ** small
average = big - small
result = first_task / average
print(result)
""""""
