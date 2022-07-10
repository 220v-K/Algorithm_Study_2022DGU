from collections import deque


def solution(bridge_length, weight, truck_weights):
    # [0] = truck's weight / [1] = the seconds when the truck on the bridge.
    truck_list = deque([[truck, 0] for truck in truck_weights])
    truck_on_bridge = deque([])

    seconds = 0
    while truck_list or truck_on_bridge:
        seconds += 1
        truck_on_bridge = deque(map(lambda x: [x[0], x[1]+1], truck_on_bridge))

        # 1초에 한 트럭밖에 못올라가니 1초에 최대 한 트럭만 나갈 수 있음
        if truck_on_bridge and truck_on_bridge[0][1] >= bridge_length:
            truck_on_bridge.popleft()

        onBridgeWeight = 0
        if truck_on_bridge:
            onBridgeWeight = sum(list(map(lambda x: x[0], truck_on_bridge)))

        if truck_list and onBridgeWeight + truck_list[0][0] <= weight:
            truck_on_bridge.append(truck_list.popleft())

    return seconds
