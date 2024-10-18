def anagrams(s, t):
    return sorted(s) == sorted(t)

def frequentElements(nums, k):
    freq_dict = {num: nums.count(num) for num in set(nums)}
    return sorted(freq_dict, key=freq_dict.get, reverse=True)[:k]

def binarySearch(nums,target):
    if target in nums: return nums.index(target)
    else: return -1

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if sum((p + mid - 1) // mid for p in piles) > h: left = mid + 1
        else: right = mid
    return left

s = "cat"
t = "car"

print(anagrams(s, t))

nums1 = [1,1,1,2,2,3]
k1 = 2
print(frequentElements(nums1, k1))  # Output: [1, 2]

nums2 = [1]
k2 = 1
print(frequentElements(nums2, k2))  # Output: [1]

nums3 = [4,5,6,7,0,1,2]
target = 3
print(binarySearch(nums3, target))  # Output: 4

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))  # Output: 4
