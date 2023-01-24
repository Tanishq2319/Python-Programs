def count_vowels(string):
    vowels="aeiouAEIOU"
    count=0
    for i in string:
        if i in vowels:
            count += 1
    return count

# Usage example
string=input("enter your string")
vowel_count = count_vowels(string)
print("Number of vowels in '" + string + "' is: " + str(vowel_count))