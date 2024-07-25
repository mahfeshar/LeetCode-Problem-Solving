class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i == \+\:
                nums.append(nums.pop() + nums.pop())
            elif i == \-\:
                firstNumber, secondNumber = nums.pop(), nums.pop()
                nums.append(secondNumber - firstNumber)
            elif i == \*\:
                nums.append(nums.pop() * nums.pop())
            elif i == \/\:
                firstNumber, secondNumber = nums.pop(), nums.pop()
                nums.append(int(secondNumber / firstNumber))
            else:
                nums.append(int(i))

        return(nums.pop())