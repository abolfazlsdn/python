def find_missing_ids(first_ids, second_ids):
    set1=set(first_ids)
    set2=set(second_ids)

    diff_set = set1-set2
    diff_list=list(diff_set)
    return diff_list
