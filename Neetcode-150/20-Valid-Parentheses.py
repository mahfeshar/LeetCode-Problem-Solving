class Solution:
    def isValid(self, s: str) -> bool:
        # s = \()[]{}\
        if len(s) % 2 == 1:
            return(False)
        stack = []
        for i in s:
            if i == \(\ or i == \[\ or i == \{\:
                print(i, \added to stack\)
                print(ord(i))
                stack.append(i)
            else:
                if stack:
                    print(i, \we have\)
                    print(ord(i) - 2)
                    if ((i == \}\ or i == \]\) and ord(i) - 2 == ord(stack.pop())) \\
                    or (i == \)\ and ord(i) - 1 == ord(stack.pop())):
                        continue
                    else:
                        return(False)
                else:
                    return(False)
        if stack:
            return(False)
        return(True)
