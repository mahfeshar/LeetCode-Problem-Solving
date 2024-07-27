class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = list(zip(position, speed))

        data.sort(key=lambda x: x[0])

        position, speed = zip(*data)

        # print(position)
        # print(speed)

        s = []
        avg = [(target - position[i]) / speed[i] for i in range(len(position))]
        # print(avg)
        for i in range(len(position)):
            while s and avg[s[-1]] <= avg[i]:
                s.pop()
            s.append(i)
        # print(s)
        return(len(s))
