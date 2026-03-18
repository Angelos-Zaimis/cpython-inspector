# cpython-inspector

cpython-inspector/
│
├── app/
│   ├── __init__.py
│   │
│   ├── main.py                  # FastAPI app entry point
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── bytecode.py          # /bytecode/disassemble, /bytecode/simulate
│   │   ├── ast_parser.py        # /ast/parse
│   │   └── pipeline.py          # /pipeline/full
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── compiler.py          # wraps compile() and code object extraction
│   │   ├── disassembler.py      # wraps dis module, returns structured data
│   │   ├── simulator.py         # stack simulation logic
│   │   ├── ast_service.py       # wraps ast module, returns structured tree
│   │   └── cache.py             # Redis caching logic
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── requests.py          # Pydantic input models
│   │   └── responses.py         # Pydantic output models
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── rate_limiter.py      # rate limiting middleware
│   │
│   └── core/
│       ├── __init__.py
│       ├── config.py            # settings, env variables
│       └── exceptions.py        # custom exception handlers
│
├── tests/
│   ├── __init__.py
│   ├── test_bytecode.py
│   ├── test_ast.py
│   ├── test_simulator.py
│   └── test_pipeline.py
│
├── .env                         # environment variables (never commit)
├── .env.example                 # template for env variables
├── .gitignore
├── Dockerfile
├── docker-compose.yml           # app + Redis together
├── requirements.txt
└── README.md

Flow

request
    ↓
router        # receives and validates input
    ↓
service       # business logic (compile, disassemble, simulate)
    ↓
schema        # structures and validates output
    ↓
response