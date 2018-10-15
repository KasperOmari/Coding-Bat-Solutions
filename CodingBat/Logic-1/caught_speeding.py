def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
  if speed<=60:
    return 0
  return 1 if speed >= 61 and speed <= 80 else 2

