# RabbitMQ

README 파일은 프로젝트를 이해하고 실행하는 데 필요한 정보를 간결하고 체계적으로 제공해야 합니다. 아래는 `send.py`와 `receive.py` 파일을 기반으로 RabbitMQ 메시지 송수신 프로젝트의 README 템플릿 예시입니다.

---

# RabbitMQ 메시지 송수신 프로젝트

## 📖 개요
이 프로젝트는 **RabbitMQ**를 활용하여 메시지를 송수신하는 Python 애플리케이션입니다.  
- `send.py`: 메시지를 RabbitMQ 큐에 전송합니다.  
- `receive.py`: RabbitMQ 큐에서 메시지를 수신하고 출력합니다.

---

## 🛠️ 주요 기능
- **메시지 전송**: 사용자가 입력한 메시지를 RabbitMQ 큐에 저장합니다.
- **메시지 수신**: 큐에 저장된 메시지를 실시간으로 수신하고 출력합니다.

---

## 📋 파일 설명

### 1. `send.py` (메시지 전송)
- 사용자로부터 메시지를 입력받아 RabbitMQ 큐에 전송합니다.
- `'exit'` 명령어를 입력하면 프로그램이 종료됩니다.

### 2. `receive.py` (메시지 수신)
- RabbitMQ 큐에서 메시지를 실시간으로 수신하여 출력합니다.
- `CTRL+C`를 눌러 프로그램을 종료할 수 있습니다.

---

## 🚀 설치 및 실행 방법

### 1. 사전 준비
1. **RabbitMQ 설치**
   - [RabbitMQ 공식 문서](https://www.rabbitmq.com/download.html)를 참고하여 설치하세요.
   - 설치 후 RabbitMQ 서버를 실행 상태로 유지합니다.

2. **Python 패키지 설치**
   - 이 프로젝트는 **pika** 라이브러리를 사용합니다.
   - 아래 명령어로 pika를 설치하세요:
     ```bash
     pip install pika
     ```

### 2. 실행 방법
1. **메시지 전송 프로그램 실행**
   - 터미널에서 `send.py` 파일을 실행합니다:
     ```bash
     python send.py
     ```
   - 메시지를 입력하고 Enter를 누르면 메시지가 전송됩니다.
   - `'exit'`을 입력하면 프로그램이 종료됩니다.

2. **메시지 수신 프로그램 실행**
   - 별도의 터미널에서 `receive.py` 파일을 실행합니다:
     ```bash
     python receive.py
     ```
   - 큐에 저장된 메시지가 실시간으로 출력됩니다.

---

## 💡 예제

### 1. 메시지 전송
```bash
$ python send.py
전송할 메시지를 입력하세요 (종료하려면 'exit' 입력): Hello, RabbitMQ!
메시지가 전송되었습니다.
전송할 메시지를 입력하세요 (종료하려면 'exit' 입력): exit
```

### 2. 메시지 수신
```bash
$ python receive.py
메시지를 기다리는 중입니다. 종료하려면 CTRL+C를 누르세요.
받은 메시지: Hello, RabbitMQ!
```

---

## 🔧 추가 개선 사항
- **환경 변수 사용**: RabbitMQ 서버 주소, 포트 등을 환경 변수로 관리하여 유연성을 높일 수 있습니다.
- **보안 강화**: 인증 및 암호화를 통해 보안을 강화할 수 있습니다.
- **에러 처리**: 네트워크 연결 실패나 큐 선언 오류에 대한 예외 처리를 추가할 수 있습니다.

---

## 📜 라이선스
이 프로젝트는 [MIT 라이선스](https://opensource.org/licenses/MIT)를 따릅니다.

---

위 템플릿을 기반으로 README 파일을 작성하면, 프로젝트의 목적과 사용법을 명확히 전달할 수 있습니다! 😊

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/46484914/c4b3c855-2f95-440c-b306-44e8d1ca4675/receive.py
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/46484914/a10a5700-a73d-4f4b-baef-0661538c2df5/send.py

---
Perplexity로부터의 답변: pplx.ai/share
