print("Welcome to the tip calculator")
total = input("What was the total bill? ")
peoples = input("How many people to split the bill? ")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

total1 = float(total)
peoples1 = float(peoples)
percentage1 = float(percentage)

result = total1/peoples1
if percentage1 == 10:
    result1 = result+result*0.10
    print(round(result1,2))
if percentage1 == 12:
    result2 = result + result * 0.12
    print(round(result2,2))
if percentage1 == 15:
    result3 = result+result*0.15
    print(round(result3,2))
