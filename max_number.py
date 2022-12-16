#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program finds the largest number in a list of 10 random numbers

import random


def find_largest_num_array(num_array):
    # Finds the largest number from a list of ten random numbers

    largest_num = 0

    for counter in range(0, len(num_array)):
        if num_array[counter] > largest_num:
            largest_num = num_array[counter]

    return largest_num


def main():
    # Generates ten random numbers in an array and calls a function

    random_array = []

    for counter in range(0, 10):
        random_num = random.randint(0, 100)
        random_array.append(random_num)
        print("The random number {0} is {1}".format(counter + 1, random_num))
    largest_num_array = find_largest_num_array(random_array)
    print("\nThe largest number is {}.".format(largest_num_array))

    print("\nDone.")


if __name__ == "__main__":
    main()
