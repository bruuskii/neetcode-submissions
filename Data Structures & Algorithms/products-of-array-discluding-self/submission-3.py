class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1,1
        i ,j = 0,len(nums)-1
        output = [1]*len(nums)
        while i <= len(nums)-1 and j >= 0:
            if i == 0:
                output[i] *=prefix
            if j == len(nums)-1:
                output[j] *=postfix
            else:
                output[i]*=prefix
                output[j]*=postfix
            prefix *= nums[i]
            postfix *= nums[j]
            i+=1
            j-=1
        return output