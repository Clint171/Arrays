def longestCommonPrefix(strs: list) -> str:
    if "" in strs:
        return ""
    lcp = ""
    strs.sort(key=len)
    print(*strs)

    for i in range(0 , len(strs[0])):
        occurrences = 1
        for j in range(1 , len(strs)):
            if(strs[j][i] == strs[0][i]):
                print(strs[0][i])
                occurrences += 1
            else:
                break

        if(occurrences == len(strs)):
            lcp += strs[0][i]
        
    return lcp

def main():
    print(longestCommonPrefix(["cirronimbus" , "carbon"]))


if __name__ == "__main__":
    main()
