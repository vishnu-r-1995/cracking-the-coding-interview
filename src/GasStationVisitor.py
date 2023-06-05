class GasStationVisitor(object):
    def canCompleteCircuit(self, gas, cost):
        if (len(gas) == 1):
            if (gas[0] >= cost[0]):
                return 0
            else:
                return -1
        net_cost = [g - c for (g, c) in zip(gas, cost)]
        for i, x in enumerate(net_cost):
            if (x > 0):
                new_list = net_cost[i : ] + net_cost[0 : i]
                gas_amt = 0
                for cnt, y in enumerate(new_list):
                    gas_amt += y
                    if (gas_amt <= 0 and cnt < len(net_cost) - 1):
                        break
                    if (cnt == len(net_cost) - 1 and gas_amt >= 0):
                        return i
        return -1
    
    #More Optimized
    def canCompleteCircuit2(self, gas, cost):
        trip_tank, curr_tank, start, n = 0, 0, 0, len(gas)
        for i in range(n):
            trip_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0 
        return start if trip_tank >= 0 else -1
