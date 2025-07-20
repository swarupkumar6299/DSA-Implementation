class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class Node:
            __slots__=("children","dup")
            def __init__(self):
                self.children={}
                self.dup=False
        root=Node()
        for p in paths:
            cur=root
            for n in p:
                cur=cur.children.setdefault(n,Node())
        sigmap=defaultdict(list)
        def dfs(node: Node):
            if not node.children:
                return ""
            parts=[]
            for name in sorted(node.children):
                parts.append(f"{name}({dfs(node.children[name])})")
            sig="".join(parts)
            sigmap[sig].append(node)
            return sig
        dfs(root)
        for nodes in sigmap.values():
            if len(nodes)>1:
                for nd in nodes:
                    nd.dup=True
        ans=[]
        for path in paths:
            cur=root
            deleted=False
            for name in path:
                cur=cur.children[name]
                if cur.dup:
                    deleted=True
                    break
            if not deleted:
                ans.append(path)
        return ans