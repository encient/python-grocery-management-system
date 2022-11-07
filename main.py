import time
# import time for .sleep() built in function

def viewGroceries():
# admin/customer to view groceries details

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in read mode
    try:
        fileHandler = open("groceries_details.txt","r")
    except:
        print("Unable to open the file.")
        exit()

    print()
    print("Category | Name | Spec | Price | Exp Date | Stock")
    print("-------------------------------------------------")

    # print every line from the file
    for line in fileHandler:
        line = line.rstrip()
        print (line)
    fileHandler.close()
    # suspends for 1 second before return to main menu
    # this can reduce confusion as words will not come in bulk
    time.sleep(1)
    print()
    print("Returning to main menu ...")
    time.sleep(1)




def inputGroceries():
# prompts input from admin for groceries details

    # create a master list for groceries details
    groceries = []

    # try and except is used to make sure the input is only number
    try:
        # admin can choose number of groceries they want to upload
        n = int(input("Enter the number of groceries that you would like to upload: "))    
        # loop in range to prompt for admin input
        for i in range(n):
            # details for one grocery are saved in a list
            groc = []
            # extra feature: put 2 arguments in input
            print("Groceries Category", i+1, ": ", end="")
            grocCategory = input()            
            grocName = input("Groceries Name: ")            
            grocSpec = input("Groceries Specification: ")            
            grocPrice = input("Groceries Price (RM): ")            
            grocExp = input("Groceries Expiry Date (DD/MM): ")            
            grocStock = input("Groceries Stock: ")
            groc.append(grocCategory.title())
            groc.append(grocName.title())
            groc.append(grocSpec)
            groc.append(grocPrice)
            groc.append(grocExp)
            groc.append(grocStock)
            # groc list appended to master list
            groceries.append(groc)
        return groceries

    except:
        print("Invalid input.")

    
def uploadGroceries():
# allows admin to upload new groceries

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in append mode
    try:
        fileHandler = open("groceries_details.txt","a")
    except:
        print("Unable to open the file.")
        exit()

    # store groceries details from inputGroceries function into variable    
    groceries = inputGroceries()

    # append groceries details line by line
    try:
        for grc in groceries:
            for g in grc:
                # write a grocery detail, split each detail with | , start a new line for another grocery
                fileHandler.write(g)
                fileHandler.write(" | ")
            fileHandler.write("\n")            
        fileHandler.close()

        print("Uploaded successfully.")

    except:
        return



def searchGroceries():
# allows admin to search groceries using word/character
    while True:
        # try to check if the text file is available or not
        # exit program if file not found
        # open file in read mode
        try:
            fileHandler = open("groceries_details.txt", "r")
        except:
            print("Unable to open the file.")
            exit()

        # prompt for word/character that admin wants to search  
        searchKey = input("Enter the word that you would like to search (Enter to exit): ")
        # read file in lines
        lines = fileHandler.readlines()
        # break the loop & return to menu if admin clicks enter
        if (searchKey == ""):
            print("\nReturning to admin menu ...")
            time.sleep(1)
            break
        print()
        print("Category | Name | Spec | Price | Exp Date | Stock")
        print("-------------------------------------------------")

        # search by word in lines
        # whole line will be printed if same word is found in the file
        for line in lines:
            if searchKey.lower() in line.lower():
                print (line.rstrip())
            else:
                continue
        fileHandler.close()
        print()



def filterGroceries():
# extra feature: allows admin/customer to filter groceries category

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in read mode
    try:
        fileHandler = open("groceries_details.txt", "r")
    except:
        print("Unable to open the file.")
        exit()

    # get input from user & count the length
    # read file in lines
    filterKey = input("Enter the category that you would like to filter: ")
    len_filter = len(filterKey)
    lines = fileHandler.readlines()

    # stop the function if the input is enter key
    if (filterKey == ""):
        print("Invalid input.")
        return

    print("Category | Name | Spec | Price | Exp Date | Stock")
    print("-------------------------------------------------")

    # looping the word by line
    # search for the first word with same length of words and same word
    # this can make sure it is only filtering for groceries category and not other groceries details
    # line will be printed when the category is matched
    for line in lines:
        if (len_filter == len(line[:len_filter])) & (filterKey.lower() == line[:len_filter].lower()):
            print (line.rstrip())
    fileHandler.close()

    # suspends for 1 second before and after printing the line
    # this can reduce confusion as words will not come in bulk
    time.sleep(1)
    print()
    print("Returning to main menu ...")
    time.sleep(1)



