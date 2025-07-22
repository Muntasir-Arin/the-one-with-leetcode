class Solution:
    def isValid(self, word: str) -> bool:

        def has_no_vowels(s):
            vowels = set('aeiou')
            return vowels.isdisjoint(s.lower())

        def has_no_consonants(s):
            consonants = "bcdfghjklmnpqrstvwxyz"
            return all(char.lower() not in consonants for char in s)

        if len(word)<3:
            return False
        if not word.isalnum():
            return False

        if has_no_vowels(word) or has_no_consonants(word):
            return False


        return True