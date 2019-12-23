from typing import List


class Solution:

    def findSubstring(self, s:str, words: List[str]) -> List[int]:
        all_len = sum(map(len, words))
        if all_len > len(s):
            return []
        if len(words) == 0:
            return []
        word_len = len(words[0])
        m = {}
        result = []
        for word in words:
            if m.get(word):
                m[word] += 1
            else:
                m[word] = 1
        for i in range(0, len(s)-all_len+1):
            ss = s[i:i+all_len]
            tmp = m.copy()
            while ss:
                current = ss[:word_len]
                if current in tmp:
                    ss = ss[word_len:]
                    if tmp[current] == 1:
                        tmp.pop(current)
                    else:
                        tmp[current] -= 1
                else:
                    break
            if ss == "" and len(tmp) == 0:
                result.append(i)
        return result

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        ss = self.allRank(words, '')
        ss = list(set(ss))
        print(ss)
        result = []
        for each in ss:
            result += self.findAll(s, each)
        return result

    def findAll(self, s, sub):
        result = []
        start = 0
        while True:
            start = s.find(sub, start)
            if start == -1:
                return result
            else:
                result.append(start)
                start += 1

    def allRank(self, words, current):
        if len(words) == 0:
            if current:
                return [current]
            else:
                return []
        result = []
        for i in range(len(words)):
            tmp = words.copy()
            tmp.remove(words[i])
            it = self.allRank(tmp, current+words[i])
            result += it
        return result


if __name__ == '__main__':
    print(Solution().findAll('spam spam spam spam', 'sp'))
    print(Solution().allRank(['1','2','3','4'], ''))
    print(Solution().findSubstring('barfoothefoobarman', ["foo","bar"]))
    print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    print(Solution().findSubstring("", []))
    print(Solution().findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel", ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]))
    print(Solution().findSubstring("ababaab",
["ab","ba","ba"]))
