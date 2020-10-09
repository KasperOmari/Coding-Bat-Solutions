def make_chocolate(small, big, goal):
  if big<goal//5:
    goal-=big*5
  else:
    goal-=(goal//5)*5
  return goal if small >= goal else -1