def updateGroceries():
# allows admin to edit groceries details
# edit groceries details by replacing the original word to edited word

    while True:
        # try to check if the text file is available or not
        # exit program if file not found
        # open file in read mode
        try:
            fileHandler_r = open("groceries_details.txt", "r")

        except:
            print("Unable to open the file.")
            exit()

        # select specific details to update
        # input will be converted to lower case
        updateChoice = input("Choose the information that you would like to update (Spec/Price/Stock) or Enter to exit\n")
        uC = updateChoice.lower()
        
        if (uC == "spec") or (uC == "price") or (uC == "stock"):
            # read file by lines
            # prompt for groceries name
            lines = fileHandler_r.read()
            productName = input("Enter the product name that you would like to update: ")

            # prompt for original word if inputed groceries name is found in file
            if productName.lower() in lines.lower():              
                updateKey = input("Enter the word that you would like to update: ")

                # prompt for word that admin wants to change to if inputed original word is found in file
                if updateKey.lower() in lines.lower():
                    updatedKey = input("Enter the word that you would like to change to: ")
                    # replace the word in the specific line
                    update = lines.replace(updateKey.title(), updatedKey.title())
                    # close file & reoopen file in write mode
                    # rewrite the line
                    fileHandler_r.close()
                    fileHandler_w = open("groceries_details.txt", "w")
                    fileHandler_w.write(update)
                    fileHandler_w.close()
                    print("Updated successfully.")

            # print a notice if inputed groceries name not found
            else:
                print("Product not found. Please try again.")

        # break loop if admin inputs enter
        elif (updateChoice == ""):
            break
        
        else:
            print("Invalid input.")

        fileHandler_r.close()



def deleteGroceries():
# allows admin to delete groceries: one whole grocery/specific grocery information

    while True:
        print()
        print("Select the operation that you would like to perform:")
        print("1. Delete one whole grocery")
        print("2. Delete specific grocery information")
        print("3. Back to admin menu")
        print()

        deleteChoice = input("Enter selection: ")

        if (deleteChoice == "1"):
        # deleting the entire line of the file
            while True:
                # try to check if the text file is available or not
                # exit program if file not found
                # open file in read mode
                try:
                    fileHandler_r = open("groceries_details.txt", "r")
                except:
                    print("Unable to open the file.")
                    exit()

                # read file by lines
                # prompt for product name
                lines = fileHandler_r.readlines()
                dltKey = input("Enter the product name that you would like to delete the details (Enter to exit): ").lower()

                # break the loop if admin inputs enter
                if (dltKey == ""):
                    break

                # open the file in write mode
                fileHandler_w = open("groceries_details.txt","w")                

                # overwrite the file line by line
                # .find() is used to search for product name entered by admin from the file
                # line that contains the product name to be deleted will be avoided to overwrite
                for line in lines:    
                    if (line.lower().find(dltKey) != -1):
                        pass
                    else:
                        fileHandler_w.write(line)
                fileHandler_w.close()
                print("Loading done. Please back to 'View Groceries' to check whether the delete has been done.")
                print()
            fileHandler_r.close()


        elif (deleteChoice == "2"):
        # replacing specific information with '-'
            while True:
                # try to check if the text file is available or not
                # exit program if file not found
                # open file in read mode
                try:
                    fileHandler_r = open("groceries_details.txt", "r")
                except:
                    print("Unable to open the file.")
                    exit()

                # prompt for choice to delete    
                dltChoice = input("Choose the information that you would like to delete (Spec/Price/Stock) or Enter to exit\n").lower()

                if (dltChoice == "spec") or (dltChoice == "price") or (dltChoice == "stock"):
                    # read file by lines
                    # prompt for product name
                    lines = fileHandler_r.read()
                    productName = input("Enter the product name that you would like to delete the details: ")

                    # prompt for specific information that admin wants to delete
                    # only works if the product name is found in the file
                    if (productName.lower() in lines.lower()):              
                        deleteKey = input("Enter the word that you would like to delete: ")

                        # replace the word with '-'
                        # open the file in write mode
                        # overwrite the entire line that contains the word that has been replaced
                        if (deleteKey.lower() in lines.lower()):
                            delete = lines.replace(deleteKey.title(), "-")
                            fileHandler_r.close()
                            fileHandler_w = open("groceries_details.txt", "w")
                            fileHandler_w.write(delete)
                            fileHandler_w.close()
                            print("Deleted successfully.")

                # break the loop if admin inputs enter
                elif (dltChoice == ""):
                    break

                # validation
                else:
                    print("Invalid input.")
                fileHandler_r.close()

        # break the loop to return to menu        
        elif (deleteChoice == "3"):
            break

        # validation
        else:
            print("Invalid input. Please enter 1, 2 or 3 only.")



