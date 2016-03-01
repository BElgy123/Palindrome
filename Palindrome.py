def is_palindrome(test_string):
    """ A standalone function to check if a string is a palindrome.

    :param test_string: the string to test
    :return: boolean
    """
    t = test_string #Change parameter name cause it's too long for laziness
    _t = [] #Will be expanded form of t
    t_ = [] #Will be _t backwards
    if(not(type(t) is str)): #Check if String
        return False
    if(len(t) == 0): #Check if Empty
        return False
    t = t.upper() #Make it uppercase
    for i in t: #Set list _t to an expaded form of the input
        if(i != " "):
            _t.append(i)
    i = len(_t)-1
    while(i>=0):# set t_ to _t backwards
        t_.append(_t[i])
        i-=1
    if(t_ == _t):#Check if forwards and backwards form are the same
        return True
    else:
        return False
            

if __name__ == '__main__':
    assert is_palindrome('') == False  # an empty string is not a palindrome
    assert is_palindrome(17) == False  # an integer is not a string, not a palindrome
    assert is_palindrome("1") == True  # "1" is the same forwards as it is backwards, in this project, we'll consider 1 character strings palindromes
    assert is_palindrome("stuff") == False  # "stuff" is not a palindrome
    assert is_palindrome("tacocat")  # all lowercase, no spaces
    assert is_palindrome("MoM") == True  # upper and lower, no spaces
    assert is_palindrome("Borrow or rob") == True  # upper and lower, spaces
    assert is_palindrome("A nut for a jar of tuna") == True  # same
