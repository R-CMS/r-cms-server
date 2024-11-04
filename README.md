# R-CMS Server

### 실행
```shell
### cd r-cms-server/

# 가상 환경 설정 및 의존성 설치
python3 -m venv .venv 
source .venv/bin/activate
pip install -r requirement.txt

# 프로젝트 루트에 .env 생성. 아래 Environments 참조
nano .env

# 실행
python3 -m uvicorn app.main:app --reload
```

### Environments
```env
DATABASE_URL=postgresql://postgres:1234@localhost:5432/rcms
SECRET_KEY=rcmssecretkey
ACCESS_TOKEN_EXPIRE_MINUTES=300
ORIGINS=http://localhost:3000,http://r-cms
```

### 프로젝트 구조
- main.py: FastAPI 애플리케이션 진입점으로 라우터 등록, 이벤트 설정 등을 관리 `SpringbootApplication`
- api/: 각 엔드포인트를 관리하며, /api/v1/user와 같은 버전 별 라우터를 조직 `Contoller`
- core/: 앱 설정, 보안, 환경 변수, 인증, 데이터베이스 등의 설정`Configuration`
- crud/: 데이터베이스의 CRUD 작업을 처리 `Repository`
- models/: SQLAlchemy 모델을 정의하여 데이터베이스의 각 테이블을 정의 `Domain`
- schemas/: API 요청 및 응답의 타입을 검증하는 Pydantic 모델을 정의 `Dto`
- services/: 복잡한 비즈니스 로직을 위한 폴더로, 여러 CRUD 작업을 결합한 로직을 여기에 포함 `Service`

```bash
repo/r-cms-server
├── README.md
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   └── api_v1
│   │       ├── __init__.py
│   │       ├── user.py
│   │       └── product.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── crud
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   └── services
│       ├── __init__.py
│       └── some_service.py
└── user.http

```

### API 생성 방법

1. schemas 에서 dto 생성
2. crud 에서 query 작성
3. services 에서 crud 를 참조해 에서 비즈니스 로직 작성
4. api 에서 schemas 에서 정의한 요청/응답 형식으로 services 매핑

### API 테스트

- test_http 실행