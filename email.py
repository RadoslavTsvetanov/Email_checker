import re
email = "h@gmail.com"
check = re.compile(r'\w((\w)+|(-)+|(_)+|())@(\w)+.com')
i = email.index("@")
if(check.search(email) != None) and (i > 3):
    result = check.search(email)
    print(result.group())
else:
    print("not valid email")
