def replace_null_values(lst):
    """ 
    :type lst: List[Union[int, None]]
    :rtype: List[Union[int, None]]
    """
    
    for i in range(1, len(lst)):
        if lst[i] is None:
            lst[i] = lst[i-1]
    return lst