#challenge day task

#get input from user
while True:
    firstname = input("What is your first name? ")
    if firstname.isalpha() == False:
        break
    else:
        lastname = input("What is your last name? ")
        age = int(input ("What is your age? "))

        #generate email adresss
        email = firstname[0]+lastname

        #generate year
        studentnumber = "102937443"
        number = studentnumber[-3]
        print (number)
        year = age + int(number)
        year = 2020 - year
        x = str(year)

        #format last name for pw and print email/pw
        pwlastname = lastname.upper()
        print (email.lower() + "@Huawow.io|" + firstname.lower() + pwlastname[0] + "_" + x)