"""
Lab 8 - Set and Dict 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  Gabrielle Boily
Due Date: This Friday (Mar. 13) 5pm.
Note: Try best to finish the lab exercises using what we've learnt about algorithms.
      Please do not rely on AI assistant too heavily for labs.

Objective:
1. Review how to write a good python docstring (started from lab7).
2. Review how to code simple Python functions and write unit tests using assert.
3. Practice how to operate on set and dict.
4. Review iterations using loop.
5. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, a set, a dict, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Here is one solution of Lab 7 exercise 3: Remove the duplicate characters in a string.
E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"
"""
def remove_duplicates(s):
    """
    This function removes the duplicates from the string s.

    E.g.,
    >>> remove_duplicates("Apple")
    "Aple"
    """
    res = ''
    for c in s:
        if c not in res:
            res += c
    return res
    
# Your unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"

"""
Exercise 1 (20 marks: doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Can you try to implement the above duplicates removal using data type set?

Hint: 1. We put the seen chars in the set while adding them to the res string;
      We also check if the new char is already in the set (more efficient than checking a string). If not seen, add it to the res string.
      2. To initialize an empty set: seen_set = set()
"""
def remove_duplicates_set(s):
    """
    This function removes duplicate characters from a given string.

    E.g.,
    >>> remove_duplicates_set('Apple Banana')
    'Aple Ban'

    Parameters:
    - s (string): the given string from which we want to remove the duplicate characters.

    Returns:
    - (string): the new string, with no repeated characters.
    """
    res = ""
    seen_set = set()
    for c in s:
        if c not in seen_set:
            seen_set.add(c)
            res += c
    return res
    
    
#Your unit tests

assert remove_duplicates_set('apple') == 'aple'
assert remove_duplicates_set('Popsipple') == 'Popsile'
assert remove_duplicates_set('I love coffee and tea') == 'I lovecfandt'
"""
Exercise 2 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Assume you've collected many stones, 
and each character in the string stones represents a type of a stone. 
And each character in the string gems represents a type of a gem.

Write a function to calculate how many stones you've collected are actually jems. 
Requirement: Implement the function using data type set

E.g.,
gem_counting("abDFMdm", "admMQq") will return 4
gem_counting("abDFMdm", "af") will return 1
gem_counting("awCcM", "cQqW") will return 1
gem_counting("bFfL", "cQqW") will return 0
"""
def gem_counting(stones, gems):
    """
    This function serves to calculate the number of gem scharacters found in a string of stones.

    E.g.,
    >>> gem_counting("abcdeFg", "afbd")
    3

    Parameters:
    - stones (string): each character represents a type of stone collected.
    - gems (string): each character represents a type of gem.

    Returns:
    - (int): the number of gems found within the 'stones' parameter.
    """
    res = 0
    set_gems = set(gems)
    for c in stones:
        if c in set_gems:
            res += 1
    return res


# Your unit tests

assert gem_counting("abDFMdm", "admMQq") == 4
assert gem_counting("aaDFMdm", "af") == 2
assert gem_counting("awCcM", "cQqW") == 1
assert gem_counting("bFfL", "cQqW") == 0

"""
Exercise 3 (20 marks: doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

CapU is planning to launch a shuttle bus between main campus 
and the students accomendation. (Fake news but best wishes 😄)

To determine how many buses are needed each day, 
CapU keeps track of the students who use the shuttle bus service.

Write a function students_id() that takes a list of student ids as its parameter, 
and returns the number of different students who use the shuttle service.

E.g.,
students_id(['002', '003', '001', '004', '012']) returns 5
students_id(['002', '003', '001', '012', '003', '001']) returns 4

Hint: 
Think about which data type we should use to ease the work of finding distinctive values from a list.

"""
def students_id(ids):
    """
    This function returns the number of different students using Capilano University's shuttle bus per day.

    E.g., 
    >>> students_id(['001', '001', '003', '004'])
    3

    Parameters:
    - ids (list): a list of the daily students' id numbers who used the shuttle service.

    Returns:
    - (int): the number of different students who used the service on a given day.
    """
    new_ids = set(ids)
    return len(new_ids)

# Your unit tests

assert students_id(['001', '001', '001']) == 1
assert students_id(['001', '002', '003', '002', '006']) == 4


"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Similar as exercise 3, write a function called students_id_occurences() 
that takes a list of student ids as its parameter, 
and returns the occurences of each different student 
who uses the shuttle service in the form of dictionary data type.

