# club-fair

**동아리 박람회 · 동아리 추천 퀴즈** (충남대학교 멋쟁이사자처럼)

## 프로젝트 목적

동아리 박람회에서는 짧은 시간 안에 많은 동아리 정보를 비교해야 해서,
신입생이 자신과 맞는 동아리를 빠르게 찾기 어렵습니다.

이 프로젝트는 간단한 성향 퀴즈를 통해 탐색 시간을 줄이고,
사용자가 관심 분야에 맞는 동아리를 바로 확인할 수 있도록 돕는 것을 목표로 합니다.

## 프로젝트 설명

`club-fair`는 7문항 이진 선택 퀴즈를 기반으로 동아리를 추천하는 정적 웹 프로젝트입니다.
사용자 응답을 7자리 코드로 변환한 뒤, 등록된 동아리 코드와의 유사도를 계산해 결과를 제공합니다.

- **구현 기술**: HTML, CSS, JavaScript (Vanilla)
- **추천 로직**: `club.js` (코드 일치 → 해밍 거리 1 → 해밍 거리 2 → fallback)
- **결과 제공 방식**: `result.html?code=...` 형태로 퀴즈 결과 코드 전달

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
