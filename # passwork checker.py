# passwork checker
pw = input ('enter password ')
if len(pw) >= 8 and pw.isdigit() == False and pw.isupper() == False and pw.islower() == False:
    print ('password is valid')
else:
    print ('password is invalid')