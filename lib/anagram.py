# your code goes here!

class Anagram:

    def __init__(self,word):
        self.word = word


    def match(self,list):
        checkable_word = sorted(self.word)

        found_anagram = [word for word in list if sorted(word)== checkable_word]

        return found_anagram