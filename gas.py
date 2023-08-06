def can_complete_circuit(gas, cost):
    total_tank = 0
    current_tank = 0
    start_station = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]

        if current_tank < 0:
            start_station = i + 1
            current_tank = 0

    if total_tank < 0:
        return -1
    else:
        return start_station