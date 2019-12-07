def isProperBracePair(leftBrace, rightBrace):
    if leftBrace == '(' and rightBrace == ')':
        return True
    elif leftBrace == '[' and rightBrace == ']':
        return True
    elif leftBrace == '{' and rightBrace == '}':
        return True
    else:
        return False


def validBraces(string):
    isRightBrace = ['}', ')', ']']
    index = -1
    for i in string:
        index += 1
        if i in isRightBrace:
            if index != 0 and isProperBracePair(string[index - 1], string[index]):
                string = string[:index - 1] + string[index + 1:]
                index = index - 2
    if len(string) == 0:
        return True
    else:
        return False
