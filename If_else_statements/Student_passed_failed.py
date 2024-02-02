chem=float(input("Enter chemistry marks"))
geo=float(input("Enter geography marks"))
math=float(input("Enter math marks"))

if chem>=40 and geo>=40 and math>=40:
    print("Student passed")

elif chem<40 and geo<40 and math<40:
    print("Student failed")
else:
    if geo<40:
        print("Failed in geo")
    if math<40:
        print("Failed in math")
    if chem<40:
        print("Failed in chem")

total_marks=chem+geo+math
percentage=(total_marks/300)*100
print(percentage);