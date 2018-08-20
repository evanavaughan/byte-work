mealCost = float(input("what is the meal cost?"))
tipPercent = int(input("what is the tip percent"))
taxPercent = int(input("what is the tax"))

totalCost = mealCost + (mealCost*tipPercent/100) + (mealCost *taxPercent/100)
print("The total meal cost is", int(totalCost) , "dollars.")