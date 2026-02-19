def find_max_value(dictionary):
    """ 
    :type dictionary: dict
    :rtype: tuple
    """
    
    max_value = float("-inf")
    max_key = None
    max_index = -1

    for idx, (k, v) in enumerate(dictionary.items()):
        if v > max_value:
            max_value = v
            max_key = k
            max_index = idx
    return [max_value, max_key, max_index]