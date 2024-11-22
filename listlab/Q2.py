def second_smallest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    if len(unique_lst) < 2:
        return None  # If there are less than two unique elements
    unique_lst.sort()
    return unique_lst[1]  # Second smallest element

# Example usage
lst = [12, 5, 8, 21, 3, 7, 5]
second_smallest_element = second_smallest(lst)
print(f"Second smallest element: {second_smallest_element}")
