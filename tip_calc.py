billAmount = float(input('Total bill amount? '))

while True:
    service = (input("Level of service(good, fair, bad)? "))
if service == "good":
    tip = .20
elif service == "fair":
    tip = .15
elif service == "bad":
    tip = .10
    
total = billAmount + billAmount * tip
print(total)
        




total = billAmount + billAmount * tip
    
print(total)

# while(i < squareSize):
#     j = 0
#     while(j < squareSize):
#         j += 1
#         print("*", end = " ")
#     i += 1
#     print()