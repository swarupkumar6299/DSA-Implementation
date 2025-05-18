class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        MOD = 10**9 + 7
        all_states = []
        len_mask = 7 << (m-1)*3
      
        def bt(column):
            if column & len_mask:
                all_states.append(column)
                return
            for mask in (1, 2, 4):
                if column & mask == 0:
                    bt((column << 3) | mask)

        bt(0)

        transition_table = [[] for _ in range(len(all_states))]
        for i, column1 in enumerate(all_states):
            for j, column2 in enumerate(all_states):
                if ~(~column1 | ~column2) == 0:
                    transition_table[i].append(j)

        dp = [1] * len(all_states)
        for _ in range(n-1):
            dp = [sum(dp[i] for i in prev_columns) % MOD for prev_columns in transition_table]
        return sum(dp) % MOD