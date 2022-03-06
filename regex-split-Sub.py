#SPLIT

from re import split
 
# '\W+' denotes Non-Alphanumeric Characters

print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))
 
# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs

print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
 
# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only

print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

# SUBSTITUTE

import re

print(re.sub('ub', '~*', 'Subject has Uber booked already'))

print(re.sub('ub', '~*', 'Subject has Uber booked already',count=1,flags=re.IGNORECASE))

print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',flags=re.IGNORECASE))
