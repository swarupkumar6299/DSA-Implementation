class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # 1. Build the Graph
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        # 2. Binary Lifting (LCA) Preprocessing
        LOG = n.bit_length()
        if LOG == 0: LOG = 1 # Safety for edge cases
        
        par = [[-1] * n for _ in range(LOG)]
        dep = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        
        # Convert string to integer list (0-25)
        # Note: s is immutable, so we'll convert to a list we can update logically if needed,
        # but here we just need initial values for dfs.
        # Actually, for the logic below, we need to track current values of nodes for the LCA term.
        # Let's keep a mutable list of current char values.
        current_s_vals = [ord(c) - ord('a') for c in s]
        
        timer = 0
        def dfs(u, p):
            nonlocal timer
            tin[u] = timer
            timer += 1
            par[0][u] = p
            
            # Initial prefix XOR from root
            # Use current_s_vals which has initial state
            val = 1 << current_s_vals[u]
            pref[u] = (pref[p] if p != -1 else 0) ^ val
            
            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    dfs(v, u)
            tout[u] = timer - 1
        
        dfs(0, -1)
        
        # Fill LCA table
        for k in range(1, LOG):
            for i in range(n):
                if par[k-1][i] != -1:
                    par[k][i] = par[k-1][par[k-1][i]]
        
        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            
            for k in range(LOG - 1, -1, -1):
                if par[k][u] != -1 and dep[par[k][u]] >= dep[v]:
                    u = par[k][u]
            
            if u == v:
                return u
            
            for k in range(LOG - 1, -1, -1):
                if par[k][u] != par[k][v]:
                    u = par[k][u]
                    v = par[k][v]
            
            return par[0][u]
        
        # 3. Fenwick Tree (BIT)
        # We need size n+1. tin/tout are 0-based.
        bit = [0] * (n + 1)
        
        def update_bit(i, x):
            i += 1  # 0-based to 1-based
            while i <= n:
                bit[i] ^= x
                i += i & -i
        
        def query_bit(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res
        
        # 4. Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            type_str = parts[0]
            
            if type_str[0] == 'u':  # "update"
                u = int(parts[1])
                c_char = parts[2]
                val_new = ord(c_char) - ord('a')
                val_old = current_s_vals[u]
                
                # XOR difference
                diff = (1 << val_old) ^ (1 << val_new)
                
                current_s_vals[u] = val_new  # Update local state
                
                # Apply XOR difference to subtree range [tin[u], tout[u]]
                update_bit(tin[u], diff)
                update_bit(tout[u] + 1, diff)
                
            else:  # "query"
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                
                # Current Path XOR = Current_Prefix(u) ^ Current_Prefix(v) ^ Current_Val(LCA)
                
                # Current Prefix(x) = Initial_Prefix(x) ^ Sum_Updates_Root_To(x)
                # Sum_Updates_Root_To(x) is obtained by point query on BIT at tin[x]
                # because we did Range Update on Subtree.
                
                curr_pref_u = pref[u] ^ query_bit(tin[u])
                curr_pref_v = pref[v] ^ query_bit(tin[v])
                val_w = 1 << current_s_vals[w]
                
                mask = curr_pref_u ^ curr_pref_v ^ val_w
                
                if mask == 0 or (mask & (mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans