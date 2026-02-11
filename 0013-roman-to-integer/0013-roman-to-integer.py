class Solution:
    def romanToInt(self, s: str) -> int:
        special_Case = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        roman_to_int = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        i = 0 
        num = 0

        while i < len(s):
            if i + 1 < len(s) and s[i] + s[i+1] in special_Case:
                c = s[i] + s[i+1]
                n = special_Case[c]
                num += n 
                i += 2
            else:
                print(roman_to_int[s[i]])
                n = roman_to_int[s[i]]
                num += n 
                i += 1
        
        
        

        return num
                
