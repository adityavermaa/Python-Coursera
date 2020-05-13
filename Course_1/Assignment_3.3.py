score = input("Enter a score:")
score = float(score)
if score <= 1.0:
    if score >= 0.9:
        Grade = "A"
    elif score >= 0.8:
        Grade = "B"
    elif score >= 0.7:
        Grade = "C"
    elif score >= 0.6:
        Grade = "D"
    else:
        Grade = "F"
else:
    Grade = "Error! out of range!"

print(Grade)