def checkpalindrome(w, l, r):
    if l>=r:
        return True
    if w[l] == w[r]:
        return checkpalindrome(w, l+1, r-1)
    else:
        return False

def ispalindrome(word: str):
    return checkpalindrome(word, 0, len(word)-1)
    
print(ispalindrome("MUHBHUM"))