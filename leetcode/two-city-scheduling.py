class Solution:
    def sort(self,array):
        for i in range(len(array)):
            index=i
            for j in range(i,len(array)):
                if abs(array[j][1]-array[j][0])>abs(array[index][1]-array[index][0]):
                    index=j
            array[index],array[i]=array[i],array[index]
        return array

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        array = self.sort(costs)
        cityA=0
        cityB=0
        totalCost=0
        maxP=len(costs)//2
        for city in array:
            if city[0]<=city[1] and cityA<maxP:
                totalCost+=city[0]
                cityA+=1
            elif city[0]>city[1] and cityB<maxP:
                totalCost+=city[1]
                cityB+=1
            elif cityA>=maxP:
                totalCost+=city[1]
                cityB+=1
            else:
                totalCost+=city[0]
                cityA+=1
        return totalCost
