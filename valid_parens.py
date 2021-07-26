import datetime
begin_time = datetime.datetime.now()

def has_valid_parens(phrase):
    """Does a string have valid parentheses?"""

    parens_match = {')': '(', '}': '{', ']': '['}
    start_chars = set(parens_match.values())
    end_chars = set(parens_match)
    started = []

    for char in phrase:
        if char in start_chars:
            started.append(char)
            # print(f'started is {started}')
        elif char in end_chars:
            # print(f'new end char is {char}')
            if started == []:
                return False
            elif started[-1] != parens_match[char]:
                return False
            else: 
                started.pop()
                
    return started == []

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(datetime.datetime.now() - begin_time)