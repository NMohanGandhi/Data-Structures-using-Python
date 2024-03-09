def linear_search(numbers_list,number_to_find):
    for index,element in enumerate(numbers_list):
        #print(index,element)
        if element == number_to_find:
            return index
    return -1

numbers_list = [2,56,78,1,3,4,5,6,7,8,9]
number_to_find = 8
index = linear_search(numbers_list,number_to_find)
print(f"Number found at index {index} using linear search..")



