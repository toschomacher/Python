#!/usr/bin/env python3

if __name__ == '__main__':
    print('\n*********** Task 1 ***********')
    user_input = int(input('Enter a number: '))
    
    def validation (number):
        if 0 <= number <= 100:
            print('True')
            return True
        else:
            print('False')
            return False
    
    validation(user_input)
    
    print('\n*********** Task 2 ***********')
    message = "Hello. This is just some RANdom text. OK?"


    def validation(text):
        upper = 0
        lower = 0
        for i in text:
            if i.isupper():
                upper = upper + 1
            if i.islower():
                lower = lower + 1
        return upper, lower


    print("We have", validation(message)[0], "number of upper case letters")
    print("and", validation(message)[1], "number of small letters in this text.")

    print('\n*********** Task 3 ***********')
    name = input("Enter your name: ")
    if not name:
        print('Hello stranger')
    else:
        print('Hi ' + name[0].upper() + name[1:].lower() + '.')

    print('\n*********** Task 4 ***********')
    text = input("Enter some text: ")


    def last_character(from_user):
        if len(from_user) > 1:
            from_user = from_user[:-1]
            print(from_user)
        else:
            print(from_user)


    last_character(text)

    print('\n*********** Task 5 ***********')
    temperature_c = float(input("Enter temperature in degrees C: "))


    def temp_conv_to_f(centigrade):
        fahrenheit = centigrade * 1.8 + 32
        return fahrenheit


    def temp_conv_to_c(fahrenheit):
        centigrade = (fahrenheit - 32) * 0.5556
        return centigrade


    print(f"Your temperature in C is equivalent to {temp_conv_to_f(temperature_c):.2f} F")
    print(f"Converting it back to C is {temp_conv_to_c(temp_conv_to_f(temperature_c)):.2f}.")

    print('\n*********** Task 6 ***********')
    text = input("Enter a temperature in Celsius in the format 21C :")

    def temp_conv(info):
        temp_c = int(info[:-1])
        temp_f = temp_c * 1.8 + 32
        return str(temp_f) + "F"
    print("Your temperature converted in Fahrenheit: ", temp_conv(text))
    
