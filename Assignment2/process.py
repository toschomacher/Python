import re


def list_process(expect_list):
    print("List process method executing...")
    ucas_list = []
    names = []
    first_names_list = []
    surnames_list = []
    names_initials = []
    temp_string = ""
    for n in expect_list:
        ucas_list.append(n[:8])
        names.append(n[9:])
    for n in names:
        surnames_list.append(n[:n.index(",")])
        first_names_list.append(n[n.index(",")+1:])
    surnames_list = [element.lower() for element in surnames_list]
    for n in surnames_list:
        new_string = re.sub(r'[^a-zA-Z]', '', n)
        surnames_list[surnames_list.index(n)] = new_string
    for element in first_names_list:
        for c in range(0, len(element)):
            if element[c] == ' ':
                temp_string += element[c+1].lower() + '.'
            if c == len(element)-1:
                names_initials.append(temp_string)
                temp_string = ""
    return ucas_list, surnames_list, names_initials
