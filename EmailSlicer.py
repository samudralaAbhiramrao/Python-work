user_input=str(input("enter your email:"))
email = user_input.split('@')
print("Username : " ,email[0])
print("Domain_name : " ,email[1])





# email = input("Enter Your Email: ").strip()
# username = email[:email.index("@")]
# domain_name = email[email.index("@")+1:]
# format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
# print(format_)