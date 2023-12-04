test_list = [1, 2, 3]

test_list2 = test_list
test_list2[0] = 100
print(f"{test_list = }")
print(f"{test_list2 = }\n")

test_list3 = test_list.copy()
test_list3[0] = 1000
print(f"{test_list = }")
print(f"{test_list3 = }")