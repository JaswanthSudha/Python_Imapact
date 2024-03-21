if __name__=="__main__":
    string=input()
    words=string.split()
    new_String=""
    for i in range(len(words)-1,-1,-1):
        new_String+=words[i]
        new_String+=' '
    print(new_String)