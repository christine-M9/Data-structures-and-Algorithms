def is_balanced(expression):
    stak = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}

    for char in expression:
        if char in opening_brackets:
            stak.append(char)
        elif char in closing_brackets:
            if not stak or bracket_pairs[stak.pop()] != char:
                return False

    return not stak


if __name__ == "__main__":
    expression1 = "([]{})"
    expression2 = "([)]"
    print(is_balanced(expression1))  
    print(is_balanced(expression2))  
