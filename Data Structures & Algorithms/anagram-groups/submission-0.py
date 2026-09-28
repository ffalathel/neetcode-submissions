class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_length = {}

        for word in strs:
            # 2. Sort the word and join it into a string to make it a valid key
            sorted_key = "".join(sorted(word))
            
            # 3. Check if this key already exists in the dictionary
            if sorted_key in dict_length:
                # If it matches an existing group, append the word to that list
                dict_length[sorted_key].append(word)
            else:
                # If it's a new group, create a new list with this word inside
                dict_length[sorted_key] = [word]
                
        # 4. Return only the values (the lists of grouped anagrams)
        return list(dict_length.values())
            
        
        
        


        
        
        
                    


                
        
        