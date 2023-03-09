#Caleb Jackson
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
        i = int(i)
        if i < 7:
            i = int(i) + 3
        elif i == 7:
            i = 0
        elif i == 8:
            i = 1
        else:
            i = 2
        encoded += str(i)
    print('Your password has been encoded and stored!')
    return encoded

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
    while running:
        option = main()
        if option == 1:
            password = encode((input('Please enter your password to encode:')))
        elif option == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}')
        elif option == 3:
            running = False
        else:
            print('Error! Invalid Input.')