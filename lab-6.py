#Caleb Jackson
def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    return int(input('Please select an option: '))

def encode(raw_pass:list):
    encode = ''
    for i in raw_pass:
        if int(i) > 6:
            # taking into account the size of the number we can filter out ones that take a little extra to change
            i = ((int(i) + 3) - 10)
        else:
            i = int(i) + 3
            # reassigining it to i just for simplicity sake
        encode += str(i)
    print('Your password has been encoded and stored!')
    return encode
    # returning the encoded value back to the user

def decode(password:list):

    #Cycles through each digit of the encoded password and reduces the value by 3 to decode it.
    original = ""
    for i in password:
        if int(i) > 2:
            original = original + str(int(i) - 3)

        #The following if statements are used so that the digits wrap back around instead of going into negative numbers
        elif i == "2":
            original = original + "9"
        elif i == "1":
            original = original + "8"
        else:
            original = original + "7"

    return original

running, password = True, None
if __name__ == '__main__':
    #Starting the loop that will run for the duration of the program
    while running:
        option = main()
        # User chooses to encode it and it is stored
        if option == 1:
            password = encode((input('Please enter your password to encode:')))
        # User chooses to decode and it is attempted, if it fails the dialogue bounces back
        elif option == 2:
            try:
                print(f'The encoded password is {password}, and the original password is {decode(password)}')
            except:
                print(f"No password to decode!")
        # Using try and except lets the program avoid breaking
        elif option == 3:
            running = False
        # A condition to help the code from being broken by a wrong input
        else:
            print('Error! Invalid Input.')