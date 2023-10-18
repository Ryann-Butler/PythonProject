# BASIC FEATURES
# 1. Output a list of screw types available and their respective details, including a summary report displaying (a) the total
# number of units in stock and (b) the total value of the stock.
# 2. Output a report giving the total number of units in stock in each length category.
# 3. Output a list of screws and their respective details which based on a length category entered by the user.
import matplotlib.pyplot as plt
# read in file
screw_list = []


# read from file
def read_file():
    # open txt file in read mode
    infile = open("SCREW_DATA_ENHANCED.txt")

    # search through and parse the file to the list
    for row in infile:
        # used to point to the current position in each line
        start = 0
        # set up a temporary, empty list
        string_builder = []
        # check if the row starts with a # - if it does read the next row
        if not row.startswith("#"):

            for index in range(len(row)):
                # go through row and split into a list at "," or \n
                if row[index] == "," or index == len(row) - 1:
                    # add each row item to the list
                    string_builder.append(row[start:index])
                    start = index + 1
            # build up our list
            screw_list.append(string_builder)
    # close txt file
    infile.close()


# # task 1 print summary
def print_summary():
    print("Material    | Head Type   |  Length   | Box of 50 | Box of 100| Box of 200| Cost per unit|")
    total_stock = 0
    total_value = 0
    for each_screw in screw_list:
        print(each_screw[0], each_screw[1], each_screw[2], each_screw[3], each_screw[4], each_screw[5], each_screw[6], sep="       |  ")
        # unit of stock = 50 screws
        # convert box sizes to integers (ints)
        stock_50_box_screws = int(each_screw[3])
        stock_100_box_screws = int(each_screw[4]) * 2
        stock_200_box_screws = int(each_screw[5]) * 4
        # convert cost to a float
        cost = float(each_screw[6])
        # calculate the total qty stock using a running total
        total_stock += stock_50_box_screws + stock_100_box_screws + stock_200_box_screws
        # calculate the total value of stock using a running total
        total_value += (stock_50_box_screws + stock_100_box_screws + stock_200_box_screws) * cost
        # total_value = (total_stock) *total_cost
    # print total qty stock
    print("Total number of units in stock ", total_stock)
    # print total value of stock
    print("The total value of the boxes of screws £", format(total_value, ",.2f"))


# task 2 printing screws based of length
def print_screw_length():
    stock_20mm = 0
    stock_40mm = 0
    stock_60mm = 0
    n = 0
    # loop through screw list
    for each_screw in screw_list:
        # check the length
        if each_screw[2] == "20":
            # calculate the total qty stock using a running total where length = 20
            stock_20mm += int(each_screw[3]) + (int(each_screw[4]) * 2) + (int(each_screw[5]) * 4)
        elif each_screw[2] == "40":
            # calculate the total qty stock using a running total where length = 40
            stock_40mm += int(each_screw[3]) + (int(each_screw[4]) * 2) + (int(each_screw[5]) * 4)
        elif each_screw[2] == "60":
            # calculate the total qty stock using a running total where length = 60
            stock_60mm += int(each_screw[3]) + (int(each_screw[4]) * 2) + (int(each_screw[5]) * 4)
        n += 1
    # print total stock for each screw length
    print("Total stock of 20mm screws is", stock_20mm)
    print("Total stock of 40mm screws is", stock_40mm)
    print("Total stock of 60mm screws is", stock_60mm)


# task 3
def menu_by_length():
    stock_length = 0
    # print list of options to user
    print("[1] Display list of 20mm screws",  "\n[2] Display list of 40mm screws", "\n[3] display list of 60mm screws")
    # check if value entered can be converted to an integer(int)
    try:
        # read in option number from user
        option = int(input("Enter your desired screw length:"))
    except ValueError:
        # if user input is not numerical display an error message & reload the menu
        print("The value entered is invalid, Please enter a number from the list below")
        menu_by_length()
    # check which option was selected
    if option == 1:
        # loop through values in screw list
        for each_screw in screw_list:
            # check length of screw type in current record
            length = int(each_screw[2])
            # if the length = 20 print the record
            if length == 20:
                print(each_screw[0], each_screw[1], each_screw[3], each_screw[4], each_screw[5], each_screw[6])
                # calculate total stock where length = 20
                stock_length += int(each_screw[3]) + int(each_screw[4]) * 2 + int(each_screw[5]) * 4
        print("There is ", stock_length, " 20mm screws available")
    elif option == 2:
        for each_screw in screw_list:
            length = int(each_screw[2])
            # if the length = 40 print the record
            if length == 40:
                print(each_screw[0], each_screw[1], each_screw[3], each_screw[4], each_screw[5], each_screw[6])
                # calculate total stock where length = 40
                stock_length += int(each_screw[3]) + int(each_screw[4]) * 2 + int(each_screw[5]) * 4
        print("There is ", stock_length, " 40mm screws available")
    elif option == 3:
        for each_screw in screw_list:
            length = int(each_screw[2])
            if length == 60:
                print(each_screw[0], each_screw[1], each_screw[3], each_screw[4], each_screw[5], each_screw[6])
                stock_length += int(each_screw[3]) + int(each_screw[4]) * 2 + int(each_screw[5]) * 4
        print("There is", stock_length, " 60mm screws available")


