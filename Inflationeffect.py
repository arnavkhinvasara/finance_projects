#imports
import numpy as np
import datetime
import random

#figuring out date when user uses program
today = datetime.date.today()
today = str(today)
year_wanted = today[0]+today[1]+today[2]+today[3]

#title
print("\nINFLATION RATE--ITEM PRICE--BUYING POWER PREDICTOR")

#avoiding errors by including criteria for user inputs    
while True:
    count2 = 0
    full_nums = "0123456789"
    year_answer = input("\nHow many years in the future do you want to forecast? ")
    for char in year_answer:
        if char in full_nums:
            count2+=1       
    if count2==len(year_answer) and int(year_answer) + int(year_wanted)>int(year_wanted):
        year_wanted_i = int(year_wanted)
        year_answer_i = int(year_answer)
        figure_year = year_wanted_i + year_answer_i
        if figure_year>year_wanted_i:
            break
    print("\nYou should be typing in numbers and wanting to forecast a year in the future.")

#inputing the year wanted into inflation_rate
def Inflation_predictor (x):
    with open("future_years.txt") as fy:
        future = fy.readlines()
        future_years = []
        for element in future:
            future_years.append(element.strip())

    with open("rates.txt") as r:
        rates = r.readlines()
        future_rates = []
        for element in rates:
            future_rates.append(element.strip())

    if str(x) in future_years:
        wanted_index = future_years.index(str(x))
        return float(future_rates[wanted_index])

    with open("future_years.txt", "a") as fy:
        fy.write(str(x)+"\n")

    x = x - 1950
    top = -0.03 * x
    rate_mate = round(8.97 * pow(2.71828, top) + 1, 2)
    rate_mate2 = rate_mate + random.uniform(-0.25, 0.25)
    with open("rates.txt", "a") as r:
        r.write((str(rate_mate2)+"\n"))
    return rate_mate2

#printing rate
print("\nInflation rate in " + str(figure_year) + ": " + str(round(Inflation_predictor(figure_year), 2)) + "%")

#defining function to return the price of a good
def Good_price (x, y):
    count = 0
    criteria = x - y
    all_rates = []
    while count < criteria:
        all_rates.append(round(Inflation_predictor(y), 2))
        y+=1
        count+=1

    all_rates2 = []
    for element in all_rates:
        appender = 1 + element/100
        all_rates2.append(appender)

    return round(10 * np.prod(all_rates2), 2)

#printing price of good
print("\nPrice of $10 item in " + str(figure_year) + ": " + str(round(Good_price(figure_year, year_wanted_i), 2)) + "$")

#defining function to return buying power
def Buy_pow (x, y):
    count = 0
    criteria = x - y
    all_rates = []
    while count < criteria:
        all_rates.append(round(Inflation_predictor(y), 2))
        y+=1
        count+=1

    all_rates2 = []
    for element in all_rates:
        appender = 1 - element/100
        all_rates2.append(appender)

    return round(10 * np.prod(all_rates2), 2)

#printing buying power
print("\n$10 worth in " + str(figure_year) + ": " + str(round(Buy_pow(figure_year, year_wanted_i), 2)) + "$")