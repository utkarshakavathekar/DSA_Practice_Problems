#User function Template for python3
##################################### Infix to postfix ###########################

class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        postfix = ""
        stack = []
        for i in range(0,len(exp)):
            
            if (exp[i]>='A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z') or (exp[i]>='0' and exp[i]<='9'):
                postfix+=exp[i]
                
            elif exp[i]=='(':
                stack.append(exp[i])
            
            elif exp[i]==')':
                while len(stack)!=0 and stack[-1]!='(':
                    postfix+=stack.pop()
                if stack:  
                    stack.pop()
                
            else:
                while len(stack)!=0 and self.Prec(exp[i])<=self.Prec(stack[-1]):
                    postfix+=stack.pop()
                stack.append(exp[i])
                
        while len(stack)!=0:
            ele = stack.pop()
            postfix+=ele
        return postfix
        
    def Prec(self,char):
        if char == '^':
            return 3
        elif char=='*' or char=='/':
            return 2
        elif char=='+' or char=='-':
            return 1
        return -1
                
######################################## Postfix to infix ###############################

#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        stack = []
        for i in range(0,len(postfix)):
            
            if (postfix[i]>='a'and postfix[i]<='z') or (postfix[i]>='A'and postfix[i]<='Z') or \
                (postfix[i]>='0'and postfix[i]<='9'):
                    stack.append(postfix[i])
                    
            else:
                opr2 = stack.pop()
                opr1 = stack.pop()
                tmp = '('+opr1+postfix[i]+opr2+')'
                stack.append(tmp)
                
        return stack.pop()
