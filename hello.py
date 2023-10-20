def add_this(x, y):
    # test with print
    print(f"This is x: {x} and the x-type {type(x)}")
    print(f"This is y: {y} and the y-type is {type(y)}")
    try:
        result = x + y
    except TypeError:
        print(f"The wrong type passed")
        result = int(x) + int(y)
        
    print(f"This is the result: {result}")
    return result


print(add_this("4", 3))
#print(add_this("one", 3))


# pdb
def add_this(x, y):
    # test with print
    # import pdb;pdb.set_trace()
    print(f"This is x: {x} and the x-type {type(x)}")
    print(f"This is y: {y} and the y-type is {type(y)}")
    try:
        result = x + y
    except TypeError:
        print(f"The wrong type passed")
        result = int(x) + int(y)
        
    print(f"This is the result: {result}")
    return result


print(add_this("4", 3))
#print(add_this("one", 3))