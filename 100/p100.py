# Done in Python 3.4 by Kurtis Mackey
# The 3n + 1 problem
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=29&page=show_problem&problem=36

import time


string_list = []
number_list = []
largest = [0]
num_cache = {}



# ********************************* FUNCTIONS ***********************************
# ===============================================================================


def user_input():

    try:
        """
        Takes the user input with the example format '1 2' for
        # the numbers 1 and 2 (input must be on the same line)
        """
        string_in = input()
        string_in = string_in.split()
        if (
            int(string_in[0]) >= 1
            and int(string_in[1]) >= 1
            and int(string_in[0]) <= 1000000
            and int(string_in[1]) <= 1000000):
                string_list.append([int(string_in[0]), int(string_in[1])])
        else:
            print('Not a valid sequence.  Must be between 1 - 1,000,000')
            exit()

    except ValueError:
        """
        Verify that input for both items are integers,
        if not then end program
        """
        print('ValueError:  Must be integers!')
        exit()
    except IndexError:
        return False    # If user types the Enter key, end loop

    return True     # Continues Loop


def num_seq(num):
    """
    While num between 0 and
    1,000,000 does not equal 1,
    recalculate number until it equals 1.
    Print the number of times the number changed
    """

    if (num >= 1) and (num <= 1000000):

        num_list = [num]

        while num != 1:
            num_cache[num] = len(num_list)
            if (num % 2) != 0:
                num = 3 * num + 1
                num_list.append(num)
            else:
                num = int(num/2)
                num_list.append(num)

        if largest[0] <= num_cache[num]:
            largest[0] = num_cache[num]

            if num in num_cache.keys():
                return num_cache[num]

        return largest[0]

    else:
        print('Invalid Sequence:  Must be between 0 and 1,000,000')
        exit()


def num_range(num1, num2):
    """
    With the input of any two numbers,
    Reorder the numbers so we can extract a range
    between the two.  Output the range as a list.
    """
    templist = sorted([num1, num2])
    reval_numlist = list(range(templist[0], templist[1]+1))
    return reval_numlist


def start(largest):
    """
    Start of the calculation portion of the program.  Calls 'largest' list into function
    and iterates over a range of numbers determined by string_list.
    string_list is determined by user_input().
    """
    for ii in string_list:
        for i in num_range(ii[0], ii[1]):
            num_seq(i)
        print(ii[0], ii[1], largest[0])
        largest[0] = 0

    print('%d calculations saved.' % len(num_cache))


# ***************************** VALUES AND CALC *********************************
# ===============================================================================

if __name__ == '__main__':

    print('Type two numbers in the form "1 2" for the numbers 1 and 2')

    while user_input():
        pass
    
    # print('Processing... Please Wait \n')

    # timer = time.clock()
    start(largest)
    # timer2 = time.clock()
    # print('{} seconds'.format(timer2-timer))







