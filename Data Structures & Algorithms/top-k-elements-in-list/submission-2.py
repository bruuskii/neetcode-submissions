class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_nums = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            my_nums[num] = my_nums.get(num, 0) + 1
        for n,c in my_nums.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        

        
        

                


        