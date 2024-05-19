class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        bracket_hash = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i=='[' or i=='(' or i=='{':
                stack.append(i)
            else:
                if stack == []:
                    return False
                if bracket_hash[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        
        if stack==[]:
            return True
        else:
            return False
        