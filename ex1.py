def summ(*nums):
    if len(list(nums)) == 1:
        return
    v = list(nums)

    #sum = 0
    #for i in nums:
     #   sum += i * nums.index(i)
    #return sum

    c=v.index((v[-1]))*v.pop() + summ(v)
    return c
print(summ(1,2,3,4))