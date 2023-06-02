def input_error(func):
    def inner(*args):
        if args[0].startswith("add:"):
            if args[0].endswith("number"):
                return f"Please enter a name or a number for this user!"
            else:
                return f"This '{args[1]}' is already in the dictionary or you specified the wrong format of the number (it should not be marked with letters)"
        if args[0].startswith("change:"):
            if args[0].endswith("number"):
                return f"Please enter a name or a number for this user:!"
            else:
                return f"There is no such '{args[1]}' in the dictionary or you specified the wrong format of the number (it should not be marked with letters)"
        if args[0].startswith("phone:"):
            if args[0].endswith("dict"):
                return f"The user: '{args[1]}' is not in the dictionary"
            else:
                return "Add a Username or follow the rules of the command, namely: 'phone -> Name'"
    return inner


def hello():
    return "How can I help you?"


def add(user):
    user_list = user.split(" ")
    if len(user_list) > 2:
        user_name = user_list[1]
        user_phone = user_list[2]
        if (user_name not in assistant_dict) and (all(not char. isalpha() for char in user_phone)):
            assistant_dict[user_name] = user_phone
        else:
            error = input_error(add)
            return error(f"add: {user_name} in dict", user_name)
    else:
        error = input_error(add)
        return error(f"add: did not specify name or number")


def change(user):
    user_list = user.split(" ")
    if len(user_list) > 2:
        user_name = user_list[1]
        user_phone = user_list[2]
        if (user_name in assistant_dict) and (all(not char. isalpha() for char in user_phone)):
            assistant_dict[user_name] = user_phone
        else:
            error = input_error(change)
            return error(f"change: {user_name} not in dict", user_name)
    else:
        error = input_error(change)
        return error(f"change: did not specify name or number")


def phone(user):
    user_list = user.split(" ")
    if len(user_list) == 2:
        user_name = user_list[-1]
        if user_name in assistant_dict:
            return assistant_dict[user_name]
        else:
            error = input_error(phone)
            return error(f"phone: {user_name} in dict", user_name)
    else:
        error = input_error(phone)
        return error(f"phone: too many or too few arguments")


def show_all():
    return assistant_dict


def exit():
    return "Good bye!"


assistant_dict = {}


def main():
    while True:
        user_command = input("Your command: ")
        if user_command.lower() == "hello":
            print(hello())
        elif user_command.lower().startswith("add"):
            result = add(user_command)
            if result != None:
                print(result)
        elif user_command.lower().startswith("change"):
            result = change(user_command)
            if result != None:
                print(result)
        elif user_command.lower().startswith("phone"):
            print(phone(user_command))
        elif user_command.lower() == "show all":
            print(show_all())
        elif user_command.lower() == "close" or user_command.lower() == "exit" or user_command.lower() == "good bye":
            print(exit())
            break
        else:
            print("You entered the wrong command, please enter one of the following commands:'hello' or 'add Name Phone' or 'change Name Phone' or 'phone Name' or 'show all' or 'close/exit/good bye'!")


if __name__ == "__main__":
    main()
