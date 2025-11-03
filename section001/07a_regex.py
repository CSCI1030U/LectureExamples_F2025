# 07a - Regular Expressions (Regex)

# .        - any character
# ..       - any character, then any character
# a        - an 'a'
# ab       - an 'a' and then a 'b'
# (a|b)    - a or b
# (a|b|c)
# (a|b*)   - 1 'a' or (zero or more 'b's)
# (a+|b)   - (1 or more 'a's) or 1 'b'
# (a?|b)   - (0 or 1 'a') or 1 'b'
# (a|b|c|d|...|y|z) - any 1 lowercase letter
# [a-z]             - same
# [abcdefghijklmnopqrstuvwxyz] - same
# [^0-9]            - any 1 character except digits
# [^abc]            - any 1 character except a, b, or c
# [a-z0-9]          - any lowercase or digit char
# [a-z0-9+-]        - any lowercase or digit or + or -
# \d{3}             - any three digits
# \d{5,10}          - any 5 through 10 digit string
import re 

# ^ - represents the start of the string
# $ - represents the end of the string
# variable_fsm = re.compile('[a-zA-Z_][a-zA-Z0-9_]*') # string match within
variable_fsm = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$') # full string match
variable_match = variable_fsm.match('max = 8')
print(f'{variable_match = }')
if variable_match:
    print(f'{variable_match.start() = }')
    print(f'{variable_match.end() = }')
    print(f'{variable_match.group() = }')

sentence = 'I ran so \tfar away  \nso far away'
print(f'{sentence.split(' ')}')
print(f'{re.split("\s+", sentence) = }')

phone_fsm = re.compile('^(1-)?[0-9]{3}-[0-9]{3}-[0-9]{4}$')
phone_match = phone_fsm.match('1-905-721-8668')
if phone_match:
	print('Start:     ', phone_match.start())
	print('End:       ', phone_match.end())
	print('Text:      ', phone_match.group())
else:
    print('No match for phone number')

# coding exercise 07b.1
# binary_fsm = re.compile('^[01]{16}|[01]{8}$')
binary_fsm = re.compile('^[01]{8}([01]{8})?$')
binary_match = binary_fsm.search('0000111100001111')
if binary_match:
	print('Text:      ', binary_match.group())
else:
    print('No match for binary number')

