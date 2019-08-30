checklist = list()


# CREATE
def create(item):
    checklist.append(item)


# READ
def read(index):
    try:
        return checklist[index]
    except:
        return None


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{}: {}".format(index, list_item))
        index += 1


# UPDATE
def update(index, item):
    checklist[index] = item


# Mark an item with a √
def mark_completed(index):
    checked = "√ " + read(index)
    update(index, checked)
    return checked


# Main menu
def select(function_code):
    code = function_code.lower()

    # Create item
    if code == "c":
        input_item = user_input("Input an item: ")
        create(input_item)
        print("Success!")

    # Read item
    elif code == "r":
        item_index = user_input("Which index number? ")
        check = check_index_validity(item_index)
        if check == "Success!":
            print(read(int(item_index)))
        print(check)

    # Update item
    elif code == "u":
        item_index = user_input("Which index number? ")
        check = check_index_validity(item_index)
        if check == "Success!":
            input_item = user_input("Input an item: ")
            update(int(item_index), input_item)
        print(check)

    # Mark an item as complete
    elif code == "m":
        item_index = user_input("Which index number? ")
        check = check_index_validity(item_index)
        if check == "Success!":
            mark_completed(int(item_index))
        print(check)

    # Destroy item
    elif code == "d":
        item_index = user_input("Which index number? ")
        check = check_index_validity(item_index)
        if check == "Success!":
            destroy(int(item_index))
        print(check)

    # Print all items
    elif code == "p":
        list_all_items()

    # Quit the program
    elif code == "q":
        return False

    # Default
    else:
        print("Invalid option")
    return True


# DESTROY
def destroy(index):
    checklist.pop(index)


# Sanitize user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input


# Checks if an index is a number and if that index exists
def check_index_validity(index):
    item_index = index
    if (item_index.isnumeric()):
        item_index = int(item_index)
        if read(item_index):
            return "Success!"
        else:
            return "Index does not exist"
    else:
        return "Not a valid index"

# Testing
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

    select("C")
    list_all_items()

    select("R")
    list_all_items()

    user_value = user_input("Please Enter a value: ")
    print(user_value)

    print(mark_completed(0))


test()

running = True
while running:
    selection = user_input("""
        Press C to add to list, R to Read from list, P to display list,
        U to update list, D to destroy item on list, or M to √ an item.
        Press Q to quit:
        """)
    running = select(selection)
