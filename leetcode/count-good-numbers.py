class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulos=1000000007
        good_pair=pow(5,ceil(n/2),modulos)*pow(4,n//2,modulos)
        return good_pair%modulos