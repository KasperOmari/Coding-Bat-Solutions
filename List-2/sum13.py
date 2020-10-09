def sum13(nums):
  cnt=0
  for i in range(len(nums)):
    if(nums[i]!=13):
      cnt+=nums[i]
    if i<len(nums)-1 and nums[i] == 13:
      nums[i]=0
      nums[i+1]=0
  return cnt

