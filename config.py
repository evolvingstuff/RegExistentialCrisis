model = 'gpt-4-0125-preview'
max_tokens = 50
outputs = 1

prompt = '''
I want to ask you a series of questions about regex.
I will provide you with a regex pattern and a string.
Your answers should be either 'yes' or 'no'.
If you think the string is matched by the regex pattern, answer 'yes'.
If you think the string is not matched by the regex pattern, answer 'no'.
To reiterate, do NOT say another word other than 'yes' or 'no'.
To clarify, I want to know if the entire string is matched by the regex pattern,
not just a portion of it.
'''

questions_answers = [
    ('given the regex a*b?c+ does the string "abcc" matched by the regex?', 'yes'),
    ('given the regex a*b?c+ does the string "a" matched by the regex?', 'no'),
    ('given the regex a*b?c+ does the string "acc" matched by the regex?', 'yes'),
    ('given the regex a*b?c+ does the string "axc" matched by the regex?', 'no'),
    ('given the regex a*b?c+ does the string "ac" matched by the regex?', 'yes'),
    ('given the regex "a*b?c+" does the string "cx" matched by the regex?', 'no')
]