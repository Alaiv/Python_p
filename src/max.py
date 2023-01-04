import collections


def maxSlidingWindow(nums, k):
    if nums is None:
        return nums

    que = collections.deque()
    res = []
    l = 0
    for i in range(len(nums)):
        while que and nums[que[-1]] < nums[i]:
            que.pop()
        que.append(i)

        if l > que[0]:
            que.popleft()

        if i >= k - 1:
            res.append(nums[que[0]])
            l += 1

    return res


nums = [1,3,-1,-3,5,3,6,7]
print(maxSlidingWindow(nums, 3))

