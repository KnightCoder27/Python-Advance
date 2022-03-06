# Search

import re
 
s = 'Programmer: A machine that turns coffee into code.'
 
match = re.search('coffee', s)
 
print('Start Index:', match.start())
print('End Index:', match.end())

# Match and Findall


import re
 
p = re.compile('\d')
print(p.findall("There’s no place like 127.0.0.1."))
p = re.compile('\d+')
print(p.findall("There’s no place like 127.0.0.1."))
