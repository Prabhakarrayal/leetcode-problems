class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        
        rem = cnt[:]

        i = 0
        while i < n:
            x = ord(target[i]) - ord('a')

            if rem[x] == 0:
                break

            rem[x] -= 1
            i += 1

       
        pos = i if i < n else n - 1

        while pos >= 0:
            x = ord(target[pos]) - ord('a')

           
            if pos < i:
                rem[x] += 1

           
            for c in range(x + 1, 26):
                if rem[c] > 0:
                    rem[c] -= 1

                    
                    ans = target[:pos] + chr(c + ord('a'))

                   
                    for j in range(26):
                        if rem[j]:
                            ans += chr(j + ord('a')) * rem[j]

                    return ans

            pos -= 1

        return ""