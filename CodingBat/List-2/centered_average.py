def centered_average(nums):
  return (reduce(lambda x,y:x+y,nums)-min(nums)-max(nums))/(len(nums)-2)

