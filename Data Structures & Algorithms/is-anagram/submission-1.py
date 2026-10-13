class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        my_s, my_t = {},{}
        for char in s:
            my_s[char] = 1 + my_s.get(char, 0)
        for char in t:
            my_t[char] = 1 + my_t.get(char, 0)
        if my_s == my_t:
            return True
        return False
        
