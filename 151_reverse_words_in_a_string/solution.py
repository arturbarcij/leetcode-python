class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0:
            return s
        
        result = []
        buffer = []
        for ch in range(len(s)-1, -1, -1):
            if s[ch] == " ":
                if buffer:
                    result.append(''.join(buffer[::-1]))
                    buffer = []
            else:
                buffer.append(s[ch])
            
        
        if buffer:
            result.append(''.join(buffer[::-1]))           
        return " ".join(result)