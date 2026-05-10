class Solution:

    def encode(self, strs: List[str]) -> str:
        _str = ''
        for string in strs:
            _str += str(len(string)) + '%' + string
        
        return _str

    def decode(self, s: str) -> List[str]:
        print(s)
        i, res = 0, []
        while i < len(s):
            
            j, num = i, ''
            while j < len(s) and s[j] != '%':
                num += s[j]
                j += 1
            
            num = int(num)
            start, end = j+1, j+1+num

            res.append(s[start:end])
            i = end
        
        return res