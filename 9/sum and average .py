# sum and average

list1 = [12, 34, 56, 90, 9078, 89, 89, 65]

sum = 0
for i in list1:
    sum += i

print("the sum of elements in the list is", sum)
avg = sum / len(list1)
print("the average of the elements are", avg)

print("the maximum element in the list is", max(list1))
print("the minimumelement in the list is", min(list1))
