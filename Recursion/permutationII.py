class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            print("path", path)
        for i in range(len(nums)):
            print("i =", i)
            if i > 0 and nums[i] == nums[i-1]: # since it sorted, you just need to compared with the one before
                print("cotinued:", nums[i])
                continue
            print("first_arg", nums[:i]+nums[i+1:], "second:", path+[nums[i]])
            print("res:", res)
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

    def permuteUnique2(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                print("l = ", l)
                for i in range(len(l)+1):
                    print("i:", i)
                    print("new_ans append:", l[:i]+[n]+l[i:])
                    new_ans.append(l[:i]+[n]+l[i:])
                    # the above means it can be inserted to the any index from the pervious result
                    if i<len(l) and l[i]==n:  # how to unsersatnd this condition?
                        print("break n:", n)
                        break              #handles duplication
            ans = new_ans
        return ans

class Main():
    def test1():
        s = Solution()
        result = s.permuteUnique([0,0,1])
        # print(result)
    def test2():
        s = Solution()
        result = s.permuteUnique2([2,1,2])
        print(result)
    test2()