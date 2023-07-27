class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = dict()
        for idx, i in enumerate(nums):
            if (target-i) in idxs:
                return [idxs[target-i], idx]
            idxs[i] = idx
        return []
