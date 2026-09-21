def merge_list(list1, list2):
    result_list = []
    
    # Get odd numbers from list1
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
            
    # Get even numbers from list2
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
            
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))