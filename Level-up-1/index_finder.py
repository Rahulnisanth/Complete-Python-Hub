# FINDING INDICES OF GIVEN ELEMENT :
def find_index(examples, search):
    indices = []
    for index, value in enumerate(examples):
        if value == search:
            indices.append([index])
        elif isinstance(examples[index], list): # Case for checking the list instance inside a list
            for i in find_index(examples[index], search): # Recursing the same function over the inside loop
                indices.append([index] + i) # Appending the outer index + inner index
    return indices
