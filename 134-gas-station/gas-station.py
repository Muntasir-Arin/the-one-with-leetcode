class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        
        idx = -1
        total = 0
        for i in range(len(cost)):
            if total==0 and (gas[i]-cost[i])>=0:
                total+=(gas[i]-cost[i])
                idx=i
            elif total+(gas[i]-cost[i])>=0:
                total+=(gas[i]-cost[i])
            else:
                total=0

        return idx