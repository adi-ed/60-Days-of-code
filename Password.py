password = input("Enter password: ")

dict_pass = {}

if (len(password) >= 8):
    dict_pass["Length"] = True
else:
    dict_pass["Length"] = False
    
digit = False
for i in password:
    if(i.isdigit()):
        digit = True
dict_pass["Digit"] = digit

upperCase = False
for i in password:
    if(i.isupper()):
        upperCase = True
        
if(all(dict_pass.values())):
    print("Strong Password!")
else:
    print("Weak Password.")