import re
text = "Python123"

result = re.findall(r"\d",text)
print(result)
import re
text ="I am learning Python"

result = re.search("Python",text)

if result:
    print("Pattern Found")
else:
    print("Pattern NOt Found")

import re
text = "My roll number is 123"
result= re.search(r"\d+",text)

if result:
    print("Found:",result.group())

import re

text = "Hello Python"   

print(re.match("python",text))
print(re.search("Python",text))



