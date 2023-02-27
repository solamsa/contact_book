
def add_template():
    add = {
        "dest": "details",
        "type": str,
        "nargs": 3,
        "metavar": "contact details",
        "help": "string value",
    }
    return add

def view_template():
    view = {
        "dest": "details",
        "type": str,
        "nargs": 1,
        "metavar": "all",
        "help": "str value",
    }
    return view

def del_template():
    del_t = {
        "dest": "details",
        "type": int,
        "nargs": 1,
        "metavar": "Key",
        "help": "INT value",
    }
    return del_t

