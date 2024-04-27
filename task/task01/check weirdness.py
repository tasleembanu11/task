'''checking weirdness'''
def check_weirdness(n):
  if n%2!=0:
    print("weird")
  else:
    print("not weird")
def even_weird(m):
    for m in range(2,5):
      if m%2==0:
        print("not weird")
      elif m in range(6,20):
        print("weird")
      else:
        m>20
        print("not weird")
check_weirdness(3)
check_weirdness(24)

