# Program that calculates stamp duty
lower_threshold = 500000
middle_threshold = 925000
upper_threshold = 1500000

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
    in the £500,000 and £925,000 bracket.
    """
    try:
        percentage = 0.05
        price_compared = capping(price, 'lower')
        stamp = (price_compared - lower_threshold)*percentage
        return stamp
    except TypeError:
            print('You did not enter a valid number.')
    except:
        raise ValueError('Number was not in range')


def calculateStampDutyMiddleThreshold(price: float) -> float:
    """
    Function that calculates the amount of tax duty to be paid
    in the £925,000 to £1,500,000 bracket.
    """
    try:
        percentage = 0.10
        price_compared = capping(price, 'middle')
        stamp = (price_compared - middle_threshold)*percentage
        return stamp
    except TypeError:
            print('You did not enter a valid number.')
    except:
        raise ValueError('Number was not in range')


def calculateStampDutyUpperThreshold(price: float) -> float:
    """
    Function that calculates the amount of tax duty to be paid
    above the £1,500,000 bracket.
    """
    try:
        percentage = 0.12
        stamp = (price - upper_threshold)*percentage
        return stamp
    except TypeError:
            print('You did not enter a valid number.')
    except:
        raise ValueError('Number was not in range')


def calculateStampDuty(price: float) -> str:
    """
    Function that calculates the amount of tax duty to be paid
    for a property.
    """
    try:
        if price <= lower_threshold and price > 0:
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
    except TypeError:
            print('You did not enter a valid number.')
    except:
        raise ValueError('Number is not in range')
    

class TaxBracket:
    def __init__(self, percentage, lower_bound, upper_bound):
        self.percentage = percentage # 0
        self.lower_bound = lower_bound # 0
        self.upper_bound = upper_bound # 500 001

    def tax_due(self, price):
        stamp_duty = -1
        if price <= self.lower_bound:
            stamp_duty = 0
        if price > self.upper_bound:
            stamp_duty = (self.upper_bound - self.lower_bound)*self.percentage
        if price > self.lower_bound and price <= self.upper_bound:
            stamp_duty = (price - self.lower_bound)*self.percentage
        return stamp_duty

bracket1 = TaxBracket(0.12, 500000, 750000)
print(bracket1.tax_due(0))
# 0
print(bracket1.tax_due(250000))
# 0
print(bracket1.tax_due(750000))
# 0


if __name__ == "__main__":
    price = input("What's the price of the house you're looking to buy?\n")
    print(calculateStampDuty(float(price)))

