# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Sort the characters of the word we're checking against
        sorted_word = sorted(self.word)
        
        # Initialize an empty list to store matching anagrams
        matches = []
        
        # Iterate over each word in the provided list
        for word in word_list:
            # Check if the sorted characters of both words are the same
            if sorted(word) == sorted_word:
                matches.append(word)
        
        # Return the list of matching anagrams
        return matches
