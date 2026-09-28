num = [0, -1, 2, 3, -1, 5, -2]

def biggie_size(num):
  new = []
  for x in num:
    if int(x) > 0:
      new.append(str('big'))
    else:
      new.append(x)
  return new
print(biggie_size(num))