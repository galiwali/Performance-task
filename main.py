#Budget tracker

def savings(income, costs):
    return income - costs

income= input("What is your monthly income? ")
if income==ValueError:
    print("please enter a valid answer ")
monthly_costs = []
while True:
    rent= int(input("How much is your rent this month? "))
    utilities= int(input("How much are your utilities this month? "))
    grocery= int(input("What is your average grocery costs per month? "))
    break
    
for cost in [rent, utilities, grocery]:
    if cost < 0:
        print("Please enter a valid answer")
    again= input("Enter again(press q to quit, enter to repeat)")
    if again == "q":

        break
    else:
        continue
        
    

#Add costs together
total = rent + utilities + grocery
monthly_costs= rent + utilities + grocery
print(f"Your monthly costs is", total)

#Subtract costs from income
balance_remaining= int(income)-total
print(f"You have a remaining balence of",balance_remaining,"dollars this month!")




# Updated_list = {rent, utillies*, miscellaneous**}
# print(Updated_list(rent, utillies, miscellaneous))
