# coding challenge 07b.1

import re 

email_fsm = re.compile('[a-z]+@[a-z]+\.[a-z]+')
email_result = email_fsm.search('bsmith@gmail.com')
if email_result:
    print(f'{email_result = }')
