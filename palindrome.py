list1 = [1, 2, 3, 2, 1, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("Palindrome")
else:
    print("NOT Palindrome")
