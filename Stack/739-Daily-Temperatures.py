class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque([])
        res = [0] * len(temperatures)

        for index, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                stack_ind = stack.pop()
                res[stack_ind] = index - stack_ind
            stack.append(index)

        return res


"""
Approach: Monotomic stack

While traversing the arr, compare every element with the top of the stack, if top of the stack lesser
than the current element pop the element and add the difference in indices to result array. If top is greater
than curr element add it to the stack. The elements of the stack will be decreasing (ie monotomic).

"""