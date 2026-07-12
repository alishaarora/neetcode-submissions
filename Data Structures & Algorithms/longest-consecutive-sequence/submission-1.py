class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set()
        map = {}
        longest=0
        for num in nums:
            if(num not in values):
                if num-1 in values or num+1 in values:
                    map[num] = map.get(num-1,0) + map.get(num+1,0) + 1
                    longest = max(longest, map[num])
                    if num-1 in values:
                        map[num - map[num-1]] = map[num]
                    if num+1 in values:
                        map[num + map[num+1]] = map[num]
                else:
                    map[num]=1
                    longest=max(longest,1)
            values.add(num)
        return longest