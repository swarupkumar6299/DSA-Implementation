class Node:
    def __init__(self):
        self.left_child = None
        self.right_child =None
        self.left_child_max =0
        self.right_child_max =0
        self.max = 0
        self.size =0
        self.left=0
        self.right =0

class SegmentTree:
    def __init__(self,size,s):
        self.tree = [Node()]*(4*size)
        self.string = s
        print("size",size)
        self.build(1,1,size)
    def build(self,index,left,right):
        self.tree[index] = Node()
        self.tree[index].left = left
        self.tree[index].right =right
        #print("build",index,self.tree[index].left,self.tree[index].right)
        if left==right:
            self.tree[index].left_child_max =self.tree[index].right_child_max =self.tree[index].max = self.tree[index].size =1
            self.tree[index].left_child = self.tree[index].right_child = self.string[left-1]
            return
        mid = (left+right)//2
        self.build(index*2,left,mid)
        self.build(index*2+1,mid+1,right)
        self.pushup(index)

    def pushup(self,index):
        root =self.tree[index]
        left = self.tree[index*2]
        right = self.tree[index*2+1]
        self._pushup(root,left,right)
    def _pushup(self,root,left,right):
        root.left_child = left.left_child
        root.right_child = right.right_child
        root.size =  left.size + right.size
        
        root.max = max(left.max,right.max)

        root.left_child_max = left.left_child_max
        root.right_child_max = right.right_child_max

        if left.right_child == right.left_child:
            if left.left_child_max == left.size:
                root.left_child_max += right.left_child_max
            if right.right_child_max == right.size:
                root.right_child_max += left.right_child_max
            root.max = max(root.max,left.right_child_max+right.left_child_max)
    
        


    def insert(self,index,index_val,val):
        if self.tree[index].left == index_val and self.tree[index].right == index_val:
            self.tree[index].left_child = self.tree[index].right_child = val
            return 
        #print("insert",index,self.tree[index].left,self.tree[index].right,index_val,val)
        mid = (self.tree[index].left + self.tree[index].right)//2
        if index_val<=mid:
            self.insert(index*2,index_val,val)
        else:
            self.insert(index*2+1,index_val,val)

        self.pushup(index)
    def query(self,index):
        return self.tree[index].max
    
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        result = []
        length = len(s)
        segmentTree = SegmentTree(length,s)
        for i , ch  in enumerate(queryCharacters):
            index = queryIndices[i]+1
            segmentTree.insert(1,index,ch)
            result.append(segmentTree.query(1))
        return result
        