class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 


        Sets, Sett = {}, {}


        
        for i in range(len(s)):
            Sets[s[i]] = 1 + Sets.get(s[i], 0)
            Sett[t[i]] = 1 + Sett.get(t[i], 0)
        return Sets == Sett
        
             
        

            
            
        