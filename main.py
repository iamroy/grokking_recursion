def string_reversal_recursion(str):
    if len(str):
        str_rev = string_reversal_recursion(str[1:]) + str[0]
    else:
        str_rev = str

    return str_rev


def number_of_vowels_recursion(str):
    vowels = 'aeiou'

    str = str.lower()
    if len(str)>1:
        return number_of_vowels_recursion(str[0]) + number_of_vowels_recursion(str[1:])
    elif len(str) == 1:
        return int(str[0] in vowels)
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


def remove_adjacent_duplicates(str):

    if len(str)<2:
        return str

    if str[0].lower() == str[1].lower():
        return remove_adjacent_duplicates(str[1:])
    else:
        return str[0] + remove_adjacent_duplicates(str[1:])


if __name__ == '__main__':

    #print(string_reversal_recursion('apple'))
    #print(number_of_vowels_recursion('a'))
    #print(first_index_recursion([4,3,2,1,1,1,1,1], 1, 0))
    #print(fibonacci_number_at_index(7))
    #print(gcd_recursion(6,6))
    #print(pascals_triangle(8))
    #print(decimal_to_binary(8))
    # Driver Code
    #print(foo(45))
    print(remove_adjacent_duplicates("HeeLllo"))

