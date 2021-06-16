user_input =str(input("Enter any Word to get its related Acronym"))

sample = user_input.split()
# Basically the split function connverted the input into list  
a=""
# Here for the given list we are considereing the list items first position and comcatenating to a

for i in sample:
	a=a+str(i[0]).upper()
print(a)