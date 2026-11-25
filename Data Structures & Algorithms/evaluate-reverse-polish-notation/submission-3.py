class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberstack =[]

        for ele in tokens:
            match ele:
                case '+':
                    numberstack.append(numberstack.pop() + numberstack.pop())
                case '-':
                    a,b = numberstack.pop(),numberstack.pop()
                    numberstack.append(b - a)
                case '/':
                    a,b =numberstack.pop(),numberstack.pop()
                    numberstack.append(int(b / a))
                case '*':
                    numberstack.append(int(numberstack.pop() * numberstack.pop()))
                case _:
                    numberstack.append(int(ele))

        return numberstack[0]

                
            
        
        