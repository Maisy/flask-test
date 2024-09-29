https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html

---

```
C:\project>mkdir maisy-python

C:\project>cd maisy-python

C:\project\maisy-python>virtualenv venv
'virtualenv'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.

C:\project\maisy-python>pip install virtualenv
Collecting virtualenv
Downloading virtualenv-20.26.3-py3-none-any.whl.metadata (4.5 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv)

(venv-maisy) C:\project>python --version
Python 3.11.6


(venv-maisy) C:\project> python run.py


(venv-maisy) C:\project> deactivate
```

---

24/09/29

## windows에서 rabbitmq 설치/테스트

rabbitmq - erlang 지원 버전 확인
https://www.rabbitmq.com/docs/which-erlang
-> 26.2.x 까지 지원

erlang 26.2.x 최신버전 다운로드
https://www.erlang.org/patches/otp-26.2.5.3
(download windows installer)

rabiitmq install
https://github.com/rabbitmq/rabbitmq-server/releases
rabbitmq-server-4.0.2.exe

### 환경 변수 설정

- 시작 -> 제어판 -> 시스템 -> 고급 시스템 설정 -> 환경 변수
- 시스템 변수 중 Path를 선택하고 편집을 클릭한 후, Erlang 설치 경로(C:\Program Files\erl{version}\bin)를 추가
- RabbitMQ 실행 파일 경로(C:\Program Files\RabbitMQ Server\rabbitmq_server-{version}\sbin)를 환경 변수 Path에 추가

### Erlang 쿠키 동기화

Erlang 쿠키는 RabbitMQ 노드와 클라이언트 간의 인증을 위한 파일입니다. 두 위치에서 쿠키가 일치해야 합니다.
C:\Users\{YourUser}\.erlang.cookie 복사하여
C:\Windows\.erlang.cookie 붙여넣기

### rqbbitmq start / stop / management console시작

```bash
rabbitmq-service.bat start

rabbitmq-plugins.bat enable rabbitmq_management
## login: guest/guest


rabbitmq-service.bat stop
```
