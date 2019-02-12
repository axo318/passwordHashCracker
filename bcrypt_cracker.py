import bcrypt

password_file = "rockyou-samples.bcrypt.txt"
file_to_write = "bcrypt-lines.txt"
password = "123456"

# Write dictionary results to file
def writeToFile(lineNumbers):
    f = open(file_to_write, "w+")
    for num in lineNumbers:
        line = str(num) + " "
        f.write(line)
    f.close()

## MAIN ##
def main():
    # Open file and extract string
    data = open(password_file).readlines()

    # Create an occurance dictionary
    lineNumbers = []

    #Loop through dictionary and determine how many occurances of each key are in data
    print("Getting password occurances...")
    lineCounter = 1
    found = 0
    for line in data:
        hashedPasswd = line[:-1]
        if bcrypt.checkpw(password, hashedPasswd):
            print("Found occurance in line "+ str(lineCounter))
            lineNumbers.append(lineCounter)
            found += 1
        if found == 5:
            break
        lineCounter += 1

    writeToFile(lineNumbers)
    exit()

if __name__ == '__main__':
    main()
