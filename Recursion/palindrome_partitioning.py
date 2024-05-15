class Solution:
    def partition(self, s):
        curr_part = list()
        ans=list()
        self.palindromePartition(0,s,curr_part, ans)
        return ans


    def palindromePartition(self,idx,s,curr_part, ans):
        if idx==len(s):
            ans.append(curr_part.copy())
            return

        for i in range(idx,len(s)):
            substr = s[idx:i+1]
            if self.ispalindrome(substr):
                curr_part.append(substr)
                self.palindromePartition(i+1,s,curr_part, ans)
                curr_part.pop()

    def ispalindrome(self,substr):
        if substr==substr[::-1]:
            return True
        else:
            return False
        