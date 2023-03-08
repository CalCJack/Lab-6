def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    return int(input('Please select an option: '))

def encode(raw_pass:list):
    encoded = ''
    for i in raw_pass:
        i = int(i) + 3
        encoded += str(i)
    print('Your password has been encoded and stored!')
    return encoded

def decode(password:list): # This is a fully functional version of the code for debugging if there is an error
    decoded = ''
    for i in password:
        i = int(i) - 3
        decoded += str(i)
    return decoded

#Initial Conditions for the code to run and name space check so it can be imported
running, password = True, None
if __name__ == '__main__':
    while running:
        option = main()
        if option == 1:
            #User input for the password
            password = encode(list(input('Please enter your password to encode:')))
        elif option == 2:
            #No point in storing the original password as a variable, just make 1 var and use decode
            try:
                print(f'The encoded password is {password}, and the original password is {decode(password)}')
            except:
                print(f"No password to decode!")
        elif option == 3:
            #Simple termination of the while loop
            running = False
        else:
            print('Error! Invalid Input.')