import sys

def generate_array(str1 : str , str2 : str):
    union = []
    for i in range(0 , len(str1)):
        row = []
        for j in range(0 , len(str2)):
            if(str1[i] == str2[j]):
                row.append(1)
            else:
                row.append(0)
        union.append(row)
            
    return union

def get_common_subsequences(str1: str , str2: str):
    array = generate_array(str1 , str2)
    subsequences = []
    for i in range(0 , len(str1)):
        for j in range(0 , len(str2)):
            if array[i][j] == 1:
                sequence = ""
                count = 0
                sequence +=(str1[i])
                for k in range(j + 1 , len(str2)):
                    count += 1
                    if(i + count >= len(str1)):
                        break
                    if(array[i+count][k] == 1):
                        sequence += (str1[i+count])
                    else:
                        break
                if sequence not in subsequences and len(sequence) >1:
                    subsequences.append(sequence)

    longest = ""
    for i in subsequences:
        if(len(i) > len(longest)):
            longest = i
    return longest
  
def getSubsequence(arguments : list):
    lcs = ''
    for i in range(0 , len(arguments)):
        if i == 0 or i == 1:
            lcs = get_common_subsequences(arguments[0] , arguments[1])
        
        else:
            lcs = get_common_subsequences(lcs , arguments[i])
    print(lcs)
    return lcs

def main():
    if len(sys.argv) > 1 :
        getSubsequence(sys.argv[1:])
    else:
        strings = input("Enter the strings, separated by spaces\n")
        getSubsequence(strings.split(" "))

if(__name__ == "__main__"):
    main()