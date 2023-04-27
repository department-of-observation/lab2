from statistics import median

finalinput = 0
min = 0
max = 0


def calcaverage():
    average = sum(finalinput) / len(finalinput)
    print(average)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    get_user_input()
    calcaverage()
    find_min_max()
    sort_temperature()
    calc_median_temperature()


def display_main_menu():
    print('“Enter some numbers separated by commas (e.g. 5, 67, 32)')


def get_user_input():
    input = input()
    split = input.split()
    finalinput = [float(x) for x in split]
    print('finalinput')
    return finalinput


def find_min_max():
    min = min(finalinput)
    max = max(finalinput)
    return (min, max)


def sort_temperature():
    sorted(finalinput)


def calc_median_temperature():
    median(finalinput)
