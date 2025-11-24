#write a program to get a mail from the user and make sure that  it is email in proper format having @ symbol and .

import re
user_input = input("Please enter propar email:")
def check_mail(user_input):
 result = re.search('^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', user_input)
 if result:
     return "email is valid"
 else:
     return "email isnt valid"

print(check_mail(user_input))