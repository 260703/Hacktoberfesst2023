# this is leet code solution (287)

def findDuplicate(nums):
    # Phase 1: Find the intersection point of the two runners.
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]
        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle.
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # The entrance to the cycle is the repeated number.
    return slow

# Example usage:
nums = [1, 3, 4, 2, 2]
result = findDuplicate(nums)
print(result)  # Output: 2