def adminLogin():
    loop = 0
    while (loop == 0):
        # admin credential placed in adminCredential list
        # prompt to enter username once enters the program
        adminCredential = ["admin", "password"]
        adminUsername = input("Enter username: ")

        # correct username entered
        if (adminUsername == adminCredential[0]):
            while (loop == 0):
                # prompt for password
                adminPassword = input("Enter password: ")

                # correct password entered
                if (adminPassword == adminCredential[1]):
                    adminMenu()
                    break

                # incorrect password entered
                else:
                    # ask to continue or return to menu
                    # try and except to validate the input as it must be integer
                    try:
                        loop = int(input("Incorrect password. Please try again. Enter 0 to continue or enter 1 to exit.\n"))
                        if (loop == 0):
                            continue
                        elif (loop == 1):
                            break
                        else:
                            print("Invalid input.")

                    except:
                        print("Invalid input. Please try again.")
            break

        # incorrect username entered
        else:
            # ask to continue or return to menu
            # try and except to validate the input as it must be integer
            try:
                loop = int(input("Incorrect username. Please try again. Enter 0 to continue or enter 1 to exit.\n"))
                if (loop == 0):
                    continue
                elif (loop == 1):
                    break
                else:
                    print("Invalid input.")
            except:
                print("Invalid input. Please try again.")



