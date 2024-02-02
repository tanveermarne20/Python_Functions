a=int(input("Enter 1st angle"))
b=int(input("Enter 2nd angle"))
c=int(input("Enter 3rd angle"))

total=a+b+c

if total==180:
    print(f" It is a triangle {total}")
else:
    print(f"Its not a triangle {total}")