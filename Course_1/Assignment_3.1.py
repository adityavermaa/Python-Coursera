hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
rate = float(rate)
if h <= 40:
    pay = h * rate
else:
    pay = (rate*40) + ((h-40)* (rate*1.5))

print(pay)