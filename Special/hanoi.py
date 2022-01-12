def hanoi(n, start, sub, dest):
  if n == 1:
    print(start, '->', dest)
    return
  
  hanoi(n - 1, start, dest, sub)
  print(start, '->', dest)
  hanoi(n - 1, sub, start, dest)

hanoi(3, 1, 2, 3)