def customerLogin():
    loop = 0
    while (loop == 0):
        # try to check if the text file is available or not
        # exit program if file not found
        # open file in read mode
        try:
            fileHandler = open("customers_details.txt", "r")
        except:
            print("Unable to open the file.")
            exit()

        # read file by lines
        # prompt for username
        lines = fileHandler.readlines()
        inputUsername = input("Enter username (Enter to exit): ")

        for line in lines:
            # split each details of the line into splitContent list
            splitContent = line.split(" | ")
            username = splitContent[1]
            password = splitContent[7]

            # correct username (username found in second element from one of the lines)
            # will keep looping if username is entered is invalid
            # else statement is not suitable in for loop
            # this is because statement will be printed repeatedly for each of the line that does not contain the username
            if (inputUsername == username.strip()):
                while loop == 0:
                    # prompt for password
                    inputPassword = input("Enter password (Enter to exit, Enter 'yes' if forgot password): ")

                    # correct password
                    if (inputPassword == password.strip()):
                        loop = 1
                        print("Login successful. Welcome!")
                        time.sleep(1)
                        # redirect customer to customer menu & break the current loop after they exit the menu
                        customerMenu()
                        break

                    # exit program (input enter)
                    elif (inputPassword == ""):
                        loop = 1
                        break

                    # extra feature: forgot password
                    elif (inputPassword.lower() == "yes"):
                        for line in lines:
                            # split each details of the line into splitContent list
                            # username is the second element in the list
                            # answer for security question (securityKey) is the nineth element in the list
                            splitContent = line.split(" | ")
                            username = splitContent[1]
                            securityKey = splitContent[8]

                            # validate if username exists
                            if (inputUsername == username.strip()):                          
                                print()
                                print("-----------------")
                                print("SECURITY QUESTION")
                                print("-----------------")
                                print("1. What is the name of the city you were born?")
                                print("2. What is your favourite animal?")
                                print("3. What is your favourite movie?")
                                print()
                                                                                    
                                while (loop == 0):
                                    # prompt for answer for security question
                                    # only correct answer is accepted
                                    # otherwise will keep looping unless input enter
                                    secKey = input("Enter your answer for the question when you registered (Enter to exit): ")

                                    # break the loop and return to menu if customer inputs enter
                                    if (secKey == ""):
                                        loop = 1
                                        break

                                    # correct answer for security question
                                    # print password of the username and break the loop (return to menu)
                                    elif (secKey == securityKey.strip()):
                                        print("Your password is:", splitContent[7])
                                        loop = 1
                                        break

                    # wrong password
                    else:
                        print("Wrong password. Please try again.")

        # break the loop if customer inputs enter
        if (inputUsername == ""):
            break

        fileHandler.close()



def registerAccount():
    # create an empty list to store each details
    cusDetails = []
    # prompt user input for each details
    cusName = input("Full Name: ")
    cusUsername = input("Username: ")                       
    cusGender = input("Gender (M/F): ")
    cusBirth = input("Date of Birth (DD/MM/YY): ")
    cusAdd = input("Address: ")
    cusNo = input("Contact Number: ")
    cusEmail = input("Email: ")
    cusPassword = input("Password: ")

    # prompt to reenter password
    while True:
        cusPassword2 = input("Reenter password: ")

        # reenter correct password
        if (cusPassword == cusPassword2):
            # ask for answer for security question
            print()
            print("-----------------")
            print("SECURITY QUESTION")
            print("-----------------")
            print("1. What is the name of the city you were born?")
            print("2. What is your favourite animal?")
            print("3. What is your favourite movie?")
            print()
            securityAns = input("Please enter the answer for one of the security question: ")

            # append each details into cusDetails list
            cusDetails.append(cusName.title())
            cusDetails.append(cusUsername)                        
            cusDetails.append(cusGender.title())
            cusDetails.append(cusBirth)
            cusDetails.append(cusAdd.title())
            cusDetails.append(cusNo)
            cusDetails.append(cusEmail)
            cusDetails.append(cusPassword)
            cusDetails.append(securityAns)

            # try to check if the text file is available or not
            # exit program if file not found
            # open file in append mode            
            try:
                fileHandler = open("customers_details.txt","a")
            except:
                print("Unable to open customers details file.")
                exit()

            # append each details into file and concatenate ' | ' after each detail
            for cd in cusDetails:
                fileHandler.write(cd + " | ")

            # a new line is created after all details has been written in file
            # so that details of next customer will be written in a new line to avoid confusion
            # loop will be broken and will be redirected back once successfully registered
            fileHandler.write("\n")
            fileHandler.close()
            print("Account has been registered.")
            print("Please return to main menu and login as 'Registered Customer'.")
            break

        # reenter wrong password    
        else:
            loop = 0
            try:
                # ask if user wants to continue or exit
                loop = int(input("Incorrect password. Please try again. Enter 0 to continue or enter 1 to exit.\n"))

                # continue retry enter password
                if (loop == 0):
                    continue
                # break the loop and return to menu
                elif (loop == 1):
                    break
                # validation
                else:
                    print("Invalid input.")
            except:
                print("Invalid input. Please try again.")



