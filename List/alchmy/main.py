def check_ingredient_match(recipe, ingredients):
    missing=[]
    for i in recipe:
        if i not in ingredients:
            missing.append(i)

    user_item = len(recipe)- len(missing)
    user_precntagr = user_item/len(recipe)*100
    return  user_precntagr , missing