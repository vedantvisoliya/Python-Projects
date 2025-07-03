# python email slicer

email_address = input("Enter your email: ")
index = email_address.find("@")

username = email_address[:index]
domain = email_address[index+1:]

print(f"Your username is {username},\n& your domain is {domain}")