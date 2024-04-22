class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def attempt(edges,source,dest,done):
            if (source,dest) in done:
                return False
            if source==destination:
                return True
            done.add((source,dest))
            for option in edges[dest]:
                if attempt(edges,dest,option,done):
                    return True
            return False
            
        if destination==source:
            return True

        newEdges = defaultdict(list)
        for x,y in edges:
            newEdges[x].append(y)
            newEdges[y].append(x)
        
        return attempt(newEdges,-1,source,set())

