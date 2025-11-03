# 07a - Regular Expressions (Regex)

'''
..b* - any 2 chars, then 0 or more 'b's
1|0  - either a 0 or a 1 (a binary digit)
(1|0)* - 0 or more binary digits
[01] - a binary digit
[01]+ - 1 or more binary digits
[^01] - any character except for 0 or 1
(\d\d\d)? - either 3 digits or 0 digits (? - optional)
[a-z0-9] - either a lowercase letter or a digit
[0-9+-] - a digit or a + or a -
\. - one dot
.{5} - any 5 characters
[0-9]{3,6} - between 3 and 6 digits
[0-9]{3,} - 3 or more digits
'''

import re 

'\d\d\d \d\d\d \d\d\d\d'
# phone_num_fsm = re.compile('(\d{3} )?\d{3} \d{4}') # match anywhere in the string
phone_num_fsm = re.compile('^(\d{3} )?\d{3} \d{4}$') # match entire string
phone_num_result = phone_num_fsm.search('905721 8668')
print(f'{phone_num_result = }')

if phone_num_result:
    print(f'{phone_num_result.start() = }')
    print(f'{phone_num_result.end() = }')
    print(f'{phone_num_result.group() = }')

