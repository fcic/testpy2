def Swcase(var):
    return {
            'a': 1,
            'b': 2,
            'c': 3,
    }.get(var,'error') 

print(Swcase('a'))