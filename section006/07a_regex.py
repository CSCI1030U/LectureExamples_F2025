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

price_fsm = re.compile('(\$\d+(\.\d\d)?)')
amazon_review = '''
I bought this product for $109.99, but then I found it elsewhere
for $100 and I wish I hadn't shopped at Amazon because it was 
more expensive and I would have saved $9.99.
'''
print(f'{price_fsm.findall(amazon_review) = }')

print(f'{re.sub(price_fsm, '...', amazon_review) = }')

print(f'{re.split(price_fsm, amazon_review) = }')

# coding exercise 07a.1

'[01]{8,16}' # common mistake

#binary_fsm = re.compile('([01]{8})?([01]{8})')
binary_fsm = re.compile('([01]{16})|([01]{8})')
print(f'{binary_fsm.match("00001111") = }')
print(f'{binary_fsm.match("0000111100001111") = }')

