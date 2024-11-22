def search_element(lst, element):
    if element in lst:
        return f"Element {element} found in the list."
    else:
        return f"Element {element} not found in the list."

# Example usage
lst = [12, 5, 8, 21, 3, 7]
element_to_search = 8
result = search_element(lst, element_to_search)
print(result)
