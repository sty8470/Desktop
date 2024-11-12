# test_valid_parenthesis.py
from valid_parenthesis import ValidParenthesis

def test_valid_simple_parentheses():
    # 간단한 올바른 괄호 조합
    parenthesis = ValidParenthesis(list("()"))
    assert parenthesis.check_valid_parenthesis() == True

def test_valid_nested_parentheses():
    # 중첩된 올바른 괄호 조합
    parenthesis = ValidParenthesis(list("{[()]}"))
    assert parenthesis.check_valid_parenthesis() == True

def test_valid_multiple_types():
    # 여러 타입의 괄호가 포함된 올바른 조합
    parenthesis = ValidParenthesis(list("([]{})"))
    assert parenthesis.check_valid_parenthesis() == True

def test_invalid_mismatched_parentheses():
    # 잘못된 괄호 조합 (괄호가 맞지 않음)
    parenthesis = ValidParenthesis(list("{(})"))
    assert parenthesis.check_valid_parenthesis() == False

def test_invalid_open_bracket_only():
    # 여는 괄호만 있는 경우
    parenthesis = ValidParenthesis(list("["))
    assert parenthesis.check_valid_parenthesis() == False

def test_invalid_close_bracket_only():
    # 닫는 괄호만 있는 경우
    parenthesis = ValidParenthesis(list("]"))
    assert parenthesis.check_valid_parenthesis() == False

def test_empty_string():
    # 빈 문자열은 유효한 괄호로 간주
    parenthesis = ValidParenthesis(list(""))
    assert parenthesis.check_valid_parenthesis() == True

def test_valid_complex_nested():
    # 복잡한 중첩 괄호 조합
    parenthesis = ValidParenthesis(list("{[({})]}"))
    assert parenthesis.check_valid_parenthesis() == True

def test_invalid_unbalanced():
    # 불균형 괄호
    parenthesis = ValidParenthesis(list("((()))]"))
    assert parenthesis.check_valid_parenthesis() == False
