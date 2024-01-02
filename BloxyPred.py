import os
clear = lambda: os.system('cls')
clear()

print("Welcome to Toxin's Very Accurate BloxyBet CF Predictor!")
hAmount = input("Heads: ")
tAmount = input("Tails: ")

if hAmount >tAmount:
    prediction = "Tails"
elif hAmount < tAmount:
    prediction = "Heads"

print(prediction)