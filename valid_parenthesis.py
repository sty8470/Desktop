"""
Valid Parenthesis 문제를 푸시오: 

"""

from typing import List, Tuple, Set

class ValidParenthesis:
    def __init__(self, parenthesis: List[str]):
        self.parenthesis = parenthesis  # 입력 문자열을 인스턴스 변수로 저장

    def check_valid_parenthesis(self) -> int:
        stack = []
        lookup = {"}": "{", "]": "[", ")": "("}
        
        for p in self.parenthesis:
            if p in lookup.values():
                stack.append(p)
            
            elif stack and lookup[p] == stack[-1]:
                stack.pop()
            
            else: 
                return False
        
        return stack == []
        
parenthesis = ValidParenthesis("{[()]}")
print(parenthesis.check_valid_parenthesis())  

parenthesis = ValidParenthesis("{()}")
print(parenthesis.check_valid_parenthesis())  

parenthesis = ValidParenthesis("{(})")
print(parenthesis.check_valid_parenthesis())  

