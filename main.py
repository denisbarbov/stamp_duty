# Program that calculates stamp duty
lower_threshold = 500000
middle_threshold = 925000
upper_threshold = 1500000

def capping(price, current_calc):
    if price > middle_threshold and current_calc=='lower':
        new_price = middle_threshold
        return new_price
    elif price <= middle_threshold and current_calc=='lower':
        return price



def calculateStampDutyLowerThreshold(price, first_home):
    if first_home:
        percentage = 0.05
        price_compared = capping(price, 'lower')
        stamp = (price_compared - lower_threshold)*percentage
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
        return 'You will pay £0 in stamp duty. This is your first home and below the threshold'
    
    if price > lower_threshold and price <= middle_threshold:
        stamp = calculateStampDutyLowerThreshold(price, first_home)
        return 'You will pay £{} in stamp duty.'.format(stamp)

    if price > middle_threshold and price <= upper_threshold:
        lower_stamp = calculateStampDutyLowerThreshold(price, first_home)
        print(lower_stamp)
        middle_stamp = calculateStampDutyMiddleThreshold(price, first_home)
        print(middle_stamp)
        final_stamp = lower_stamp + middle_stamp
        print(final_stamp)
        return 'You will pay £{} in stamp duty.'.format(final_stamp)

    if price > upper_threshold:
        lower_stamp = calculateStampDutyLowerThreshold(price, first_home) 
        middle_stamp = calculateStampDutyMiddleThreshold(price, first_home)
        upper_stamp = calculateStampDutyUpperThreshold(price, first_home)
        final_stamp = lower_stamp + middle_stamp + upper_stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)

def calculateSecondHomeLowerThreshold(price):
    percentage = 0.03
    stamp = price*percentage
    return 'You will pay £{} in stamp duty'.format(stamp)

def stampDutyCalculator(first_home, price):
    if not first_home and price <= lower_threshold:
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
