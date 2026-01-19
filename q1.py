"""
Q1: Stable Character

You are given a string `s`.

In this string, some characters may appear multiple times.

A character is called **stable** if all of its occurrences appear **together as
one continuous group**, without being interrupted by other characters.

Your task is to identify the **first stable character** you encounter when
reading the string from left to right.

If the string does not contain any stable character, return `None`.

Examples:
---------
Input: "aaabccddde"  → Output: 'a'
Input: "abccba"      → Output: 'c'
Input: "aabbcc"      → Output: 'a'
Input: "abc"         → Output: None
Input: "a"           → Output: None

Explanation:
- In "abccba", 'c' appears at positions 2,3 (continuous), while 'a' and 'b'
  are interrupted
- Single character occurrences are not considered stable (must appear at least
  twice)
"""


def first_stable_character(s):
    i = 0
    while i < len(s):
        ch = s[i]
        j = i
        while j < len(s) and s[j] == ch:
            j += 1
        size = j - i
        if size >= 2:
            if ch not in s[j:]:
                return ch
        i = j
    return "None"



if __name__ == "__main__":
    # Test your solution here
    print(first_stable_character("abccba"))  # Should print: c
    print(first_stable_character("abc"))     # Should print: None
    print(first_stable_character("a"))       # Should print: None
