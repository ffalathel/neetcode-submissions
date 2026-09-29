class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictnum = {}
        for num in nums:
            if num in dictnum:
                dictnum[num] += 1
            else:
                dictnum[num] = 1
        sorted_dict_desc = dict(sorted(dictnum.items(), key=lambda item: item[1], reverse=True))
        
        result =[]
        for x in sorted_dict_desc:
            result.append(x)
            if len(result) == k:
                return result
