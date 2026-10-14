class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = ""
        i = 0
        for s in strs:
            encoded_word += str(len(s)) + "#" + s
        return encoded_word



    def decode(self, s: str) -> List[str]:
        current_word = ""
        res , i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            deli = int(str(s[i:j]))
            j+=1
            current_word=s[j:j+deli]
            res.append(current_word)
            i = j + deli
        return res


