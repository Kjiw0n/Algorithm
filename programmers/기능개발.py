from collections import deque

def solution(progresses, speeds):
    arr = deque(progresses)
    speeds = deque(speeds)
    ans = []

    while arr and arr[0] < 100:
        arr = deque([a + s for a, s in zip(arr, speeds)])

        for i in range(len(arr)):
            if i == len(arr) - 1 and arr[i] >= 100:
                ans.append(i + 1)
            if arr[i] < 100:
                if i > 0:
                    ans.append(i)
                for _ in range(i):
                    arr.popleft()
                    speeds.popleft()
                break

    return ans