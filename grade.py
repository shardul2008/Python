per = int(input("Enter Percentage"))
if(per>90):
    print("Grade A")
elif per<90 and per > 75:
    print("Grade B")
elif per<75 and per>50:
    print("Grade C")
elif per<50 and per>35:
    print("Grade D")
else:
    print("Fail")