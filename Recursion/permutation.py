class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, 0, len(nums) - 1, result)
        return result

    def helper(self, list_num, l, r, result_list):
        if (l == r):
            # print("base:", list_num)
            new_list = list_num[:] # We must make a copy of it, else it would be a list object
            # when the list object change, the result_list will also change.
            result_list.append(new_list)
            # print("result_list:",result_list)
        else:
            for i in range(l, r+1):
                list_num[i], list_num[l] = list_num[l], list_num[i]
                # print("list:",list_num)
                self.helper(list_num, l+1, r, result_list)
                list_num[i], list_num[l] = list_num[l], list_num[i]

class Main():
    def test():
        s = Solution()
        result = s.permute([1,2,3])
        print(result)
    test()