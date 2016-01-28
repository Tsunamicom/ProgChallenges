# Done in Python 3.4 by Kurtis Mackey
# The 3n + 1 problem
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=29&page=show_problem&problem=36


# ********************************* FUNCTIONS ***********************************
# ===============================================================================

def user_input():

    try:
        """
        Takes the user input with the example format '1 2' for
        # the numbers 1 and 2 (input must be on the same line)
        """
        string_in = input().split()

        number_list.append(int(string_in[0]))
        number_list.append(int(string_in[1]))

        string_list.append([int(string_in[0]), int(string_in[1])])

    except ValueError:
        # Verify that input for both items are integers
        print('ValueError:  Must be integers!')
        exit()
    except IndexError:
        print('IndexError:  Must have a value!')
        exit()


def num_seq(num):
    """
    While the number between 0 and
    1,000,000 does not equal 1,
    recalculate number until it equals 1.
    Print the number of times the number changed
    """
    if (num > 0) and (num < 1000000):

        num_list = [num]

        while num != 1:

            if (num % 2) != 0:
                num = 3 * num + 1
                num_list.append(num)
            else:
                num = int(num/2)
                num_list.append(num)

        largest.append(len(num_list))
    else:
        print('Invalid Sequence:  Must be between 0 and 1,000,000')
        exit()

# ***************************** VALUES AND CALC *********************************
# ===============================================================================


# Original Values
string_list = []
number_list = []
largest = []

# Request a list to be generated
user_input()

number_list = sorted(number_list)

# Create new list from numbers
reval_numlist = list(range(number_list[0], number_list[1]+1))
# print(reval_numlist)



for i in reval_numlist:
    num_seq(i)

# print(string_list)
print('%d %d %d' % (number_list[0], number_list[1], sorted(largest).pop()))







