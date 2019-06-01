# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

# You must change exactly one character in every transformation
# Each intermediate word must exist in the dictionary
# Example :

# Given:

# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note that we account for the length of the transformation path instead of the number of transformation itself.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.

########################################################################################################################################

def traverse_words(d, seen, word, end):
    # print(seen)
    if word == end:
        # print(seen)
        return len(seen)
    
    # print(seen)
    # print(len(seen))
    num = float('inf')
    for words in d[word]:
        if words not in seen:
            seen.add(words)
            num = min(num, traverse_words(d, seen, words, end))
            seen.remove(words)
    return num

class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        # print(start)
        # print(end)
        # print(dictV)
        d = {}
        dictV.append(start)
        dictV.append(end)
        for ii in range(len(dictV)):
            if dictV[ii] not in d:
                d[dictV[ii]] = set()
            for jj in range(ii + 1, len(dictV)):
                # if dictV[jj] in d:
                #     continue
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
        
        # print(d)
        seen = set([start])
        num = traverse_words(d, seen, start, end)
        if num == float('inf'):
            return 0
        return num
        
########################################################################################################################################
