#!/usr/bin/env python3

if __name__ == '__main__':
    print('Temperature converter (C to F)')
    temperatureC = 38.4
    fahrenheit = temperatureC * 1.8 + 32
    print(f'The temperature {temperatureC} C is = {fahrenheit} F.')

    # sep='' removes white spaces after ,
    print(temperatureC, ' C', ' is ', fahrenheit, ' F', sep='')
    print()

    print('      Task 4')
    print('********************')
    scored = 48426
    notOut = 162
    batted = 1014
    matches = 609
    averageBatting = scored // (batted - notOut)
    print(f'The average batting for Geoffrey Boycott is {averageBatting}')
    averageBatting = scored / (batted - notOut)

    # preferred way for rounding
    print(f'The average batting for Geoffrey Boycott is {averageBatting:.2f}')
    print(f'*{averageBatting:12.2f}*')
    print(f'*{averageBatting:<12.2f}*')
    print(f'*{averageBatting:^12.2f}*')

    # this way is changing the number and processing
    print(f'The average batting for Geoffrey Boycott is {round(averageBatting, 2)}')
    print()

    print('      Task 5')
    print('********************')
    group1 = 113
    group2 = 175
    group3 = 12
    fullGroups = 0
    leftOverGroup = 0
    print('Group 1 ')
    print('Number of full groups =', group1 // 24)
    print('Number of students in the left over group =', group1 % 24)
    print('____________________________________________________________')
    print('Group 2 ')
    print('Number of full groups =', group2 // 24)
    print('Number of students in the left over group =', group2 % 24)
    print('____________________________________________________________')
    print('Group 3 ')
    print('Number of full groups =', group3 // 24)
    print('Number of students in the left over group =', group3 % 24)
    print('____________________________________________________________')

    for s in [113, 175, 12]:
        print(f'Students {s:3} Groups: {s // 24:2} Left Over: {s % 24:2}')
    print()
    for s in [113, 175, 12]:
        print(f'Students {s} Groups: {s // 24:2} Left Over: {s % 24:2}')
