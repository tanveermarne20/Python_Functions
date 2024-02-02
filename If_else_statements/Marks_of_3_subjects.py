math=float(input("Enter marks of math"))
geo=float(input("Enter marks of geo"))
chem=float(input("Enter marks of chem"))

total_marks=math+geo+chem
percentage=(total_marks/300)*100

if percentage<60:
    print(f"Hard luck ,next time    {percentage}")
elif percentage>=60:
    print(f"passed {percentage}")