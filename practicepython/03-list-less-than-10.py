list_a = [1,1,2,3,5,8,11,23]
new_list = []
for item in list_a:
    if item <= 5:
        new_list.append(item)
for n in new_list:
    print(n)