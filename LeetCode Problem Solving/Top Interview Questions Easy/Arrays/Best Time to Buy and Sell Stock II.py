
prices = input([int])

def maxProfit(self, prices: List[int]) -> int:

    startingBalance = 10000
    finalBalance = 10000
    stockOwned = False

    for i in range(len(prices)):
        if (i + 1 < len(prices)):

            if (not stockOwned):
                if (prices[i] < prices[i + 1]):
                    finalBalance -= prices[i]
                    stockOwned += 1

            else:
                if (prices[i] > prices[i + 1]):
                    finalBalance += prices[i]
                    stockOwned -= 1
        else:
            if (stockOwned and prices[i] >= prices[i - 1]):
                finalBalance += prices[i]
                stockOwned -= 1

    return finalBalance - startingBalance

print(maxProfit(prices))

'''
if priceToday < priceTmrw:
    buy stock today if not owned
        or
    hold stock if owned
else (assumes stock is less than or equal to today's price)
    sell stock today if owned
        or
    hold if stock not owned
'''