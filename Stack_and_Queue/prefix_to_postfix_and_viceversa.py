################################# prefix to postfix ################################3

#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        stack = []
        pre_exp = pre_exp[::-1]
        for i in range(0,len(pre_exp)):
            
            
            if (pre_exp[i]>='a'and pre_exp[i]<='z') or (pre_exp[i]>='A'and pre_exp[i]<='Z') or \
                (pre_exp[i]>='0'and pre_exp[i]<='9'):
                    stack.append(pre_exp[i])
                    
            else:
                opr1 = stack.pop()
                opr2 = stack.pop()
                tmp = opr1+opr2 +pre_exp[i]
                stack.append(tmp)
                
        return stack.pop()

################################## postfix to prefix ################################
#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        stack = []
        
        for i in range(0,len(post_exp)):
            
            
            if (post_exp[i]>='a'and post_exp[i]<='z') or (post_exp[i]>='A'and post_exp[i]<='Z') or \
                (post_exp[i]>='0'and post_exp[i]<='9'):
                    stack.append(post_exp[i])
                    
            else:
                opr1 = stack.pop()
                opr2 = stack.pop()
                tmp = post_exp[i]+opr2 +opr1 
                stack.append(tmp)
        return stack.pop()