# Program that calculates stamp duty
lower_threshold = 500000
middle_threshold = 925000
upper_threshold = 1500000

def calculateStampDutyLowerThreshold(price, first_home):
    if first_home:
        percentage = 0.05
        stamp = (price - lower_threshold)*percentage
        return stamp
    else:
        percentage = 0.08
        stamp = (price - lower_threshold)*percentage
        return stamp
        
def calculateStampDutyMiddleThreshold(price, first_home):
    if first_home:
        percentage = 0.10
        stamp = (price - middle_threshold)*percentage
        return stamp
    else:
        percentage = 0.13
        stamp = (price - middle_threshold)*percentage
        return stamp

def calculateStampDutyUpperThreshold(price, first_home):
    if first_home:
        percentage = 0.12
        stamp = (price - upper_threshold)*percentage
        return stamp
    else:
        percentage = 0.15
        stamp = (price - upper_threshold)*percentage
        return stamp

def calculateStampDuty(price, first_home):
    if price <= lower_threshold:
        stamp = calculateStampDutyLowerThreshold(price, first_home)
        return 'You will pay £{} in stamp duty.'.format(stamp)

    if price > middle_threshold and price <= upper_threshold:
        lower_stamp = calculateStampDutyLowerThreshold(price, first_home) 
        middle_stamp = calculateStampDutyMiddleThreshold(price, first_home)
        final_stamp = lower_threshold + middle_threshold
        return 'You will pay £{} in stamp duty.'.format(final_stamp)

    if price > upper_threshold:
        lower_stamp = calculateStampDutyLowerThreshold(price, first_home) 
        middle_stamp = calculateStampDutyMiddleThreshold(price, first_home)
        upper_stamp = calculateStampDutyUpperThreshold(price, first_home)
        final_stamp = lower_threshold + middle_threshold + upper_stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)

def calculateSecondHomeLowerThreshold(price):
    percentage = 0.03
    stamp = price*percentage
    return 'You will pay £{} in stamp duty'.format(stamp)

def stampDutyCalculator(first_home, price):
    if first_home and price <= lower_threshold:
        return '0%. This is your first home and it is within the threshold.'
    elif not first_home and price <= lower_threshold:
        return calculateSecondHomeLowerThreshold(price)
    else:
        return calculateStampDuty(price, first_home)

if __name__ == "__main__":
    print("Let's calculate your stamp duty")
    print("Is this your first home?")
    first_home = input("Yes or No\n")
    if first_home == "Yes":
        first_home_bool = True
    elif first_home == "No":
        first_home_bool = False
    price = input("What's the price of the house you're looking to buy?\n")
    print(stampDutyCalculator(first_home_bool, int(price)))
