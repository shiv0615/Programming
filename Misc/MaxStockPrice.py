import numpy as np
from collections import OrderedDict
import copy

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    else:
        low = 99999  # represent minimum price so far
        profitmax = 0
        for price in prices:
            if price > low:
                if price - low > profitmax:
                    profitmax = price - low
            elif price < low:
                low = price

        return profitmax

def main(prices):
    delta = maxProfit(prices)
    print(f'Delta = {delta}')

if __name__ =='__main__':
    prices = [7,1,5,3,6,4]
    main(prices)