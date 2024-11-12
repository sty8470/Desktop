"""
Valid Parenthesis 문제를 푸시오: 
가장 많이 나오는 빈출 유형에 대해서 대비한다.

"""

from typing import List, Tuple, Set

class ValidParenthesis:
    def __init__(self, parenthesis: List[str]):
        self.parenthesis = parenthesis  # 입력 문자열을 인스턴스 변수로 저장

    def check_valid_parenthesis(self) -> int:
        stack = []
        lookup = {"}": "{", "]": "[", ")": "("}
        
        for p in self.parenthesis:
            # 열린 괄호 먼저 처리하기 
            if p in lookup.values():
                stack.append(p)
            
            # 닫힌 괄호 후속 처리하기
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

