#!/usr/bin/python3
""" this module is for the canunlockAll question """


def canUnlockAll(boxes):

    def dfs(box, visited):
        visited[box] = True
        for key in boxes[box]:
            if not visited[key]:
                dfs(key, visited)

    n = len(boxes)
    visited = [False] * n
    dfs(0, visited)
    return all(visited)
