s = 'kuutfgwv'

string = ""
count = 0
longestCount = 0
longestString = ""
for i in range(len(s)):
    # if i at the first character, automatically add the character to string
    if i == 0:
        string += s[i]
        count += 1
    # if the current character is more than or equals to (in alphabeticall order) the previous number
    elif s[i] >= s[i - 1]:
        string += s[i]
        count += 1
    # if the current character is less than (in alphabeticall order) the previous number   
    elif s[i] < s[i - 1]:
        if count > longestCount:
            longestCount = count
            longestString = string
        # reset count, then count is incremented by one for current character.
        count = 0
        count = 1
        # reset string, then current character is added to string.
        string = ""
        string += s[i]
    # if i is at the last character, and the current character is continuation of a series of alphabets in ascending order, 
    # it has not been compared with longestCount yet.
    if i == len(s) - 1:
        if count > 1:
            if count > longestCount:
                longestCount = count
                longestString = string
print("Longest substring in alphabetical order is: " + longestString)