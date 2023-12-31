contacts = {}


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Use help."
        except KeyError:
            return "Unknown name. Try another or use help."
        except TypeError:
            return "Unknow type. Try another or use help."
        except ValueError:
            return f"{args[1:]} is not a number. Try again!"
    return inner


def normalize(phone):
    if len(phone) == 12 and phone.startswith("380") or len(phone) == 13 and phone.startswith("+380"):
        return True
    else:
        return f"{phone} is wrong phone. Phone must start with '+380' or '380', and have minimum 12 symbols"


@user_error
def add_contact(*args):
    name = args[0].capitalize()
    phone = args[1]
    if normalize(phone) == True:
        contacts[name] = int(phone)
        return f"Add record {name = }, {phone = }"
    else:
        return normalize(phone)


@user_error
def change_phone(*args):
    name = args[0].capitalize()
    new_phone = args[1]
    rec = contacts[name]
    if rec and normalize(new_phone) == True:
        contacts[name] = int(new_phone)
        return f"Change record {name = }, {new_phone = }"
    else:
        return normalize(new_phone)


@user_error
def show_num(arg):
    cap_arg = arg.capitalize()
    if cap_arg in contacts.keys():
        return contacts[cap_arg]
    else:
        return f"I don't know {arg}'s number. If you want to add it - print 'add'"
 

@user_error
def greeting_hello():
    return "Hello! How can i help you?"


@user_error
def show_all_nums():
    return contacts


def unknown(*args):
    return "Unknown or not enough params. Try again."
        

COMMANDS = {add_contact: "add",
            change_phone: "change",
            greeting_hello: "hello",
            show_num: "phone",
            show_all_nums: "show all",
            }


def parser(text: str):
    for func, kw in COMMANDS.items():
        if text.lower().startswith(kw):
            return func, text[len(kw):].strip().split()
    return unknown, []


def main():
    while True:
        user_input = input(">>>")
        if user_input.lower() in ["good bye", "close", "exit"]:
            print("Good bye!")
            return False
        else:
            func, data = parser(user_input)
            print(func(*data))
        
        
if __name__ == '__main__':
    main()