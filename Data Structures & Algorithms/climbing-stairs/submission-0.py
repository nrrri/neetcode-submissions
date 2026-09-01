class Solution:
    def climbStairs(self, n: int) -> int:
        # SOLUTION 1
        # use dfs
        # left = +1
        # right = +2

        # def dfs(node):
        #     if node >= n:
        #         return node == n
        #     return dfs(node + 1) + dfs(node + 2)

        # return dfs(0)

        # SOLUTION 2 
        # we can also do fibonocci -> bottom-up

        one,two = 1,1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one 


        """ 
        n = 5
        1*5 + 2*0 -> n=1
        1*3 + 2*1 -> n=4
        1*1 + 2*2 -> n=3 -> 1,2,2 | 2,1,2 | 2,2,1
        output = 8

            0
            /\
            1     2
        /\     /\
        2 3    3 4
        /\ /\  /\  /\
        3 4 4 5 4 5 5 6
        /\ /\/\  /\
        4 5565 6 5 6
        /\
        5 6
        """

