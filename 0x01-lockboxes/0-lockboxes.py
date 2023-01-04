def canUnlockAll(boxes):
    keys = []
    for box in boxes:
        keys+=box
    for i in range(len(boxes)):
        if i+1 not in keys:
            return False
    return True
