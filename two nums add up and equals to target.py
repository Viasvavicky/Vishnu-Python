def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num] = i
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target number: "))
print(two_sum(nums, target))
