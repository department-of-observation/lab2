from statistics import median
import math
finalinput=[]
sorted1=[]
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    finalinput = get_user_input()
    calcaverage(finalinput)
    find_min_max(finalinput)
    sorted1=sort_temperature(finalinput)
    calc_median_temperature(sorted1)


def calcaverage(finalinput):
    average = sum(finalinput) / len(finalinput)
    print(average)
    return average




def display_main_menu():
    print('“Enter some numbers separated by commas (e.g. 5, 67, 32)')


def get_user_input():
    input1 = input('number?')
    split = input1.split(",")
    finalinput=[float(i) for i in split]
    print(finalinput)
    print(type(finalinput))
    return finalinput


def find_min_max(finalinput):
    min1 = min(finalinput)
    max1 = max(finalinput)
    print(max1)
    print(min1)
    return min, max


def sort_temperature(finalinput):
    sorted1 = sorted(finalinput)
    print(sorted1)
    return sorted1


def calc_median_temperature(sorted1):
    median1 = median(sorted1)
    print(median1)
    return median1

if __name__ == '__main__':
    main()
