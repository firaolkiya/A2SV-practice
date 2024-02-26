class Solution:
    def myPow(self, x: float, n: int) -> float:
        print("state: ",x,n)
        if n<0:
            x=1/x
            n=-n
        if n==0:
            return 1
        result=self.myPow(x,n//2)
        result=result**2
        if n%2!=0:
            result*=x
        print("result: ",result)
        return result