Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
If there are multiple such sequence of shortest length, return all of them. Refer to the example for more details.

Example :
Given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:
All words have the same length.
All words contain only lowercase alphabetic characters.

########################################################################################################################################

def traverse_words(d, seen, word, end, curr_lst, lst):
    if word == end:
        tmp = curr_lst[:]
        tmp.append(word)
        if tmp in lst:
            return lst, True
        if lst:
            if len(lst[0]) > len(tmp):
                lst = [tmp]
            elif len(lst[0]) == len(tmp):
                lst.append(tmp)
        else:
            lst.append(tmp)
        return lst

    if lst and len(lst[0]) <= len(seen):
        return lst
    curr_lst.append(word)
    for words in d[word]:
        if words not in seen:
            seen.add(words)
            lst = traverse_words(d, seen, words, end, curr_lst, lst)
            seen.remove(words)
    curr_lst.pop()
    return lst


class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        d = {}
        dictV.append(start)
        dictV.append(end)
        for ii in range(len(dictV)):
            if dictV[ii] not in d:
                d[dictV[ii]] = set()
            for jj in range(ii + 1, len(dictV)):
                num = 0
                for kk in range(len(dictV[ii])):
                    if dictV[ii][kk] != dictV[jj][kk]:
                        num += 1
                    if num > 1:
                        break
                if num == 1:
                    d[dictV[ii]].add(dictV[jj])
                    if dictV[jj] not in d:
                        d[dictV[jj]] = set()
                    d[dictV[jj]].add(dictV[ii])

        seen = set([start])
        lst = traverse_words(d, seen, start, end, [], [])
        return lst

########################################################################################################################################
