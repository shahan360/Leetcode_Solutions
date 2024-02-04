def isIsomorphic(s, t): #Check if the two strings are isomorphic
    if len(s) != len(t): #If the length of the two strings are not equal, then they cannot be isomorphic
        return False #Return False
    
    s_to_t_mapping = {} #Create a dictionary to store the mapping from s to t
    t_to_s_mapping = {} #Create a dictionary to store the mapping from t to s

    for char_s, char_t in zip(s, t): #Iterate through the characters of the two strings
        if char_s in s_to_t_mapping: #If the character from s is already in the dictionary
            if s_to_t_mapping[char_s] != char_t: #If the mapping from s to t is not equal to the character from t
                return False #Return False
        else: #If the character from s is not in the dictionary
            s_to_t_mapping[char_s] = char_t #Add the mapping from s to t

        if char_t in t_to_s_mapping:
            if t_to_s_mapping[char_t] != char_s:
                return False
        else:
            t_to_s_mapping[char_t] = char_s

    return True #If the two strings are isomorphic, return True

# Time complexity: O(n) where n is the length of the string
# Space complexity: O(n) where n is the length of the string

# Driver code
s1 = "egg"
t1 = "add"
print(isIsomorphic(s1, t1)) #Output: True

s2 = "foo"
t2 = "bar"
print(isIsomorphic(s2, t2)) #Output: False