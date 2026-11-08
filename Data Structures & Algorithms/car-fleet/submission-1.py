class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for p, s in cars:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)
            # if time <= stack[-1] -> stuck at the same position

        return len(stack)


# Summary
# time = (target - position)/speed -> time need to reach the target
# zip = [] make it pair in parallel
## condition
# if the arrival time collide before target -> car fleet
# start from the latest position fist // reverse order & sorted positions
# if arrival time a car behind < front -> another car fleet, that car will never catched up with the front