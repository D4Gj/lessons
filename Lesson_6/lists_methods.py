nums = [1432, 22, 3, 432, 5]
print(min(nums), max(nums))
print([1, 2, 3] + [2, 3, 4])
print([1, 2, 3] * 10)
print(sum(nums))

# добавление n элементов
# some_words = []
# n = int(input())
# for _ in range(n):
#     chars = input()
#     some_words.append(chars)
# print(some_words)
print(nums)
print(nums.pop(3))
# nums.clear()
print(nums)
# print(nums.append(100))
nums.append(100)
print(nums)

print(sorted(nums))
print(nums)
nums.sort()
print(nums)
print(nums.index(100))
nums2 = [2, 3, 4]
nums.extend(nums2)
print(nums)