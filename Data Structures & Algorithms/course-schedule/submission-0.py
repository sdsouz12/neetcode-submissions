class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisitesMap = {i:[] for i in range(numCourses)} # maps corse to prerequisites

        for courses, pre_requisites in prerequisites:
            prerequisitesMap[courses].append(pre_requisites)


        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if prerequisitesMap[course] == []:
                return True

            visited.add(course)
            for prerequisite in prerequisitesMap[course]:
                if not dfs(prerequisite): return False
            visited.remove(course)
            prerequisitesMap[course] = []
            return True

        for course in prerequisitesMap:
            if not dfs(course): return False

        return True








        