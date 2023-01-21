import string

def letter_count(file):
    """
    Opens a file and creates a list of all the words assigned to variable my_list
    Creates a nested for loop to target every letter, then compare to string.ascii_lowercase
    returns dictionary of all letters and occurrences in file that is then passed through letter_frequency() function
    """

    occurrences = {}

    #opens the file 
    f = open(file)
    #reads file and assigns list to variable
    my_list = f.readlines()

    #closes file
    f.close()

    #Scan each word and then each letter
    for word in my_list:
        for letter in word.lower():

            #Check to see if letter is in dictionary and if it is a lowercase letter
            #Adds +1 to existing key
            if letter in occurrences and letter in string.ascii_lowercase:
                occurrences[letter] += 1
            
            #Checks to see if letter is not in dictionary but it is a lowercase letter
            #Creates a new key with the value of 1
            elif letter not in occurrences and letter in string.ascii_lowercase:
                occurrences[letter] = 1

    #occurrences is returned
    return occurrences


def letter_frequency(dict_letters):
    """
    Takes the dictionary created from letter_count() function and sums up all the values and divides the occurrence of each letter by the total number of letters
    A for loop is created to do this calculation for every letter which a new dictionary is created with the letter and its frequency
    """
    frequency_dict = {}

    #sums up all the values in dict_letters from letter_count()
    num_occurrences = sum(dict_letters.values())

    #for each value of a key, the value is divided by the total number of letters to find the frequency
    for k, v in dict_letters.items():
        frequency = v / num_occurrences

        #A new dictionary is created with the key and frequency being added
        frequency_dict[k] = frequency
   
    return frequency_dict
        
if __name__ == '__main__':
    
    file_name = input()
    # letter_frequency(letter_count(file_name))

    expected_count = {'a':1,
                      'e':1,
                      'h':1,
                      'i':2,
                      's':3,
                      't':3
                     }

    actual_count = letter_count(file_name) 
    assert(expected_count == actual_count) 