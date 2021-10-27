#! python3

import re

#Function that reads the text file and also replaces the text file.
def edit_file(text_file, cursed_words):
    text_read = open(text_file, 'r')
    text_file_content = text_read.readlines()
    text_read.close()
    text_file_content = edit_file_list(''.join(text_file_content), cursed_words)
    text_write = open(text_file, 'w')
    text_write.write(text_file_content)
    text_write.close()
    return None

#Funtion that edits the list and check each string if any of the cursed word is found.
def edit_file_list(text_file_content, cursed_words):
    swapping = True
    while swapping == True:
        content_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB', re.I)
        content_group = content_regex.search(text_file_content)
        if content_group == None:
            break;
        elif content_group.group().lower() == 'adjective':
            text_file_content = substituter('an adjective', text_file_content, content_regex)
        elif content_group.group().lower() == 'noun':
            text_file_content = substituter('a noun', text_file_content, content_regex)
        elif content_group.group().lower() == 'adverb':
            text_file_content = substituter('an adverb', text_file_content, content_regex)
        elif content_group.group().lower() == 'verb':
            text_file_content = substituter('a verb', text_file_content, content_regex)
    return text_file_content

def substituter(_input, text_file_content, content_regex):
    _input = input(f'Enter {_input}: ')
    content_regex = content_regex.sub(_input, text_file_content, count = 1)
    return content_regex


if __name__ == '__main__':
    text_file = input('Pls input the text file directory: ')
    cursed_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
    edit_file(text_file, cursed_words)