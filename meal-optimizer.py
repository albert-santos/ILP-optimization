"""
An optimization model to obtain the optimal amount of food in a meal.

Authors: Albert Einstein Coutinho dos Santos 
Federal University of Pará,  2022
"""

# Import PuLP modeler functions
from pulp import *  

# Creates a list of the Ingredients
Ingredients = ["FRANGO", "ARROZ_BRANCO", "FEIJÃO", "FAROFA", "MAÇÃ", "ÓLEO_DE_SOJA"]


# A dictionary of costs per 10 g serving of each of the ingredients is created
costs = {
    "FRANGO": 0.1649,
    "ARROZ_BRANCO": 0.048,
    "FEIJÃO": 0.0625,
    "FAROFA": 0.178,
    "MAÇÃ": 0.845,
    "ÓLEO_DE_SOJA": 0.111,
}

# A dictionary of the caloria amount of each ingredient in a 10 g serving is created
calorieAmount = {
    "FRANGO": 17.3,
    "ARROZ_BRANCO": 35.812,
    "FEIJÃO": 32.903,
    "FAROFA": 40.6,
    "MAÇÃ": 81.289,
    "ÓLEO_DE_SOJA": 88.4,
}

# A dictionary of the protein amount of each ingredient in a 10 g serving is created
proteinAmount = {
    "FRANGO": 3.091,
    "ARROZ_BRANCO": 0.724,
    "FEIJÃO": 1.998,
    "FAROFA": 0.21,
    "MAÇÃ": 0.299,
    "ÓLEO_DE_SOJA": 0,
}

# A dictionary of the fat amount of each ingredient in a 10 g serving is created
fatAmount = {
    "FRANGO": 0.451,
    "ARROZ_BRANCO": 0.028,
    "FEIJÃO": 0.126,
    "FAROFA": 0.91,
    "MAÇÃ": 0.325,
    "ÓLEO_DE_SOJA": 10,
}

# A dictionary of the carbohydrate amount of each ingredient in a 10 g serving is created
carbohydrateAmount = {
    "FRANGO": 0,
    "ARROZ_BRANCO": 7.888,
    "FEIJÃO": 6.122,
    "FAROFA": 8.03,
    "MAÇÃ": 21.567,
    "ÓLEO_DE_SOJA": 0,
}

# A dictionary of the salt (in mg) amount of each ingredient in a 10 g serving is created
saltAmount = {
    "FRANGO": 7.7,
    "ARROZ_BRANCO": 0.057,
    "FEIJÃO": 0,
    "FAROFA": 575,
    "MAÇÃ": 17.16,
    "ÓLEO_DE_SOJA": 0,
}


# Create the 'prob' variable to contain the problem data
problem = LpProblem("The Meal Problem", LpMinimize)

# A dictionary called 'ingredient_vars' is created to contain the referenced Variables
ingredient_vars = LpVariable.dicts("Ingr", Ingredients, lowBound=0, cat=LpInteger)

# The meal should have at least one serving of these ingredients.
apple = LpVariable("Ingr_MAÇÃ", lowBound=1, upBound=1,cat=LpInteger)
ingredient_vars["MAÇÃ"] = apple
frango = LpVariable("Ingr_FRANGO", lowBound=3,cat=LpInteger)
ingredient_vars["FRANGO"] = frango
feijao = LpVariable("Ingr_FEIJÃO", lowBound=4,cat=LpInteger)
ingredient_vars["FEIJÃO"] = feijao
arroz = LpVariable("Ingr_ARROZ", lowBound=1,cat=LpInteger)
ingredient_vars["ARROZ"] = arroz
farofa = LpVariable("Ingr_FAROFA", lowBound=1,cat=LpInteger)
ingredient_vars["FAROFA"] = farofa

# The objective function is added to 'problem' first
problem += (
    lpSum([costs[i] * ingredient_vars[i] for i in Ingredients]),
    "Total Cost of Ingredients per meal",
)

# The constraints are added to 'problem'
# Restrictions are established according 
# to the PNAE reference values for people aged between 19 and 30.

# Calories for a single meal (30% of daily needs)
problem += (
    lpSum([calorieAmount[i] * ingredient_vars[i] for i in Ingredients]) >= 700,
    "CalorieRequirement",
)


problem += (
    lpSum([proteinAmount[i] * ingredient_vars[i] for i in Ingredients]) >= 18.0,
    "MinProteinRequirement",
)

problem += (
    lpSum([proteinAmount[i] * ingredient_vars[i] for i in Ingredients]) <= 27.0,
    "MaxProteinRequirement",
)

problem += (
    lpSum([fatAmount[i] * ingredient_vars[i] for i in Ingredients]) >= 12.0,
    "MinFatRequirement",
)

problem += (
    lpSum([fatAmount[i] * ingredient_vars[i] for i in Ingredients]) <= 24.0,
    "MaxFatRequirement",
)

problem += (
    lpSum([carbohydrateAmount[i] * ingredient_vars[i] for i in Ingredients]) >= 98.0,
    "MinCarbohydrateRequirement",
)

problem += (
    lpSum([carbohydrateAmount[i] * ingredient_vars[i] for i in Ingredients]) <= 116.0,
    "MaxCarbohydrateRequirement",
)

problem += (
    lpSum([saltAmount[i] * ingredient_vars[i] for i in Ingredients]) <= 800,
    "SaltRequirement",
)

# The problem data is written to an .lp file
problem.writeLP("MealModel.lp")

# The problem is solved using PuLP's choice of Solver
problem.solve()


print("\n")
print("-*" * 50)
print("RESULTADOS".center(100))

# The status of the solution is printed to the screen
print("Status: ", LpStatus[problem.status])

# Each of the variables is printed with it's resolved optimum value
for v in problem.variables():
        print(v.name, " = ", v.varValue)

print("\nTOTAL VALUES: ")
# The optimised objective function value is printed to the screen
print(f"Total Cost per meal = R${value(problem.objective):.2f}")

# Total calories
total_calories = value(lpSum([calorieAmount[i] * ingredient_vars[i] for i in Ingredients]))
print(f'Total calories: {total_calories:.2f} Kcal')

# Total protein
total_protein = value(lpSum([proteinAmount[i] * ingredient_vars[i] for i in Ingredients]))
print(f'Total protein: {total_protein:.2f}g')

# Total fat
total_fat = value(lpSum([fatAmount[i] * ingredient_vars[i] for i in Ingredients]))
print(f'Total fat: {total_fat:.2f}g')

# Total carbohydrate
total_carbohydrate = value(lpSum([carbohydrateAmount[i] * ingredient_vars[i] for i in Ingredients]))
print(f'Total carbohydrate: {total_carbohydrate:.2f}g')

# Total salt
total_salt = value(lpSum([saltAmount[i] * ingredient_vars[i] for i in Ingredients]))
print(f'Total salt: {total_salt:.2f}mg')

