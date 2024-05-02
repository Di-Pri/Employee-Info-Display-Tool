# Description
# The program prompts user for an employee's first name, last name, and
# SSN while ensuring the SSN's correct format; and displays the employee's
# initials, generated email address, and the last four digits of their SSN.
# ---------------------------------------------

# This function will display the start of the project
def projectStart():
    print('Start of Project')
    print('-' * 50 )
    print('\tEmployee Identification')
    print('-' * 50 + '\n')

# This function will display the end of the project
def projectEnd():
    print('-' * 50)
    print('End of Project')

# This function returns a string input from the user
def getStringData(prompt):
    while True:
        value = input(prompt)
        if value.isalpha(): # Checks if the input contains only letters
            # Returns the input with spaces removed from the beginning and end
            return value.strip()
        else:
            print('Please enter only letters')

# This function validates the format of the SSN
def checkSSN(ssn):
    # Checks if SSN is not 11 characters long
    if len(ssn) != 11:
        return False
    # Checks if dashes are not in the correct positions
    if ssn[3] != '-' or ssn[6] != '-':
        return False
    # Checks if parts of SSN are not digits
    if not ssn[:3].isdigit() or not ssn[4:6].isdigit() or not ssn[7:].isdigit():
        return False
    # SSN format is correct
    return True

# This function displays employee's initials, email and the last 4 digits of SSN
def displayResult(first_name, last_name, ssn):
    initials = first_name[0].upper() + last_name[0].upper()
    email = first_name.lower()[0] + last_name.lower() + '@gmail.com'
    ssn_4_digits = ssn[-4:]
    print("\nEmployee")
    print("Initials:", initials)
    print("Email address:", email)
    print("Last 4 digits of SSN:", ssn_4_digits)

def main(): 
    # Calls function to display the start of project
    projectStart()

    # Gets the employee's first and last names
    first_name = getStringData("Enter first name: ")
    last_name = getStringData("Enter last name: ")

    # This loop prompts the user to input their SSN
    while True:
        ssn = input("Enter SSN in the format xxx-xx-xxxx: ")
        # Checks if the entered SSN is valid
        if checkSSN(ssn):
            break # Exits the loop if SSN is valid
        else:
            print("Wrong SSN. Enter SSN in the format xxx-xx-xxxx.")

    # Calls the function to display results
    displayResult(first_name, last_name, ssn)

    # Calls function to display the end of project
    projectEnd()
      
# calling the function main()
if __name__ == "__main__": 
    main()



