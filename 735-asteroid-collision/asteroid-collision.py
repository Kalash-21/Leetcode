class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l = []

        for a in asteroids:
            alive = True

            while alive and l and l[-1] > 0 and a < 0:
                if l[-1] < abs(a):
                    l.pop()
                elif l[-1] == abs(a):
                    l.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                l.append(a)

        return l