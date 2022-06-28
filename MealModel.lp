\* The_Meal_Problem *\
Minimize
Total_Cost_of_Ingredients_per_meal: 0.048 Ingr_ARROZ_BRANCO
 + 0.178 Ingr_FAROFA + 0.0625 Ingr_FEIJÃO + 0.1649 Ingr_FRANGO
 + 0.845 Ingr_MAÇÃ + 0.111 Ingr_ÓLEO_DE_SOJA
Subject To
CalorieRequirement: 35.812 Ingr_ARROZ_BRANCO + 40.6 Ingr_FAROFA
 + 32.903 Ingr_FEIJÃO + 17.3 Ingr_FRANGO + 81.289 Ingr_MAÇÃ
 + 88.4 Ingr_ÓLEO_DE_SOJA >= 700
MaxCarbohydrateRequirement: 7.888 Ingr_ARROZ_BRANCO + 8.03 Ingr_FAROFA
 + 6.122 Ingr_FEIJÃO + 21.567 Ingr_MAÇÃ <= 116
MaxFatRequirement: 0.028 Ingr_ARROZ_BRANCO + 0.91 Ingr_FAROFA
 + 0.126 Ingr_FEIJÃO + 0.451 Ingr_FRANGO + 0.325 Ingr_MAÇÃ
 + 10 Ingr_ÓLEO_DE_SOJA <= 24
MaxProteinRequirement: 0.724 Ingr_ARROZ_BRANCO + 0.21 Ingr_FAROFA
 + 1.998 Ingr_FEIJÃO + 3.091 Ingr_FRANGO + 0.299 Ingr_MAÇÃ <= 27
MinCarbohydrateRequirement: 7.888 Ingr_ARROZ_BRANCO + 8.03 Ingr_FAROFA
 + 6.122 Ingr_FEIJÃO + 21.567 Ingr_MAÇÃ >= 98
MinFatRequirement: 0.028 Ingr_ARROZ_BRANCO + 0.91 Ingr_FAROFA
 + 0.126 Ingr_FEIJÃO + 0.451 Ingr_FRANGO + 0.325 Ingr_MAÇÃ
 + 10 Ingr_ÓLEO_DE_SOJA >= 12
MinProteinRequirement: 0.724 Ingr_ARROZ_BRANCO + 0.21 Ingr_FAROFA
 + 1.998 Ingr_FEIJÃO + 3.091 Ingr_FRANGO + 0.299 Ingr_MAÇÃ >= 18
SaltRequirement: 0.057 Ingr_ARROZ_BRANCO + 575 Ingr_FAROFA + 7.7 Ingr_FRANGO
 + 17.16 Ingr_MAÇÃ <= 800
Bounds
 0 <= Ingr_ARROZ_BRANCO
 1 <= Ingr_FAROFA
 4 <= Ingr_FEIJÃO
 3 <= Ingr_FRANGO
 Ingr_MAÇÃ = 1
 0 <= Ingr_ÓLEO_DE_SOJA
Generals
Ingr_ARROZ_BRANCO
Ingr_FAROFA
Ingr_FEIJÃO
Ingr_FRANGO
Ingr_MAÇÃ
Ingr_ÓLEO_DE_SOJA
End
