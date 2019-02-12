#
# Finds password occurances in md-5 encrypted text
#

import hashlib
import time
import sys
from string import ascii_lowercase
from itertools import product

# Relevant variables
password_file = "rockyou-samples.md5.txt"
file_to_write = "md5-cracked.txt"
char_string = ascii_lowercase + "0123456789"

# Returns dict with all combinations and their hashes
def getHashedPasswordsDict():
    # Create a dictionary with all combination values initialized to 0
    print("Initializing hashed dictionary...")
    combs = product(char_string, repeat=5)
    new_dict = dict()
    counter = 0
    for comb in combs:
        plain_passwd = "".join(comb)
        key = str(hashlib.md5(plain_passwd.encode()).hexdigest())
        new_dict[key] = plain_passwd

    print("Hashed dictionary initialized:")
    return new_dict

# Write dictionary results to file
def writeToFile(occurance_dict):
    f = open(file_to_write, "w+")
    for key in occurance_dict:
        line = str(occurance_dict[key]) + "," + key + "\n"
        f.write(line)
    f.close()


## MAIN ##
def main():
    # Open file and extract string
    data = open(password_file).readlines()

    # Get hashed dictionary
    hashed_dictionary = getHashedPasswordsDict()

    # Create an occurance dictionary
    occurances = dict()

    #Loop through dictionary and determine how many occurances of each key are in data
    print("Getting password occurances...")
    for line in data:
        decrypted_pass = hashed_dictionary.get(line[:-1], None)
        if decrypted_pass==None:
            continue
        else:
            n = occurances.get(decrypted_pass,0)
            occurances.update({decrypted_pass:n+1})

    print("Password occurances found")
    print("Writting to file...")
    writeToFile(occurances)
    print("Writting complete")

if __name__ == '__main__':
    main()
