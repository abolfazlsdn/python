def merge(dict1, dict2):
    base_dict = dict2
    for i in dict1:
          if i not in base_dict:
               base_dict[i]=dict1[i]
    return base_dict
    


def total_score(score_dict):
    total_new_score=0
    for score ,vlaue in score_dict.items():
          total_new_score+=vlaue
    return total_new_score