# Email Extraction

import re
s = " Knock, knock … Who’s there? … *very long pause* xyz@gmail.com and abc@gmail.com"
t = re.findall('\S+@\S+',s)
print(t)

# Quantifiers

import re

p = re.compile('[0-9]')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

#p = re.compile('[a-z]+')
print(re.findall('[a-z]+',"I went to him at 11 A.M. on 4th July 1886"))
