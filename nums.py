nums = []
def find_missing_nums(nums):
    I = int(input())
    n = int(input())
    nums_2 = []
    count_2 = 1
    count = 1
    while count <= I:
        nums.append(count)
        count = count + 1
    while count_2 <= n:
        nums_2.append(count_2)
        count_2 = count_2 + 1
    if I <= n:
        print(nums_2[I:])
    return(nums_2[I:])
find_missing_nums(nums)
