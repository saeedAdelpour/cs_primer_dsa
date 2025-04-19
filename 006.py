def has_duplicate(_list):
    """
    1- for each in array
        check every other in the array
    O(n^2)

    2- sort array, iterate through adjacent pairs
    O(nlogn) + O(n)
    -------- + -----------
      sort       iterate

    3- iterate once through, build a has map/hash table
    O(n)
    """
