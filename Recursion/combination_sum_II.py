#Input does not contain unique numbers, each no can be taken only once, return all unique combinations.

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = list()
        curr_op = list()
        i=0
        self.combSum2(i, candidates, target, curr_op, ans)
        return ans

    def combSum2(self, idx, candidates, target, curr_op, ans):
        if target==0:
            ans.append(curr_op.copy())
            return

        for i in range(idx,len(candidates)):
            if i>idx and candidates[i]==candidates[i-1]:
                continue
            if candidates[i] >target:
                return

            curr_op.append(candidates[i])
            self.combSum2(i+1, candidates, target-candidates[i], curr_op, ans)
            curr_op.pop()

        return
