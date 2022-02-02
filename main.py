import linkedlist as l

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


def average_recursion(nums, current_index):

    if current_index==len(nums):
        return 0

    return nums[current_index]/len(nums)+average_recursion(nums, current_index+1)


def balanced_parenthesis(string, start_index, curr_index):

    if start_index == len(string):
        return curr_index == 0

    if curr_index < 0:
        return False

    if string[start_index] == "(":
        return balanced_parenthesis(string, start_index + 1, curr_index + 1)
    elif string[start_index] == ")":
        return balanced_parenthesis(string, start_index + 1, curr_index - 1)


def sort_recursion(nums, length):

    if length <= 1:
        return

    sort_recursion(nums, length-1)
    #print(nums, nums[-1], nums[length-1])
    last_element = nums[length-1]

    i = length-2

    while i>=0 and nums[i]>last_element:
        nums[i+1] = nums[i]
        i -= 1

    nums[i+1] = last_element


def reverse_linked_list_recursion(linked_list, current, previous):
    if current.next is None:
        linked_list.head = current
        current.next = previous
        return

    next_node = current.next
    current.next = previous

    return reverse_linked_list_recursion(linked_list, next_node, current)

def reverse_linked_list_driver(linked_list):
    if linked_list.head is None:
        return

    return reverse_linked_list_recursion(linked_list, linked_list.head, None)



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
    #print(is_palindrome_recursion("0110"))
    #testVariable = [10,1,4]
    #currentIndex = 0
    #print(average_recursion(testVariable, currentIndex))
    #string_arr= ["(", "(", ")", "(", ")"]
    #print(balanced_parenthesis(string_arr, 0, 0))
    #nums = [4, 1, 3,2]
    #length = 4
    #sort_recursion(nums, length)
    #print(nums)
    # Driver Code
    myLinkedList = l.LinkedList()
    myLinkedList.append_node(3)
    myLinkedList.append_node(4)
    myLinkedList.append_node(7)
    myLinkedList.append_node(11)

    print("Original Linked List")
    myLinkedList.print_linked_list()

    reverse_linked_list_driver(myLinkedList)
    print("\nReversed Linked List")
    myLinkedList.print_linked_list()
