def string_reversal_recursion(string):
    if len(string):
        str_rev = string_reversal_recursion(string[1:]) + string[0]
    else:
        str_rev = string

    return str_rev


def number_of_vowels_recursion(string):
    vowels = 'aeiou'

    string = string.lower()
    if len(string)>1:
        return number_of_vowels_recursion(string[0]) + number_of_vowels_recursion(string[1:])
    elif len(string) == 1:
        return int(string[0] in vowels)
    else:
        return 0


def first_index_recursion(nums, target, current_index):
    if len(nums) == current_index:
        return -1
    if nums[current_index] == target:
        return current_index

    return first_index_recursion(nums, target, current_index + 1)


def fibonacci_number_at_index(index):

    if index <= 1:
        return index

    return fibonacci_number_at_index(index-1)+fibonacci_number_at_index(index-2)


def gcd_recursion(a, b):

    if a>=b:
        rem = a % b
        d = b
    else:
        rem = b % a
        d = a

    if rem == 0:
        return d

    return gcd_recursion(d, rem)


def pascals_triangle(row_id):

    if row_id == 0:
        return [1]

    node_list = [1]

    previous_line = pascals_triangle(row_id-1)

    for i in range(len(previous_line)-1):
        node_list.append(previous_line[i]+previous_line[i+1])

    node_list.append(1)

    return node_list


def decimal_to_binary(num):

    if num == 0:
        return "0"
    if num == 1:
        return "1"

    return str(decimal_to_binary(num//2)) + str(num%2)


def foo(n):
    print(n)
    if n > 100:
        return n - 5
    return foo(foo(n + 11))


def remove_adjacent_duplicates(string):

    if len(string)<2:
        return string

    if string[0].lower() == string[1].lower():
        return remove_adjacent_duplicates(string[1:])
    else:
        return string[0] + remove_adjacent_duplicates(string[1:])


def string_length_recursion(string):

    if not string:
        return 0
    else:
        return 1 + string_length_recursion(string[1:])


def sum_digits_recursion(string):

    if not string:
        return 0

    return int(string[0])+sum_digits_recursion(string[1:])


def is_palindrome_recursion(string):
    if not string:
        return True

    if len(string) == 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome_recursion(string[1:len(string)-1])
    else:
        return False


if __name__ == '__main__':

    #print(string_reversal_recursion('apple'))
    #print(number_of_vowels_recursion('a'))
    #print(first_index_recursion([4,3,2,1,1,1,1,1], 1, 0))
    #print(fibonacci_number_at_index(7))
    #print(gcd_recursion(6,6))
    #print(pascals_triangle(8))
    #print(decimal_to_binary(8))
    #print(foo(45))
    #print(remove_adjacent_duplicates("HeeLllo"))
    #print(string_length_recursion("a"))
    #print(sum_digits_recursion("345671"))
    print(is_palindrome_recursion("0110"))
