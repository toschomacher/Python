#!/url/bin/env python3

if __name__ == '__main__':
    print('*********** Task 1 ***********')
    name = input('Hello, what is your name? ')

    print(f'Hello, Mr {name}. Good to meet you!\n')

    print('*********** Task 2 ***********')
    temperature_C = float(input('Enter a temperature in Celsius:'))

    print(f'{temperature_C}C is equivalent to ' + str(temperature_C * 1.8 + 32) + 'F.\n')

    print('*********** Task 3 ***********')
    num_of_students = int(input('How many students? '))
    group_size = int(input('Required group size? '))

    print('There will be', num_of_students // group_size,
          ' groups with', num_of_students % group_size, 'students left over.\n')

    print('*********** Task 4 ***********')
    num_of_sweets = int(input('Enter number of sweets: '))
    num_of_children = int(input('Enter number of children: '))

    print('You should give each child', num_of_sweets // num_of_children, 'sweets.')
    print('You will have', num_of_sweets % num_of_children, 'sweets left over.')
