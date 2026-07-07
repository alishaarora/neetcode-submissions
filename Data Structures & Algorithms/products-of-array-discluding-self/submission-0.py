class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]*len(nums)
        suff=[1]*len(nums)
        idx=1
        while idx < len(nums):
            pref[idx] = pref[idx-1] * nums[idx-1]
            idx+=1
        for idx in range(len(suff)-2, -1, -1):
            suff[idx] = suff[idx+1] * nums[idx+1]
        print(pref,suff)
        return [a*b for (a,b) in zip(pref,suff)]