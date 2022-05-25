DATA = {}
list_command = []


def input_error(func):
    def wrapper():
        try:
            return func()
        except IndexError:
            return "Error,please enter 'command' 'name' 'number'"
        except KeyError:
            return "Error,please enter 'phone' 'name'"
        except ValueError:
            return "Error,please enter 'command' 'name' 'number'"
    return wrapper


def greeting():
    return "How can I help you?"


def exit1():
    return "Good bye!"


def exit2():
    return "Good bye!"


def exit3():
    return "Good bye!"


@input_error
def adding():
    if len(list_command) > 3:
        raise IndexError
    DATA.update({list_command[1]: list_command[2]})
    return "You add a new contact"


@input_error
def changing():
    if len(list_command) > 3:
        raise ValueError
    for k in DATA.keys():
        if k == list_command[1]:
            DATA[k] = list_command[2]
    return f"Contact {list_command[1].title()} changed"


@input_error
def get_phone():
    if not 1 < len(list_command) < 3:
        raise KeyError
    result = DATA.get(list_command[1])
    return f'Contact: {list_command[1].title()} {result}'


def show():
    cont_list = []
    for k, v in DATA.items():
        _ = k.title() + ' ' + str(v)
        cont_list.append(_)
        line = ('\n').join(cont_list)
    return f'Contacts:\n{line}'


COMMANDS = {greeting: "hello", exit1: "good bye",
            exit2: "close", exit3: "exit", show: 'show all'}


def main():
    true = True
    while true:
        user_in = input(">>> ")
        if user_in == ' ' or user_in == '':
            break
        user_input = user_in.lower()
        for k, v in COMMANDS.items():
            if v == user_input:
                print(k())
            if user_input in ['good bye', 'exit', 'close']:
                true = False
        lst = user_input.split(' ')
        if lst[0] == 'add':
            list_command.extend(lst)
            print(adding())
            list_command.clear()
        if lst[0] == 'change':
            list_command.extend(lst)
            print(changing())
            list_command.clear()
        if lst[0] == 'phone':
            list_command.extend(lst)
            print(get_phone(), end='\n')
            list_command.clear()


if __name__ == "__main__":
    main()
