class Solution:

    def encode(self, strs: List[str]) -> str:
        separators = [str(len(s)) + '#' for s in strs]
        return "".join((a+b for (a,b) in zip(separators,strs)))


    def decode(self, s: str) -> List[str]:
        sep,idx,strs='', 0, []
        while idx < len(s):
            ch=s[idx]
            idx=idx+1
            if(ch=='#'):
                length=int(sep)
                sep=''
                strs.append(s[idx:idx+length])
                idx=idx+length
            else:
                sep=sep+ch;
        return strs
                



