class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += "#" + str([ord(c) for c in s])
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded=[]
        delimeter='#'
        str_list = s.split(delimeter)
        for s in str_list:
            if s:
                decoded.append("".join(chr(n) for n in eval(s)))
        
        return decoded