# start of menu
def screw_menu():
    # list the options available to select
    print("Welcome to simply screws! You break it, we help you fix it")
    print("[1] Display a summary")
    print("[2] Display the total number of units in each length")
    print("[3] Display list of screws based on length entered")
    print("[4] check stock or make a sale")
    print("[5] Discount on screws with the largest stocks")
    print("[6] Display a bar chart of units by length")
    print("[7] Exit the program")


# list the options available to select
def main():
    read_file()
    screw_menu()
    # read_file()
    option = int(input("Please enter your option: "))
    while option != 0:
        if option == 1:
            # summary
            print("option 1 selected")
            print_summary()  # task 1
        elif option == 2:
            print("option 2 selected")
            print_screw_length()  # task 2
        elif option == 3:
            print("option 3 selected")
            menu_by_length()  # task 3
        elif option == 4:
            print("option 4 selected")
            find_stock()  # broken
        elif option == 5:
            print("option 5 selected")
            stock_discount()  # task 5 # broken
        elif option == 6:
            print("option 6 selected")
            bar_chart()  # task 6
        elif option == 7:
            print("option 7 selected")
            exit_program()   # quit program
        else:
            print("Option unavailable, please select another!")  # error message
        print()
        # recall menu
        screw_menu()
        option = int(input("Please enter your option: "))
    print("Goodbye")


def find_stock():
    # the selection of the desired material
    print("what type of search material are you looking for?  \n [1] steel \n [2] Brass")
    try:
        # read in option number from user
        material_type = int(input("Enter your desired screw type:"))
    except ValueError:
        # if user input is not numerical display an error message & reload the menu
        print("The value entered is invalid, Please enter a number from the list below")
        find_stock()
    for each_screw in screw_list:
        if material_type == 1:
            # check length of screw type in current record
            material_type = each_screw[0]
            # if the length = 20 print the record
            if material_type == "steel":
                print(each_screw[0], each_screw[1], each_screw[3], each_screw[4], each_screw[5], each_screw[6])
            else:
                break
        else:
            # check length of screw type in current record
            material_type = each_screw[0]
            # if the length = 20 print the record
            if material_type == "brass":
                print(each_screw[0], each_screw[1], each_screw[3], each_screw[4], each_screw[5], each_screw[6])
            else:
                break




# task 5  # fix appending loop # broken, doesn't put discount in correct place in the temp list.
def stock_discount():
    # set previous_ details to first record
    previous_details = screw_list[0]
    total_stock = 0
    previous_total = 0
    n = 0
    # loop through screw list
    for i in screw_list:
        print(i)
        # set first list to details variable
        details = screw_list[n]
        # set box sizes to integers(int)
        stock_50 = int(details[3])
        stock_100 = int(details[4])
        stock_200 = int(details[5])
        # calculate total qty stock for record
        total_stock = (stock_50 + (stock_100 * 2) + (stock_200 * 4))
        # check if current total is greater than previous total
        if previous_total < total_stock:
            previous_details = details
            screw_list[n][7] = details[7]
        else:
            break
        n += 1
        previous_total = total_stock
    n = 0
    for j in screw_list:
        print(j)
        # print record currently discounted
        print("the current discount is:", details)
        # print record with the most stock
        print("place discount on:", previous_details, "?")
        # convert user input to lowercase
        place_discount = str.lower(input("press y to confirm update of previous discount"))
        # check if user input = "y"
        if place_discount == "y":
            # open txt file in append mode
            # detail_file = open("SCREW_DATA_ENHANCED.txt", "w")
            temp_list = []
            for k in screw_list:
                print(k)
                each_screw = screw_list[n]
                # write updated list to file
                # detail_file.write(each_screw)
                temp_list.append(each_screw)
                n += 1
            # detail_file.close()
            print(temp_list)
            break
        else:
            print("discount remains")
            break


# task 6 bar chart by length
def bar_chart():
    length = ["20", "40", "60"]
    # units = []
    n = 0
    stock_20mm = 0
    stock_40mm = 0
    stock_60mm = 0
    # loop through screw list
    for each_screw in screw_list:
        # check the length
        if each_screw[2] == "20":
            # calculate the total qty stock using a running total where length = 20
            stock_20mm += int(each_screw[3]) + (int(each_screw[4]) * 2) + (int(each_screw[5]) * 4)
        elif each_screw[2] == "40":
            # calculate the total qty stock using a running total where length = 40
            stock_40mm += int(each_screw[3]) + (int(each_screw[4]) * 2) + (int(each_screw[5]) * 4)
        elif each_screw[2] == "60":
            # calculate the total qty stock using a running total where length = 60
            stock_60mm += int(each_screw[3]) + (int(each_screw[4]) * 2) + (int(each_screw[5]) * 4)
        n += 1
    # add stock totals per length total_stock
    units = [stock_20mm, stock_40mm, stock_60mm]
    bar_colour = ["red", "blue", "green"]
    # set x-axis, y-axis and bar-colour
    plt.bar(length, units, color=bar_colour)
    plt.title("length of screws vs stock available")
    plt.xlabel("length of screws mm")
    plt.ylabel("number of screw available")
    plt.show()


# task 7 close option
def exit_program():
    close = str.lower(input("press Y to close the program or any other key to return to menu: "))
    if close == "y":
        print("closing program")
        exit()
    else:
        print("Returning to menu: ")
        main()


# main
main()

# read_file()
# print_summary()
# print_screw_length()
# menu_by_length()
# bar_chart()
