def NULL_not_found(object: any) -> int:
    flag = 0
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
    elif object != object:
        print(f"Cheese: {object} {type(object)}")
    elif object == '':
        print(f"Empty: {object} {type(object)}")
    elif not object and type(object) is bool:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        flag = 1

    return flag