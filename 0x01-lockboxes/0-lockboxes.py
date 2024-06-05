#!/usr/bin/python3
""" this module is for the canunlockAll question """


def canUnlockAll(boxes):
""" main function"""
    num_of_boxes = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box = unseen_boxes.pop()
        if not box or box >= n or box < 0:
            continue
        if box not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box])
            seen_boxes.add(box)
    return n == len(seen_boxes)
