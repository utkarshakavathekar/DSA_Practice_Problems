class Solution:
    def subsets(self, nums):
        op = []
        ans = []
        self.findAllSubsets(nums,op,ans)
        return ans


    def findAllSubsets(self, nums, op, ans):
        if len(nums)==0:
            ans.append(op)
            return 

        op1 = op.copy()
        op2 = op.copy()
        op2.append(nums[0])
        nums = nums[1:]
        print("op1",op1,"op2",op2,"nums",nums)
        self.findAllSubsets(nums,op1,ans)
        self.findAllSubsets(nums,op2,ans)
        return 
        