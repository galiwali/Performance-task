#Budget tracker

def savings(income, costs):
    return income - costs

income= input("What is your monthly income? ")
if income==ValueError:
    print("please enter a valid answer ")
monthly_costs = []
while True:
    rent= int(input("How much is your rent this month? "))
    utillies= int(input("How much are your utillies this month? "))
    grocery= int(input("What is your average grocery costs per month? "))
    break
    
for cost in [rent, utillies, grocery]:
    if cost < 0:
        print("Please enter a valid answer")
        break   
    

#Add costs together
total = rent + utillies + grocery
monthly_costs= rent + utillies + grocery
print(f"Your monthly costs is", {total})

#Subtract costs from income
if total >0:
        def subtract(income, total):
            discretionary_income = income - total
            return discretionary_income
        print("discretionary_income(income - total:)")
else:
    print("Try again")
    if __name__ == "__main__": main()
    

# #Subtract costs from income
# def subtract (income, monthly_costs):
#     discretionary_income = income - monthly_costs
#     discretionary_income
# for total in "discretionary_income":




# Updated_list = {rent, utillies*, miscellaneous**}
# print(Updated_list(rent, utillies, miscellaneous))
