#!/usr/bin/python3
""" this module is for the canunlockAll question """


def canUnlockAll(boxes):
    if not boxes or type(boxes) is not list or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not isinstance(key, int):
                return False  # Non-integer key found
            if key < 0 or key >= n:
                return False  # Key out of range
            if not visited[key] and key != current_box:
                visited[key] = True
                queue.append(key)

    return all(visited)
