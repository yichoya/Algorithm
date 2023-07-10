while(1):
  i = str(input())
  if i == "0":
    break
  r = i[::-1]

  if i == r:
    print("yes")
  else:
    print("no")