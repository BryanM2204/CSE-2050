from letters import letter_count, letter_frequency

def highest_freq(file):
    """
    Takes a file as a parameter and passes it through the functions imported from letters.py
    The frequency dictionary is assigned to the variable frequency which is then used to find the max value
    A for loop is then used to find the key assigned to the frequency and both the key and value are returned
    """
    #passes the file through the functions in letters.py and assigns to variable frequency
    frequency = letter_frequency(letter_count(file))
    
    #uses max() to find the highest value in the dictionary and assigns to highest_freq
    highest_freq = max(frequency.values())

    #for loop is used to find which value matches with the highest frequency in order to find the key that it is paired with
    for k, v in frequency.items():
        if v == highest_freq:
            return k, v


#Take file name from user input
file = input()

#assigns the returned values key and value from the function to the variables letter and freq respectively
letter, freq = highest_freq(file)

print(letter, freq)

#Made a test using test.txt knowing that t is the highest frequency letter used
expected_highest = 't', 0.2727272727272727

#Passes assert test only if the file being used is the test.txt, allowing for use of other files without rising an AssertionError
if file == 'test.txt':
    assert(expected_highest == highest_freq(file))