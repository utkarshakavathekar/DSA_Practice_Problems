#  Input contains all unique numbers, were each no can be taken multiple times to form sum, combination should be unique

class Solution:
    def combinationSum(self, candidates, target):
        ans = list()
        curr_op = []
        i=0
        self.findCombinations(i,candidates,target,curr_op,ans)
        return ans
        

    def findCombinations(self,i, candidates, target, curr_op, ans):
        if i==len(candidates):
            if target == 0:
                ans.append(curr_op.copy())

            return

        if candidates[i]<=target:
            curr_op.append(candidates[i])
            print(curr_op)
            self.findCombinations(i, candidates, target-candidates[i], curr_op, ans)
            curr_op.pop()
        self.findCombinations(i+1, candidates, target, curr_op, ans)

        return
        