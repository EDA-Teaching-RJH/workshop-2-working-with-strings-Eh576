def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")



def pounds_to_float(d):
    pounds_to_float = d.replace ("£", "")
    outputF = float(pounds_to_float)
    return outputF

def percent_to_float(p):
    percent_to_float = p.replace ("%", "")
    outputP = float(percent_to_float)
    return outputP / 100

main()
