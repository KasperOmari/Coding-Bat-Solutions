def array_front9(nums):
  x=0
  for i in range(min(len(nums), 4)):
    x += nums[i]==9
  return x > 0

