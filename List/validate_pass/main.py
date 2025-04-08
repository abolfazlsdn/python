def validate_path(expected_path, character_path):
    user_pass_gone=[]
    user_pass=character_path[1:]
    for i in expected_path:
        if i in user_pass:
            user_pass_gone.append(i)
            
    precntage_goenpath = len(user_pass_gone) *100/len(expected_path)
    return character_path[0],precntage_goenpath,

