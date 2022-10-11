#!/url/bin/env python3

from statistics import mean as avg

if __name__ == '__main__':
    # Improved version
    NUMBER_OF_MARKS = 3

    marks = []

    while True:
        try:
            mark = int(input(f'Enter next mark: '))
            if 0 <= mark <= 100:
                marks.append(mark)
            else:
                print('Error: Value is out of range.')
        except ValueError:
            print('Error: Value is not and integer.')
        if len(marks) == NUMBER_OF_MARKS:
            break

    max_mark = max(marks)
    min_mark = min(marks)
    avg_mark = avg(marks)

    print(f'Highest Mark: {max_mark}')
    print(f'Lowest  Mark: {min_mark}')
    print(f'Average Mark: {avg_mark:.2f}')

    # TODO comment

    # Old version of this program
    mark_1 = int(input('Enter mark #1: '))
    mark_2 = int(input('Enter mark #2: '))
    mark_3 = int(input('Enter mark #3: '))
    mark_4 = int(input('Enter mark #4: '))
    mark_5 = int(input('Enter mark #5: '))

    max_mark = max(mark_1, mark_2, mark_3, mark_4, mark_5)
    min_mark = min(mark_1, mark_2, mark_3, mark_4, mark_5)
    avg_mark = avg([mark_1, mark_2, mark_3, mark_4, mark_5])

    print(f'Highest Mark: {max_mark}')
    print(f'Lowest  Mark: {min_mark}')
    print(f'Average Mark: {avg_mark:.2f}')

    # s.split('::')           how to split a string
    # ['112', '134']
    # int(s.split('::')[1])
