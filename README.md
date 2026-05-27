# club-fair

**동아리 박람회 · 동아리 추천 퀴즈** (충남대학교 멋쟁이사자처럼)

7문항 퀴즈 응답을 7자리 이진 코드로 변환한 뒤, **해밍 거리** 기반으로 맞춤 동아리를 추천하는 웹 퀴즈입니다.

- **기획**: 동아리 박람회에서 신입생이 자신에게 맞는 동아리를 빠르게 알아보기 위함
- **구현**: HTML, CSS, JavaScript (Vanilla)
- **추천 로직**: `club.js` — 코드 일치 → 해밍 거리 1 → 2 → fallback 순으로 동아리 추천

## 실행 방법

별도의 빌드나 패키지 설치 없이 브라우저에서 바로 실행할 수 있습니다.

### 1. 저장소 받기

```bash
git clone https://github.com/shushuburger/club-fair.git
cd club-fair
```

### 2. 웹 페이지 실행

**방법 A — 파일 직접 열기**

`index.html`을 브라우저로 열면 퀴즈를 시작할 수 있습니다.

**방법 B — 로컬 서버 (권장)**

폰트·리소스 로딩이 안정적이므로 로컬 서버 사용을 권장합니다.

```bash
# Python 3
python -m http.server 8000
```

브라우저에서 [http://localhost:8000](http://localhost:8000) 으로 접속합니다.

### 3. 사용 흐름

1. `index.html` — 메인 · 7문항 퀴즈
2. 퀴즈 완료 후 `result.html?code=...` — 추천 동아리 결과
3. `about.html` — 멋쟁이사자처럼 소개 페이지

### 4. (선택) 추첨 스크립트 실행

`result.py`는 로컬 참가자 파일을 읽어 추첨합니다.

```bash
python result.py
```

- 실제 데이터는 `participants.local.txt`에 작성하세요. (git 추적 제외)
- 저장소에는 예시 파일 `participants.example.txt`만 포함됩니다.
