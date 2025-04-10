class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        if(n <= 1):
            return True
        stack = [rooms[0]]
        visited = {0}
        while(stack):
            room = stack.pop()
            for key in room:
                if key in visited:
                    continue
                stack.append(rooms[key])
                visited.add(key)
        if(len(visited) == n):
            return True
        else:
            return False