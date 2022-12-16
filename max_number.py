#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program finds the largest number in a list of 10 random numbers

import random


def main():
    # this function uses an array
    answer = 0

    random_numbers = []
    # process
    for loop_counter in range(0, 10):
        a_random_number = random.randint(1, 100)  # a number between 1 and 100
        print("The random number is: {0}".format(a_random_number))
        random_numbers.append(a_random_number)
    print("")

    for loop_counter in range(0, len(random_numbers)):
        answer = answer + random_numbers[loop_counter]
    max_num = max(random_numbers)

    print("\nThe largest number is: {0}".format(max_num))

    print("\nDone.")


if __name__ == "__main__":
    main()