def viewPersonal():
# allows customers to view personal information that they registered

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in read mode
    try:
        fileHandler = open("customers_details.txt", "r")
    except:
        print("Unable to open the file.")
        exit()

    # read file by lines
    lines = fileHandler.readlines()
    loop = 0
    
    while (loop == 0):
        # prompt for username
        cusUsername = input("Enter username (Enter to exit): ")

        # break the loop if user inputs enter
        if (cusUsername == ""):
            loop = 1
            break
        
        for line in lines:
            # split each content in line into a list
            splitContent = line.split(" | ")
            username = splitContent[1]

            # print customer details if username is same as the second element of the list
            if (cusUsername == username.strip()):
                print("Name | Username | Gender | DOB | Address | Contact No. | Email | Password | Sec |")
                print("---------------------------------------------------------------------------------")
                print(line)
                loop = 1

        # loop = 0 indicates nothing changes
        # thus this indicates that username is not found
        if (loop == 0):
            print("Username not found.")

    fileHandler.close()



def inputOrder():
# prompts input from customer for order placement

    # create a master list for order placing details
    # prompt for customer username
    order = []
    username = input("Enter username: ")

    # try and except is used to make sure the input is only number
    try:
        # customer can choose number of order they want to place
        n = int(input("Enter the number of order you would like to place: "))

        # loop in range to prompt for user input            
        for i in range(n):
            # try to check if the text file is available or not
            # exit program if file not found
            # open file in append mode
            try:
                fileHandler = open("groceries_details.txt","r")
            except:
                print("Unable to open the file.")
                exit()

            # details for each order are saved in a list    
            orde = []
            ordeName = input("Groceries Name: ")

            # read file by lines
            lines = fileHandler.readlines()

            for line in lines:
                # split content of each detail from groceries details file into a list
                splitContent = line.split(" | ")
                # groceries name is the second element of the list
                groceriesName = splitContent[1]
                # convert stock detail from string to integer
                groceriesStock = int(splitContent[5])
                groceriesPrice = splitContent[3]

                # prompt for quantity for the order if the grocery name is found in second element of the list
                if (ordeName.lower() == groceriesName.lower()):
                    ordeQuantity = int(input("Quantity: "))

                    # extra feature: groceries stock
                    # able to place order only if the order quantity is same or less than the stock amount
                    if (ordeQuantity <= groceriesStock):
                        # append each detail of order placement into orde list
                        orde.append(username)
                        orde.append(groceriesName)
                        orde.append(groceriesPrice)
                        orde.append(ordeQuantity)

                        # append orde list into master list
                        order.append(orde)
                        print("Ordered successfully.")

                    # fail to place order if order quantity exceeded the available stock
                    else:
                        print("Sorry, we do not have enough stock for the above quantity.")

        return order
        fileHandler.close()

    except:
        print("Error input.")



def placeOrder():
# allows customer to place order

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in append mode
    try:
        fileHandler = open("customers_order.txt","a")
    except:
        print("Unable to open the file.")
        exit()

    # store order details from inputOrder function into variable    
    order = inputOrder()

    try:
        for orde in order:
            for o in orde:
                # append each order detail, split each detail with | , start a new line for another order
                fileHandler.write(str(o))
                fileHandler.write(" | ")
            fileHandler.write("\n")            
        fileHandler.close()

        # call for function for payment after all orders have been appended
        payOrder()

    except:
        return



def payOrder():
# allows customer to pay for their order

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in read mode
    try:
        fileHandler = open("customers_order.txt","r")
    except:
        print("Unable to open the file.")
        exit()

    # read file by lines
    lines = fileHandler.readlines()
    total = 0
    # prompt for customer username
    username = input("Enter username to make payment: ")
    
    print()
    print("Successful order is listed below:")
    print("Username | Name | Price | Quantity |")
    print("------------------------------------")

    for line in lines:
        # split each content in line into a list
        # registered customer username is the first element of the list
        splitContent = line.split(" | ")
        splitUsername = splitContent[0]

        # if username is valid
        if (username == splitUsername.strip()):
            # display the customer order
            print(line.strip())
            # convert price from string to float
            # convert quantity from string to integer
            price = float(splitContent[2])
            quantity = int(splitContent[3])
            # count total amount to be paid for the order
            total = total + (price*quantity)
    fileHandler.close()
    
    print()
    print("PAYMENT")
    print("Total amount to be paid (RM):", total)

    # total = 0 indicates that there is no order from the customer
    if (total == 0):
        print("You have no order in our system.")
        time.sleep(1)

    # show total amount to customer & ask for card number
    else:
        cardNo = input("Enter your card number: ")
        print("Loading...")
        time.sleep(1)
        print("Payment successful. Thank you!")



