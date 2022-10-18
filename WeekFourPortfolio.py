#!/usr/bin/env python3

if __name__ == '__main__':

    user_input = int(input('Enter a number: '))
    
    def validation (number):
        if 0 <= number <= 100:
            print('True')
            return True
        else:
            print('False')
            return False
    
    validation(user_input)
    
