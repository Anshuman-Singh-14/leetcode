
# s is a string having the problem input of brackets

def isValid(self, s):
    stack = []

    opening = "[{("
    closing = ")}]"
    val = True
    for i in s:
        if len(stack) == 0:
            push(stack, i)
        else:
            if i in opening:
                push(stack, i)
            elif i in closing:
                if i == ")" and pull(stack) == "(":
                    pass
                elif i == "}" and pull(stack) == "{":
                    pass
                elif i == "]" and pull(stack) == "[":
                    pass
                else:
                    val = False
    return val




def push(stack, element):
    stack.append(element)
    return 0

def pull(stack):
    if len(stack) <= 0:
        print("\n stack underflow")
    else:
        return stack.pop()
    


isValid("(){}{[]}")