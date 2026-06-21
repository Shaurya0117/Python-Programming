marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 33:
    print("Grade C")
else:
    print("Fail")


"""Single line condition {Ternary operator}"""
final_result = "Pass" if marks >= 33 else "Fail"
print(final_result)