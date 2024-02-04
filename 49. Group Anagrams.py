def group_anagrams(words):
    anagram_groups = {} #Create a dictionary to store the anagram groups

    for word in words: #Iterate through the words list
        sorted_word = ''.join(sorted(word)) #Sort the word and join it back together
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word) #If the sorted word is already in the dictionary, append the word to the list
        else:
            anagram_groups[sorted_word] = [word] #If the sorted word is not in the dictionary, create a new list with the word

    return list(anagram_groups.values()) #Return the values of the dictionary as a list

# Time complexity: O(w * n * log(n)) where w is the number of words and n is the length of the longest word
# Space complexity: O(wn) where w is the number of words and n is the length of the longest word
# w * n * log(n) because we are sorting each word which takes O(n * log(n)) time

# Driver code
input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(input_words)
print(result) #Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]   
