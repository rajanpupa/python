# Type is string by default
hrs = input("Enter hours: ")
rate = input("Enter rate: ")

# cast the variables to float and then multiply
pay = float(hrs) * float(rate)

# use comma instead of + sign to print string and float
print("Pay:", pay)