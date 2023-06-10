class CourseScheduler(object):
    preMap = {}
    visitSet = set()
    def canFinish(self, numCourses, prerequisites):
        if (numCourses == 1 or len(prerequisites) == 0):
            return True
        self.preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            self.preMap[course].append(pre)
        for course in range(numCourses):
            self.visitSet.clear()
            if not self.dfs(course):
                return False
        return True
    
    def dfs(self, course):
        if course in self.visitSet:
            return False
        if self.preMap[course] == []:
            return True
        self.visitSet.add(course)
        for x in self.preMap[course]:
            if not self.dfs(x):
                return False
        self.visitSet.remove(course)
        self.preMap[course] = []
        return True