def find_sum_max(*nums):
    sum = 0
    max = 0
    for i in nums:
        sum += i
        if i > max:
            max = i
    return sum, max

sum, max = find_sum_max(1,2,-4,7,22,100,-100,888888,9999)
print(f' sum = {sum}\n max = {max}')
