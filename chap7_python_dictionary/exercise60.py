test_string = "aabbbbcccccd"

cnt_dict = {}
for char in test_string:
    cnt_dict[char] = cnt_dict.get(char, 0) + 1
print(cnt_dict)