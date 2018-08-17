def mealCost:
    return float(mealCost)
def tipPercent:
    return int(tipPercent)
def taxPercent:
    return int(taxPercent)

totalCost = mealCost + (mealCost*tipPercent/100) + (mealCost*taxPercent/100)
print(int(totalCost))