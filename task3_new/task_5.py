def d(a : int,
      b : int,
      c : int,
      x : int,
      y: int=1):
    if (x >= a and y >= b) or (x >= c and y >= b):
        print("кирпич прошел")
    else:
        print("не прошел")


d(input(), input(), input(), input(), input())
