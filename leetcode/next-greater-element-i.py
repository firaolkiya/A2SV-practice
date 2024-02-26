class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        for i in range(len(nums1)):
            flag=False
            for k in range(len(nums2)):
                if flag and nums2[k]>nums1[i]:
                    nums1[i]=(nums2[k])
                    break
                elif nums1[i]==nums2[k]:
                    flag=True
            else:
                nums1[i]=-1
        return nums1
        