class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:



        adj = { i:[] for i in range(n)} 
        # MAKING ADJACENCY LIST
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        count = 0
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            
            for n in adj[node]:
                dfs(n)
                
                


       
        for node in adj:
            if node not in visited:
                dfs(node)
                
                count+=1

        return count
                
            



    

                

            

        