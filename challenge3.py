#define a function that return the total value of the consonants in a word
def consonant_value(word):
   #declare the alphabet
    alphabet = "-abcdefghijklmnopqrstuvwxyz"
    #replace the vowels in the word with a space
    for vowel in "aeiou" :
        word = word.replace(vowel, " ")
        #create an empty  where we will append our sum values
    values = []
    #split the word into substrings 
    for substring in word.split():
        sum = 0
        #loop through each substring to assign each letter in the alphabet a value which is its index number
        for letter in substring:
            #and add the values. 
            sum += alphabet.index(letter)
            #append the sum to our empty array
        values.append(sum)
        #return the highest value, return zero if no word is input
    return max(values, default = 0)

print(consonant_value("zodiacs"))