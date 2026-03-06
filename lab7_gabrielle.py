"""
Lab 7 - Strings and Tuples 
(100 marks in total)

Author:  Gabrielle Boily
Due Date: This Friday (Mar. 6) 5 pm.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    '''This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.
    '''
    r = ""
    for c in s:
        r = c + r
    return r

    

# Your unit tests

assert reverse_str("giraffe") == "effarig"
assert reverse_str("Gabrielle") == "elleirbaG"
assert reverse_str("star") == "rats"

"""
Exercise 2 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    vowel = "AEIOUaeiou"
    n = 0
    for c in s:
        if c in vowel:
            n += 1
    return n
    

# Your unit tests
assert count_vowels("coffee") == 3
assert count_vowels("Apples are healthy") == 6
assert count_vowels("phone call") == 3


"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: in
"""
def remove_duplicates(s):
    """This function removes the duplicate characters in the string s.
    
    E.g.,
    >>> remove_duplicates("apple")
    "aple"
    
    Parameters:
    -s (string): the string from which we want to remove duplicate characters.
    
    Returns:
    - (string): the new string that has had its duplicates removed (including spaces).
    """
    r = ""
    for c in s:
        if c not in r:
            r = r + c
    return r


# Your unit tests

assert remove_duplicates("book") == "bok"
assert remove_duplicates("I like coffee") == "I likecof"
assert remove_duplicates("cats") == "cats"


"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
use break
"""
def find_index(s, t):
    """
    This fuction returns the lowest index of a character (t) found in a string (s). If the character is
    not in the string, the function returns -1.

    E.g.,
    >>> find_index("abcd", "d")
    3

    Parameters:
    - s (string): the string in which we want to locate a character.
    - t (string): the character we want to locate in the string s.

    Return:
    - (int): the lowest position of the character t within the string s.
    """
    for i in range(len(s)):
        if t in s:
            return s.index(t)
        else:
            return -1

# Your unit tests
assert find_index("abc", "b") == 1
assert find_index("tea", "z") == -1
assert find_index("aaa", "a") == 0
assert find_index("abccdeff", "f") == 6 

"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    This function serves to return the day of completion of a project, based on the inputs of today's day and the
    number of days to completion.

    E.g.,
    >>> project_completion_day('Monday', 3)
    'Thursday'

    Parameters:
    - day (string): today's day name.
    - days_to_completion (int): the number of days to the project's completion.

    Return:
    - (string): the name of the day the project will be completed.

    Note: the days_week tuple is required for this function to work.
    """
    day_number = days_week.index(day)
    dtc_number = (day_number + days_to_completion) % 7
    return days_week[dtc_number]

# Your unit tests

assert project_completion_day('Monday', 3) == 'Thursday'
assert project_completion_day('Wednesday', 9) == 'Friday'
assert project_completion_day('Sunday', 0) == 'Sunday'

"""Log Parsing Exercise (20 marks - function implementation 10, unit test 5, function usage 5)

You are given a log string containing application logs 
in a standardized format. Each log entry contains 
a timestamp, severity level, module name, and message.
Your task is to implement two functions to parse and filter
these logs.

Log format - Each log line follows this pattern:
YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message

Sample log data: """
'''
log_string =
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s 
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
'''
"""
Implement a function parse_log_line(line) to parse a single log line into its components.

Your function returns:
A tuple of 4 elements: (timestamp, level, module, message)

timestamp (str): Date and time in format "YYYY-MM-DD HH:MM:SS"
level (str): Log severity level ("ERROR", "WARNING", or "INFO")
module (str): The Python module/file name (e.g., "database.py")
message (str): The log message text

E.g.,
line = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
parse_log_line(line) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

Hint: str.split() returns a list of strings, split by default (whitespace).
"hello world python".split()
# Returns: ['hello', 'world', 'python']

use concantentation and add a string " " for space
last part, use .join() function and 
Alice could do it in 2 lines of code, but I can organize it in sections
"""

def parse_log_line(line):
    split_up = line.split()
    timestamp = split_up[0] + " " + split_up[1]
    level = split_up[2].strip('[]')
    module = split_up[3]
    message = " ".join(split_up[4:])
    return (timestamp, level, module, message)

# Your unit tests
line = '2024-03-05 14:33:15 [ERROR] api.py Request handler crashed'
assert parse_log_line(line) == ('2024-03-05 14:33:15', 'ERROR', 'api.py', 'Request handler crashed')

line2 = '2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable'
assert parse_log_line(line2) == ('2024-03-05 14:33:02', 'WARNING', 'cache.py', 'Redis connection unstable')


# Use your parse_log_line() to parse all the lines in the sample data log_string,
# and store each tuple item in a list.
# Hint: log_string.split('\n') will return a list of lines.


"""
Congratulations on finishing your lab7. Hope you feel more confident 
on function implementation.

Now you just need to upload it to your GitHub repository, and paste the link on e-learn. That's all.
"""