def viewOrder():
# allows users (admin/customers) to view order of specific customer

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in read mode
    try:
        fileHandler = open("customers_order.txt","r")
    except:
        print("Unable to open the file.")
        exit()

    # read file by lines
    # prompt username of the customer
    lines = fileHandler.readlines()
    username = input("Enter username: ")
    print("Username | Name | Price | Quantity |")
    print("------------------------------------")

    for line in lines:
        # split each content in line into a list
        splitContent = line.split(" | ")
        # username is the first element of the lsit
        splitUsername = splitContent[0]
        # print entire line if the inputed username is valid
        if username == splitUsername.strip():
            print(line.strip())
    fileHandler.close()

    # suspends for one second for user to have a clearer view on the order (to reduce confusion)
    time.sleep(1)
    print()
    print("Returning to main menu ...")
    time.sleep(1)



def viewCusOrder():
# allows admin to view order of all customers

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in read mode    
    try:
        fileHandler = open("customers_order.txt","r")
    except:
        print("Unable to open the file.")
        exit()

    print("Username | Name | Price | Quantity |")
    print("------------------------------------")

    # print each line of the file using for loop
    for line in fileHandler:
        print(line.strip())
    fileHandler.close()

    # suspends for one second for user to have a clearer view on the order (to reduce confusion)
    time.sleep(1)
    print()
    print("Returning to main menu ...")
    time.sleep(1)



def searchItem():
# allows admin to search order for specific item

    # try to check if the text file is available or not
    # exit program if file not found
    # open file in read mode    
    try:
        fileHandler = open("customers_order.txt","r")
    except:
        print("Unable to open the file.")
        exit()

    # read file by lines
    # prompt for product name
    lines = fileHandler.readlines()
    item = input("Enter product name: ")
    print("Username | Name | Price | Quantity |")
    print("------------------------------------")

    for line in lines:
        # split each content in line into a list
        splitContent = line.split(" | ")
        # product name is the second element of the list
        splitProduct = splitContent[1]
        # print the entire line if the inputed product name is valid
        if (item.lower() == splitProduct.lower().strip()):
            print(line.strip())
    fileHandler.close()

    # suspends for one second for user to have a clearer view on the order (to reduce confusion)
    time.sleep(1)
    print()
    print("Returning to main menu ...")
    time.sleep(1)



def newCustomerMenu():
# menu for new customers
    print()
    print("_________________________________________________________")
    print("                    NEW CUSTOMER MENU                    ")
    print("_________________________________________________________")

    # start looping
    # program will keep looping if invalid input
    while True:
        # display operations that they could perform
        print()  
        print("Select the operation that you would like to perform: ")
        print(" 1. View groceries")
        print(" 2. Register an account")
        print(" 3. Back to main menu")
        print()

        # prompt for operation choice
        choice = input("Enter selection: ")

        # call different functions for different choices
        if (choice == "1"):
            viewGroceries()
        elif (choice == "2"):
            registerAccount()
        # break the loop to return to main menu
        elif (choice == "3"):
            break
        else:
            print("Invalid input. Please try again.")



