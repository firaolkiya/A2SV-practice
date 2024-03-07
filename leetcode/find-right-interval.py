class Solution:
    def find(self, m, lis):
        ans = len(lis)
        left = 0
        right = ans - 1
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] == m:
                return mid
            elif lis[mid] > m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        _dict = {}
        leng = len(intervals)
        for i in range(leng):
            _dict[intervals[i][0]] = i
        value = list(_dict.keys())
        value.sort()
        ans = [0] * leng
        for i,j in intervals:
            index = self.find(j, value)
            if index == leng:
                ans[_dict[i]] = -1
            else:
                ans[_dict[i]] = _dict[value[index]]
        return ans