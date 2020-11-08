principal = 1000
monthly_addition = 0

duration = 1 # In Years.
daily_interest = 1
monthly_interest = 0
interest = 0
contributed = 0
total_profit = 0
# Daily Compound
if daily_interest != 0:
    print(f"\t : {int(principal)}EUR + {int(interest)}EUR interest, + {int((monthly_addition/30))}\n")
    for i in range((duration*365)):
        interest = (principal*0.97) * (daily_interest/100)
        total_profit += interest
        if i % 30:
            principal += (monthly_addition/30) + interest
            contributed += monthly_addition
        else:
            principal += interest
        print(f"\t {i+1} : {int(principal)}EUR + {int(interest)}EUR interest, + {int((monthly_addition/30))}, Total contributed : {contributed} \t -- Total profit = {int(total_profit)}EUR")
else:
# Monthly Compound
    print(f"\t : {int(principal)}EUR + {int(interest)}EUR interest, + {int((monthly_addition))}\n")
    for i in range((duration*12)):
        interest = (principal*0.97) * (monthly_interest/100)
        total_profit += interest
        principal += (monthly_addition/30) + interest
        contributed += monthly_addition
        print(f"\t {i+1} : \t{int(principal)}EUR + {int(interest)}EUR interest, + {int((monthly_addition))}, \tTotal contributed : {contributed} \t -- Total profit = {int(total_profit)}EUR")