def customerMenu():
# menu for registered customers
    print()
    print("_________________________________________________________")
    print("               REGISTERED CUSTOMER MENU                  ")
    print("_________________________________________________________")

    # start looping
    # program will keep looping if invalid input
    while True:
        print()
        print("Select the operation that you would like to perform: ")
        print(" 1. View groceries")
        print(" 2. Filter groceries categories")
        print(" 3. Place an order & Do payment")
        print(" 4. View own order")
        print(" 5. View personal information")
        print(" 6. Back")
        print()

        # prompt for operation choice
        choice = input("Enter selection: ")

        # call different functions for different choices
        if (choice == "1"):
            viewGroceries()
        elif (choice == "2"):
            filterGroceries()
        elif (choice == "3"):
            placeOrder()
        elif (choice == "4"):
            viewOrder()
        elif (choice == "5"):
            viewPersonal()
        # break the loop to return to main menu
        elif (choice == "6"):
            break
        else:
            print("Invalid input. Please try again.")


               
def adminMenu():
# menu for admin
    print()
    print("_________________________________________________________")
    print("                      ADMIN MENU                         ")
    print("_________________________________________________________")

    # start looping
    # program will keep looping if invalid input    
    while True:
        print()
        print("Select the operation that you would like to perform: ")
        print(" 1. View groceries")
        print(" 2. Search specific groceries detail")
        print(" 3. Filter groceries categories")
        print(" 4. Upload groceries")
        print(" 5. Update/Modify groceries information")
        print(" 6. Delete groceries")        
        print(" 7. View customers' order")
        print(" 8. Search order (for specific customer)")
        print(" 9. Search order (for specific item)")
        print("10. Back to main menu")
        print()

        # call different functions for different choices
        choice = input("Enter selection: ")

        if (choice == "1"):
            viewGroceries()
        elif (choice == "2"):
            searchGroceries()
        elif (choice == "3"):
            filterGroceries()
        elif (choice == "4"):
            uploadGroceries()
        elif (choice == "5"):
            updateGroceries()
        elif (choice == "6"):
            deleteGroceries()
        elif (choice == "7"):
            viewCusOrder()
        elif (choice == "8"):
            viewOrder()
        elif (choice == "9"):
            searchItem()
        # break the loop to return to main menu
        elif (choice == "10"):
            break
        else:
            print("Please enter the number listed above only. Please try again.")



def mainMenu():
# landing page menu
    print("*********************************************************************")
    print("   _______  ______    ______   _____            ______    _____ ")
    print("   |        |     \  |        |       |      | |         /     \ ")
    print("   |        |      | |        |       |      | |        /       \ ")
    print("   |______  |_____/  |______  |_____  |______| |       |    |    |")
    print("   |        |   \    |              | |      | |       |    |    |")
    print("   |        |    \   |              | |      | |        \       / ")
    print("   |        |     \  |______  ______| |      | |______   \_____/")
    print()
    print("*********************************************************************")

    # start looping
    # program will keep looping if invalid input        
    while True:
        print()
        print("Select a user that you would like to perform in this system: ")
        print("1. Admin")
        print("2. New Customer")
        print("3. Registered Customer")
        print("4. Exit")
        print()

        # call different functions for different choices
        choice = input("Enter selection: ")

        if (choice == "1"):
            adminLogin()
        elif (choice == "2"):
            newCustomerMenu()
        elif (choice == "3"):
            customerLogin()
        # break the loop & end the program
        elif (choice == "4"):
            print("Thank you for your time in FRESHCO. Have a great day ahead!")
            print("*************************************************************")
            print("  _______           ______                   _____    __ ")
            print("     |    |      | |      | |\     | |    / |        |  |")
            print("     |    |      | |      | | \    | |   /  |        |  |")
            print("     |    |______| |______| |  \   | |__/   |_____   |  |")
            print("     |    |      | |      | |   \  | |  \         |  |__|")
            print("     |    |      | |      | |    \ | |   \        |   __ ")
            print("     |    |      | |      | |     \| |    \  _____|  |__|")
            print()
            print("*************************************************************")
            break
        else:
            print("Please enter the number listed above only. Please try again.")
        


# start the program by calling main function
mainMenu()
