my_list = [7,6,3,2,8,9,11,3]

min_val = my_list[0]
min_idx =0

for i in range(len(my_list)):
    if my_list[i] < min_val:
        min_val = my_list[i]
        min_idx = i

print(f"Lowest element in the list is {min_val} at the {min_idx} index")