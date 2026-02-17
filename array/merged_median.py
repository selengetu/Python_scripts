def find_median_sorted_arrays(input):
    """ 
    :type input: Dict[str, List[int]]
    :rtype: float
    """

    nums1 = input["nums1"]
    nums2 = input["nums2"]
    
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 0:
        return sum(merged[n//2 - 1:n//2 + 1]) / 2
    else:
        return merged[n//2]