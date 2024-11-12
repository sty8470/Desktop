prev_sonatus
프로젝트 개요
prev_sonatus는 Sonatus Systems Test Engineer 면접 준비를 위해 작성된 프로젝트입니다. 이 저장소는 면접 준비 과정에서 연습한 Python 코드와 테스트 케이스, CI/CD 자동화를 포함하고 있습니다. GitHub Actions를 사용하여 테스트 코드가 푸시될 때마다 자동으로 실행되도록 설정하여 코드 품질을 유지하고 있습니다.

주요 기능
Python 알고리즘 문제 풀이 및 테스트 코드
GitHub Actions를 통한 CI/CD 파이프라인 구성
pytest를 이용한 테스트 자동화
파일 구조
bash
Copy code
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
설치 방법
이 저장소를 클론합니다:

bash
Copy code
git clone https://github.com/sty8470/prev_sonatus.git
cd prev_sonatus
필요한 Python 패키지를 설치합니다 (Python 3.8+ 권장):

bash
Copy code
pip install -r requirements.txt
pytest를 사용하여 테스트 코드를 실행할 수 있습니다:

bash
Copy code
pytest
사용 방법
예제: 유효한 괄호 검사
valid_parenthesis.py 파일에서 제공하는 함수는 문자열이 올바른 괄호 조합을 이루고 있는지 확인합니다.

예제 코드
python
Copy code
from src.valid_parenthesis import is_valid

print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
CI/CD 파이프라인 설정
이 프로젝트는 GitHub Actions를 통해 CI/CD가 구성되어 있습니다. 코드가 푸시되면 pytest 테스트가 자동으로 실행됩니다. CI/CD 설정 파일은 .github/workflows/ci.yml에 위치해 있습니다.

기여 방법
기여를 환영합니다! 이 프로젝트에 기여하려면 다음 단계를 따르세요:

포크(Fork)하여 프로젝트를 복제합니다.
새로운 브랜치를 생성하여 기능을 추가합니다 (git checkout -b feature-branch).
변경 사항을 커밋하고 푸시합니다 (git commit -m "Add new feature").
Pull Request를 생성하여 변경 사항을 제출합니다.
라이선스
MIT License. 자세한 사항은 LICENSE 파일을 참조하세요.
