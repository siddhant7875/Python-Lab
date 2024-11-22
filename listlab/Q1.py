def find_min_max(lst):
    if lst:  # Check if the list is not empty
        min_element = min(lst)
        max_element = max(lst)
        return min_element, max_element
    else:
        return None, None

# Example usage
lst = [12, 5, 8, 21, 3, 7]
min_element, max_element = find_min_max(lst)
print(f"Minimum: {min_element}, Maximum: {max_element}")