E.g.,
students_id_occurences(['002', '003', '001', '004', '012']) 
returns {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}}

students_id_occurences(['002', '003', '001', '012', '003', '001']) 
returns {'002': 1, '003': 2, '001': 2, '012': 1}

Hint: To initialize an empty dict: id_dict = {}
"""
def students_id_occurrences(ids):
    """
    This function serves to return the number of occurences of each student using the shuttle service.

    E.g.,
    >>> students_id_occurences(['001', '001', '002', '002'])
    {'001': 2, '002': 2}

    Parameters:
    - ids (list): a list of the daily students' id numbers who used the shuttle service.

    Returns:
    - (dict): a dict list that uses the student's id number as a key, and the number of occurences as a value. 
    """
    id_dict = {}
    for id in ids:
        if id in id_dict:
            id_dict[id] += 1
        else:
            id_dict[id] = 1
    return id_dict


# Your unit tests

assert students_id_occurrences(['001', '001', '002', '003', '004']) == {'001': 2, '002': 1, '003':1, '004': 1}
assert students_id_occurrences(['231', '231', '231', '001']) == {'001': 1, '231': 3}


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to count 
the frequency of words in a given paragraph.

E.g.,
word_frequency("I am alive. I am happy.") 
returns {'I': 2, 'am': 2, 'alive': 1, 'happy': 1}

word_frequency("I do not like water. I like fruits.") 
returns {'I': 2, 'do': 1, 'not': 1, 'like': 2, 'water': 1, 'fruits': 1}

# Hint: 
# import Python's regular expression (pattern used to search for text patterns) module re. 
# re.findall(r'\b\\w+\b', s) returns list of words from s that matches the pattern of word.
"""
import re
def word_frequency(paragraph):
    """
    This function serves to return the word count frequency in a given paragraph.

    E.g.,
    >>> word_frequency("I like Python and I like donuts")
    {'I': 2, 'like': 2, 'Python': 1, 'and': 1, 'donuts': 1}

    Parameters:
    - paragraph (string): The paragraph from which we want to count the word frequency.

    Returns:
    - (dict): displays unique words from the paragraph as keys and their frequency in the paragraph as values.
    """
    word_dict = {}
    words = re.findall(r'\b\w+\b', paragraph)
    for w in words:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1
    return word_dict


# Your unit tests

assert word_frequency("My name is Gabrielle. My last name is Boily") == {'My': 2, 'name': 2, 'is': 2, 'Gabrielle': 1, 'last': 1, 'Boily': 1}
assert word_frequency("I like Python and I like donuts") == {'I': 2, 'like': 2, 'Python': 1, 'and': 1, 'donuts': 1}
assert word_frequency("I am alive. I am happy.") == {'I': 2, 'am': 2, 'alive': 1, 'happy': 1}




"""
Real-world Coding Question (optional): Extract Repository IDs and Names from GitHub API Data

The GitHub API allows you to search for repositories using different criteria. 
The following code sends a request to GitHub to find Python repositories with more than 300,000 stars.

The API response is converted into a Python dictionary called response_dict. 
Inside this dictionary, the key "items" contains a list of repository dictionaries,
where each repository includes information such as id, name, stars, and more.
"""

# import requests

url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>300000"
# You can copy and paste the url into your browser to view the data.

# headers = {"Accept": "application/vnd.github.v3+json"}
# response = requests.get(url, headers=headers)

# print(f"Status Code: {response.status_code}") 
# HTTP response status code 200 means The server processed the request and returned the requested data successfully.

# response_dict = response.json() # Convert the response object to a dictionary


"""
Task: Write a function called id_name_repo_starred_300k(response_dict) that
takes response_dict as its parameter, 
traverses the list stored under the "items" key,
returns a dictionary containing all repository id → name pairs.

Ensure that your function passes the unit test provided below.
"""

# Save the repositories' id: name as a pair in a dict, and print them out.
def id_name_repo_starred_300k(response_dict):
    pass

# assert id_name_repo_starred_300k(response_dict) == {
#     13491895: 'free-programming-books',
#     54346799: 'public-apis',
#     83222441: 'system-design-primer'
#     }


"""
Congratulations on finishing your lab8. Hope you feel more comfortable now on the data type set and dict.

You just need to upload this lab to your GitHub repository, and copy the link to e-learn. That's all.
"""