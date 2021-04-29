# Program that calculates stamp duty
lower_threshold = 500000
middle_threshold = 925000
upper_threshold = 1500000
additionalhome_min_threshold = 0


def capping(price, current_calc):
    if price > middle_threshold and current_calc=='lower':
        new_price = middle_threshold
        return new_price
    elif price <= middle_threshold and current_calc=='lower':
        return price
    elif price > upper_threshold and current_calc=='middle':
        new_price = upper_threshold
        return new_price
    elif price > middle_threshold and price <=upper_threshold and current_calc=='middle':
        return price
        
        
def capping_additional_homes(price, current_calc):
    if price > additionalhome_min_threshold and price < lower_threshold and current_calc=='min':
        return price
    elif price > middle_threshold and current_cal == 'lower':
        new_price = middle_threshold
        return new_price
    elif price <= middle_threshold and current_calc == 'lower':
        return price
    elif price > upper_threshold and current_calc == 'middle':
        new_price = upper_threshold
        return new_price
    elif price > middle_threshold and price <=upper_threshold and current_cal == 'middle':
        return price
        

def calculateSecondHomeLowerThreshold(price):
    percentage = 0.03
    price_compared = capping_additional_homes(price, 'min')
    stamp = price_compared*percentage
    return stamp
    
    
def calculateStampDutyLowerThreshold(price, first_home):
    if first_home:
        percentage = 0.05
        price_compared = capping(price, 'lower')
        stamp = (price_compared - lower_threshold)*percentage
        return stamp
    else:
        percentage = 0.08
        price_compared = capping_additional_homes(price, 'lower')
        stamp = (price_compared - lower_threshold)*percentage
        return stamp
        
        
def calculateStampDutyMiddleThreshold(price, first_home):
    if first_home:
        percentage = 0.10
        price_compared = capping(price, 'middle')
        stamp = (price_compared - middle_threshold)*percentage
        return stamp
    else:
        percentage = 0.13
        price_compared = capping_additional_homes(price, 'middle')
        stamp = (price_compared - middle_threshold)*percentage
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
        

def calculateStampDuty(price,first_home):
    if price <= lower_threshold:
        return 'You will pay £0 in stamp duty. This is your first home and below the threshold'
    
    if price > lower_threshold and price <= middle_threshold:
        stamp = calculateStampDutyLowerThreshold(price,first_home)
        return 'You will pay £{} in stamp duty.'.format(stamp)

    if price > middle_threshold and price <= upper_threshold:
        lower_stamp = calculateStampDutyLowerThreshold(price,first_home)
        middle_stamp = calculateStampDutyMiddleThreshold(price,first_home)
        final_stamp = lower_stamp + middle_stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)

    if price > upper_threshold:
        lower_stamp = calculateStampDutyLowerThreshold(price,first_home)
        middle_stamp = calculateStampDutyMiddleThreshold(price,first_home)
        upper_stamp = calculateStampDutyUpperThreshold(price,first_home)
        final_stamp = lower_stamp + middle_stamp + upper_stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)
        
        
def calculateStampDutyAdditional(price,first_home):
    if price <= lower_threshold:
        min_stamp = calculateSecondHomeLowerThreshold(price)
        return 'You will pay £{} in stamp duty.'.format(min_stamp)
    
    if price > lower_threshold and price <= middle_threshold:
        min_stamp = calculateSecondHomeLowerThreshold(price)
        stamp = calculateStampDutyLowerThreshold(price,first_home)
        final_stamp = min_stamp + stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)

    if price > middle_threshold and price <= upper_threshold:
        min_stamp = calculateSecondHomeLowerThreshold(price)
        lower_stamp = calculateStampDutyLowerThreshold(price,first_home)
        middle_stamp = calculateStampDutyMiddleThreshold(price,first_home)
        final_stamp = min_stamp + lower_stamp + middle_stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)

    if price > upper_threshold:
        min_stamp = calculateSecondHomeLowerThreshold(price)
        lower_stamp = calculateStampDutyLowerThreshold(price,first_home)
        middle_stamp = calculateStampDutyMiddleThreshold(price,first_home)
        upper_stamp = calculateStampDutyUpperThreshold(price,first_home)
        final_stamp = min_stamp + lower_stamp + middle_stamp + upper_stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)



def stampDutyCalculator(first_home, price):
    if first_home:
        return calculateStampDuty(price, first_home)
    else:
        return calculateStampDutyAdditional(price, first_home)


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
