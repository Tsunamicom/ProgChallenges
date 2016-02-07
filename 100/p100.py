# Done in Python 3.4 by Kurtis Mackey
# The 3n + 1 problem
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=29&page=show_problem&problem=36

import time

string_list = []
largest = [0]
num_cache = dict()



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

    count = 1
    temp = num

    while temp != 1:
        if (temp % 2) != 0:
            temp = 3 * temp + 1
        else:
            temp = int(temp/2)

        # Recall memo if the new value is within num_cache
        if temp in num_cache:
            num_cache[num] = num_cache[temp] + count
            return num_cache[temp] + count
        count += 1

    # Store new value for process length for given number
    num_cache[num] = count

    return count




def num_range(num1, num2):
    """
    With the input of any two numbers,
    Reorder the numbers so we can extract a range
    between the two.  Output the range as a list.
    """
    numlist = sorted([num1, num2])
    reval_numlist = list(range(numlist[0], numlist[1]+1))
    return reval_numlist


def start():
    """
    Start of the calculation portion of the program.  Calls 'largest' list into function
    and iterates over a range of numbers determined by string_list.
    string_list is determined by user_input().
    """
    for ii in string_list:
        for i in num_range(ii[0], ii[1]):
            sequence = num_seq(i)
            if largest[0] <= sequence:
                largest[0] = sequence
        print(ii[0], ii[1], largest[0])
        largest[0] = 0  # Reset largest for multiple input strings





# ***************************** VALUES AND CALC *********************************
# ===============================================================================

if __name__ == '__main__':

    print('Type two numbers in the form "1 2" for the numbers 1 and 2')

    while user_input():
        pass

    t1 = time.clock()
    start()
    t2 = time.clock()
    print('%s ' % (t2-t1))
