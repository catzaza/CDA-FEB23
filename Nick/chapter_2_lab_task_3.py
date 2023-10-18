# miles per gallon

def calculate_mpg(miles_driven, gallons_used):
    mpg = miles_driven / gallons_used
    return mpg


def main():
    miles_driven = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the number of gallons used: "))

    if miles_driven <= 0 or gallons_used <=0:
        print("Miles driven and gallons used must be positive numbers.")
    else:
        mpg = calculate_mpg(miles_driven, gallons_used)
        print(f"The cars mpg is: {mpg:.2f} miles/gallon")

if __name__ == "__main__":
    main()
