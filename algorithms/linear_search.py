def linear_search(search_list, target):
    flag = False
    for idx in range(len(search_list)):
        if search_list[idx].lower() == target.lower():
            flag = True
            return idx
    if not flag:
        return f"{target} is not in the list."


recipe = ['fish', 'chips', 'vinegar', 'pickles', 'tartar', 'beer']
ingredient = 'pickles'

print(linear_search(recipe, ingredient))
