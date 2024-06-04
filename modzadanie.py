def find_max_element(lst):
    if not lst:
        return None
    return max(lst)

def count_max_elements(lst):
    if not lst:
        return 0
    max_element = find_max_element(lst)
    return lst.count(max_element)