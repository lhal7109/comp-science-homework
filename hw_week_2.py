n = int(input("How long would u like ur list to be?: "))
a = int(input("How many times would u like to perform the operation?: "))
def enter():
    nums = [] 
    for i in range(1,n + 1):
        num = int(input("What would u like number " + str(i) + " to be?: "))
        nums.append(num)
    return(nums)
def add_sub(nums):
     for i in range(0,n):
          if nums[i] % 2 == 0:
               nums[i] = nums[i] + 2
          else:
               nums[i] = nums[i] - 2 
     
def o_or_e():
    nums = enter()
    for l in range(0,a):
         add_sub(nums)
    print(nums)

o_or_e()
