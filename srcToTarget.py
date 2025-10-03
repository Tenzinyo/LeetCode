class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # backtracking and using dfs all possible paths
        self.graph = collections.defaultdict(list)
        res = []

        for i,v in enumerate(graph):
            self.graph[i] = v

        def dfs(path,node):
            if node == len(graph)-1:
                res.append(list(path))
                
            
            for c in self.graph[node]:
                path.append(c)
                dfs(path,c)
                path.pop()
        dfs([0],0)
        return res
    
   