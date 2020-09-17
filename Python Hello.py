# Brad's greeting:
# print('Hello Professor Berlin')


# -------------------------------------------
# Other ways to print a greeting message:
# 1)
greeting = ['Hello', 'Professor', 'Berlin']

# We can use .join(<a list of strs>) to print our greeting
print(' '.join(greeting))
# > Hello Professor Berlin

# or
print('\n'.join(greeting))
""" out:
Hello
Professor
Berlin
"""


# 2) Using a for loop over the items (key, val)
# from a dictionary combined with string
# justification (left, center)
# Also, f strings - they do the same as '{}'.format()
greet_dict = {
    'first':  'Hello',
    'second': 'Professor',
    'third':  'Berlin'
}

print('\n'.join(f"| {key:>8} | {val:^15} |"
                for key, val in greet_dict.items()))
""" out:
|    first |      Hello      |
|   second |    Professor    |
|    third |     Berlin      |
"""
