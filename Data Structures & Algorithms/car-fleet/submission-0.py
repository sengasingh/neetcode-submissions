class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([position[i], (target-position[i])/speed[i]] for i in range(len(position)))

        pace, total = -1, 0
        for i in range(len(cars)-1, -1, -1):
            pos, time = cars[i]
            if time <= pace:
                continue
            
            pace = time
            total += 1

        return total