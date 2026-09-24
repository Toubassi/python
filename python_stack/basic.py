# Basic
for x in range(0, 151, 1):
  print(x)

#Multiples of 5s
for y in range(5, 1001, 5):
  print(y)

#Coding the Dojo way
for z in range(1, 101, 1):
  if z % 10 == 0:
    print('Coding Dojo')
  elif z % 5 == 0:
    print('Coding')
  else: print(z)

#That sucker's huge
total = 0
for a in range(1, 500000, 2):
  total += a
print(total)

#Countdown by 4s
for sub in range(2018, 0, -4):
  print(sub)

#Flexible counter
low_num = 1
high_num = 20
mult = 3
for m in range(low_num, high_num, 1):
  if m % mult == 0:
    print(m)