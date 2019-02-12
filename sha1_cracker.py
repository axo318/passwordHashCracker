#
# Finds 25 most common password occurances in sha1 encrypted text
#

import hashlib

# Relevant variables
password_file = "rockyou-samples.sha1-salt.txt"
file_to_write = "salt-cracked.txt"
password_list = ["123456","12345", "123456789", "password", "iloveyou",
"princess", "1234567", "rockyou", "12345678", "abc123",
"nicole", "daniel", "babygirl", "monkey", "lovely",
"jessica", "654321", "michael", "ashley", "qwerty",
"111111", "iloveu", "000000", "michelle", "tigger"]

# Returns a dictionary with all salts and respective hashes
def getDictionary():
    dic = dict()
    #Read the lines and add them to dictionary
    data = open(password_file, "r").readlines()
    for line in data:
        string = line[1:-1]             # Get rid of new line and first dollar symbol
        lineList = string.split("$")    # Split line
        salt = lineList[1]              # Get the salt
        hashed = lineList[2]            # Get the hashed value
        dic[salt] = hashed              # Enter pair in dictionary
    return dic

# Calculates hash from passwd and salt
def getHashedPassword(salt, password):
    m = hashlib.sha1()
    m.update(bytes(salt, "ascii"))
    m.update(bytes(password, "ascii"))
    return str(m.hexdigest())

# Write dictionary results to file
def writeToFile(occurance_dict):
    f = open(file_to_write, "w+")
    for key in occurance_dict:
        line = str(occurance_dict[key]) + "," + key + "\n"
        f.write(line)
    f.close()

## MAIN ##
def main():
    # Get dictionary with salts and hashes
    dic = getDictionary()

    # Create an b" the spammish repetition"occurance dictionary
    occurances = dict()

    #Loop through dictionary and determine how many occurances of each key are in data
    for password in password_list:
        for salt in dic:
            if(dic[salt]==getHashedPassword(salt, password)):
                n = occurances.get(password, 0)
                occurances.update({password:n+1})

    writeToFile(occurances)
    exit()

if __name__ == '__main__':
    main()
