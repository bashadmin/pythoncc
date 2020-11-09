import re

text = re.sub('(<INSD[^[_\n]*_)|(</[^\n]*)|<([^\n&^>]*>\n)|(<INSD{1})',"", open('INSD.xml').read()).replace('>',":")

def remove_left_spaces(string):
    string_list = string.split("\n")
    temp_list = [i.lstrip() for i in string_list]
    joined_list = "\n".join(temp_list)
    return joined_list

#lst_text = text.split()
#clean_text = "\n".join(lst_text)

text = remove_left_spaces(text)

with open('INSD.txt', 'w') as file:
    file.write(text)
