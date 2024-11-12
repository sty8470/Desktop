# prev_sonatus

## 프로젝트 개요
**prev_sonatus**는 Sonatus Systems Test Engineer 면접 준비를 위해 작성된 프로젝트입니다. 이 저장소는 면접 준비 과정에서 연습한 Python 코드와 테스트 케이스, CI/CD 자동화를 포함하고 있습니다. GitHub Actions를 사용하여 테스트 코드가 푸시될 때마다 자동으로 실행되도록 설정하여 코드 품질을 유지하고 있습니다.

## 주요 기능
- Python 알고리즘 문제 풀이 및 테스트 코드
- GitHub Actions를 통한 CI/CD 파이프라인 구성
- `pytest`를 이용한 테스트 자동화

## 파일 구조

<pre>
prev_sonatus/
├── src/                 # 주요 코드 파일
│   ├── valid_parenthesis.py     # 괄호 유효성 검사 코드
│   └── 1_freq.py                # 가장 자주 등장하는 단어를 찾는 코드
├── tests/               # 테스트 코드
│   ├── test_valid_parenthesis.py    # valid_parenthesis.py에 대한 테스트 코드
│   └── test_freq.py                 # 1_freq.py에 대한 테스트 코드
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions 워크플로 설정 파일
└── README.md            # 프로젝트 설명 파일
</pre>

## 설치 방법

1. 이 저장소를 클론합니다:

    ```bash
    git clone https://github.com/sty8470/prev_sonatus.git
    cd prev_sonatus
    ```

2. 필요한 Python 패키지를 설치합니다 (Python 3.8+ 권장):

    ```bash
    pip install -r requirements.txt
    ```

3. `pytest`를 사용하여 테스트 코드를 실행할 수 있습니다:

    ```bash
    pytest
    ```

## 사용 방법
### 예제: 유효한 괄호 검사
`valid_parenthesis.py` 파일에서 제공하는 함수는 문자열이 올바른 괄호 조합을 이루고 있는지 확인합니다.

#### 예제 코드
```python
from src.valid_parenthesis import is_valid

print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
