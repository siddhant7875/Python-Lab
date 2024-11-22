def remove_duplicates_and_sort(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()  # Sort the list
    return unique_lst

# Example usage
lst = [12, 5, 8, 21, 3, 7, 5, 3]
sorted_lst = remove_duplicates_and_sort(lst)
print(f"Sorted list with unique elements: {sorted_lst}")
