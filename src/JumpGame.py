class JumpGame(object):
    def canJump(self, nums):
        if len(nums)==0:
            return False
        elif len(nums)==1:
            return True
        reach=nums[0]
        for i in range(0,len(nums)):
            if i>reach:
                return False
            reach=max(reach,i+nums[i])
            
        return True