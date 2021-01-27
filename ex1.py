def summ(*nums):
    sum = 0
    for i in nums:
        sum += i * nums.index(i)
    return sum

print(summ(1,2,3,4))