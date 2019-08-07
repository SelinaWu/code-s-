    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # split each string into a list of chars
        # sort each list in order
        
        anagrams = dict()
        # scan the entire word list, check if it is anagrams, save in answer
        for i in range(len(strs)):
            curr_key = ''.join(sorted(strs[i]))
            if curr_key in anagrams:
                anagrams[curr_key].append(strs[i])
            else:
                anagrams[curr_key] = [strs[i]]
                
        
        return anagrams.values()
