# coding challenge 08b.1 

class IneligibleToVoteError(Exception):
    pass 

age = int(input('What is your age? '))
if age < 18:
    raise IneligibleToVoteError('You need to be 18 years old or older to vote')
