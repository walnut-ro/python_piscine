def all_thing_is_obj(object: any) -> int:
#your code here
    type_names = {list: "List", tuple: "Tuple", set: "Set", dict: "Dict", str: "String"}

    object_type = type(object)
    type_name = type_names.get(object_type)

    if object_type == str:
        print(f"{object} is in the kitchen : {object_type}")
    elif type_name != None:
        print(f"{type_name} : {object_type}")
    else:
        print("Type not found")

    return 42