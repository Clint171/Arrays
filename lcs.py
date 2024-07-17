def generate_array(str1 : str , str2 : str):
    union = []
    for i in range(0 , len(str1)):
        row = []
        for j in range(0 , len(str2)):
            if(str1[i] == str2[j]):
                row.append(1)
            else:
                row.append(0)
        print(*row)
        union.append(row)
            
    return union

def get_common_subsequences(str1: str , str2: str):
    array = generate_array(str1 , str2)
    subsequences = []
    for i in range(0 , len(str1)):
        for j in range(0 , len(str2)):
            if array[i][j] == 1:
                sequence = []
                count = 0
                sequence.append(str1[i])
                for k in range(j + 1 , len(str2)):
                    count += 1
                    if(array[i+count][k] == 1):
                        sequence.append(str1[i+count])
                    else:
                        break
                if sequence not in subsequences:
                    subsequences.append(sequence)
    return subsequences
  
def main():
    print("Subsequences: " , get_common_subsequences("racecar" , "palace"))

if(__name__ == "__main__"):
    main()