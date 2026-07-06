class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps={}
        ret = []
        for s in strs:
            indicesMap = self.buildIndices(s)
            if indicesMap in maps:
                maps[indicesMap].append(s)
            else:
                maps[indicesMap] = [s]
        print("maps", maps.items())
        for key,value in maps.items():
            ret.append(value)
        print(ret)
        return ret
            
    def buildIndices(self, s:str):
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        return tuple(count)