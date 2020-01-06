from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = dict()
        for s in strs:
            l = list(s)
            l.sort()
            t = ''.join(l)
            if t in m:
                m[t].append(s)
            else:
                m[t] = [s]
        return [v for k,v in m.items()]


if __name__ == '__main__':
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(s))
