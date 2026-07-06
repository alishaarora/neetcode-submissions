class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map1 = self.buildmap(s)
        print("map1",map)
        map2 = self.buildmap(t)
        print("map2",map)
        if map1 == map2:
            return True
        return False

    def buildmap(self, s: str) -> map:
        map={}
        for ch in s:
            if ch in map:
                map[ch] = map[ch]+1
            else:
                map[ch] = 1
        return map