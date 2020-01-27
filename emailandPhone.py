#! /usr/bin/env python3
import re, pyperclip
# A program that scans a document for emails and phone numbers, then compiles a list.

phoneRegex = re.compile(r'''
(
(\d{3}|\(\d{3}\))?      # area code 3 first digits
(\s|-|\.)?          # separators: a hyphen
(\d{3})         # first three digits of the number
(\s|-|\.)           # separator A hyphen
(\d{4})         # last four digits of the number
(\s*(ext|x|ext.)\s*(\d{2,5}))? # Extension number?
) 
''', re.VERBOSE)

#create a regex for email
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+   # username
@                   # At symbol
[a-zA-Z0-9.-]+      # Domain name
(\.[a-zA-Z]{2,4})   # .dotsomething
)''', re.VERBOSE)

#Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No Phone numbers or Email addresses found.')