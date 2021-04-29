# Program that calculates stamp duty
lower_threshold = 500000
middle_threshold = 925000
upper_threshold = 1500000
#additionalhome_min_threshold = 0

def capping(price: float, current_calc: str) -> float:
    """
       Function that caps the price at the correct levels.
    """
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


def calculateStampDutyLowerThreshold(price: float) -> float:
    """
    Function that calculates the amount of tax duty to be paid
    for properties less than £500,000.
    """
    percentage = 0.05
    price_compared = capping(price, 'lower')
    stamp = (price_compared - lower_threshold)*percentage
    return stamp


def calculateStampDutyMiddleThreshold(price: float) -> float:
    """
    Function that calculates the amount of tax duty to be paid
    in the £500,000 and £925,000 bracket.
    """
    percentage = 0.10
    price_compared = capping(price, 'middle')
    stamp = (price_compared - middle_threshold)*percentage
    return stamp


def calculateStampDutyUpperThreshold(price: float) -> float:
    """
    Function that calculates the amount of tax duty to be paid
    in the £925,000 to £1,500,000 bracket.
    """
    percentage = 0.12
    stamp = (price - upper_threshold)*percentage
    return stamp


def calculateStampDuty(price: float) -> str:
    """
    Function that calculates the amount of tax duty to be paid
    for a property.
    """
    if price <= lower_threshold:
        return 'You will pay no stamp duty.'

    if price > lower_threshold and price <= middle_threshold:
        stamp = calculateStampDutyLowerThreshold(price)
        return 'You will pay £{} in stamp duty.'.format(stamp)

    if price > middle_threshold and price <= upper_threshold:
        lower_stamp = calculateStampDutyLowerThreshold(price)
        middle_stamp = calculateStampDutyMiddleThreshold(price)
        final_stamp = lower_stamp + middle_stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)

    if price > upper_threshold:
        lower_stamp = calculateStampDutyLowerThreshold(price)
        middle_stamp = calculateStampDutyMiddleThreshold(price)
        upper_stamp = calculateStampDutyUpperThreshold(price)
        final_stamp = lower_stamp + middle_stamp + upper_stamp
        return 'You will pay £{} in stamp duty.'.format(final_stamp)
    

if __name__ == "__main__":
    price = input("What's the price of the house you're looking to buy?\n")
    print(calculateStampDuty(float(price)))

