s = input()
t = input()

answer = 0
def sub(str1, target):
  global answer
  if len(str1) == len(target):
    if target == str1:
      answer = 1
    return
  if target[-1] == 'A':
    sub(str1, target[:-1])
  if target[0] == 'B':
    sub(str1, target[:0:-1])

sub(s, t)
print(answer)