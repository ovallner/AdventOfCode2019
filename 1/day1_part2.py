# Author: Oscar Vallner
import math

def calc_fuel(weight):
    new_weight = math.floor(weight / 3) - 2
    if new_weight > 0:
        return new_weight + calc_fuel(new_weight)
    else:
        return 0

def main():
    total_fuel = 0
    with open("input.txt") as input:
        for weight in input:
            fuel = calc_fuel(int(weight))
            total_fuel += fuel
            print(f"Weight {int(weight)} requires {fuel} fuel")
    
    print(f"Total Fuel requirement: {total_fuel}")
    

if __name__=="__main__":main()