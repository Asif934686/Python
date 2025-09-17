name = input("Enter customer name: ")
mobile = input("Enter mobile number: ")
cost = float(input("Enter cost of purchase: "))
if cost >= 5000:
    discount = cost * 0.10   # 10%
elif cost >= 2000:
    discount = cost * 0.05   # 5%
else:
    discount = 0
total = cost - discount
print("\nCustomer Name:", name)
print("Mobile Number:", mobile)
print("Purchase Cost:", cost)
print("Discount:", discount)
print("Total Amount to be Paid:", total)
