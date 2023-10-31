def balance(s):
    stack = []
    for char in s:
        # opening brackets
        if char in ["[","(", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            # closing brackets not match
            if char == "]" and stack[-1] != "[":
                return False

            if char == "}" and stack[-1] != "{":
                return False

            if char == ")" and stack[-1] != "(":
                return False

            # pop the last opening bracket
            stack.pop()

    return len(stack) == 0



