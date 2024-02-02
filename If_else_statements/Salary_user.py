salary=int(input("Enter your salary"))

if 20000<=salary <=30000:
    print("Software Engineer")
elif    31000<=salary <=45000:
    print("Senior software engineer")
elif salary>45000:
    print("Team Leader")

else:
    print("Invalid input")