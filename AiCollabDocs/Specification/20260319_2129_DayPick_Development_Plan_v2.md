# DayPick - 개발 계획서 v2

문서작성자: 허창원  
AI 지원: Claude Code Assistant  
작성일: 2026-03-19  
버전: v2 (배포 정보 및 개발 체계 추가)

---

## 1. 프로젝트 개요

### 1.1 앱 이름
**DayPick** - 날짜 선택 및 클립보드 복사 웹앱

### 1.2 목적
오늘 날짜 기준 2주(14일) 이전까지의 날짜 목록을 표시하고,
원하는 날짜를 탭하면 지정된 형식으로 클립보드에 복사하는 간편 도구.

### 1.3 복사 형식
```
2026-03-19(목)
```
- `년-월-일(요일)` + 마지막 공백 1개 포함
- 요일은 한국어 한 글자 (월, 화, 수, 목, 금, 토, 일)

---

## 2. 기술 스택

| 항목 | 선택 |
|------|------|
| 프론트엔드 | HTML + CSS + JavaScript (Vanilla) |
| 앱 형태 | PWA (Progressive Web App) |
| 호스팅 | GitHub Pages |
| 빌드 도구 | 없음 (빌드 불필요) |

---

## 3. 저장소 및 경로 정보

### 3.1 GitHub 저장소
- **Repository**: https://github.com/cwheo/Pages-WebApp.git
- **SSH**: `git@github.com:cwheo/Pages-WebApp.git`
- **GitHub 계정**: cwheo
- **배포 URL**: `https://cwheo.github.io/Pages-WebApp/DayPick/`

### 3.2 로컬 개발 경로
- **프로젝트 루트**: `D:\Work_Claude\2026\03\DayPick`
- **웹앱 결과물**: `D:\Work_Claude\2026\03\DayPick\DayPick\`
- **개발 문서**: `D:\Work_Claude\2026\03\DayPick\AiCollabDocs\Specification\`

### 3.3 배포 파일 구조
```
DayPick/                    # 웹앱 결과물 (GitHub Pages 배포 대상)
├── index.html              # 메인 앱 (HTML + CSS + JS 통합)
├── manifest.json           # PWA 매니페스트 (앱 이름, 아이콘, 테마)
├── sw.js                   # Service Worker (오프라인 캐시)
└── icons/
    ├── icon-192.png        # 앱 아이콘 192x192
    └── icon-512.png        # 앱 아이콘 512x512
```

---

## 4. 기능 명세

### 4.1 날짜 목록 표시
- 오늘 날짜부터 14일 전까지 총 **15개 날짜** 표시 (오늘 포함)
- 정렬: 오늘이 맨 위, 과거로 갈수록 아래
- 각 항목에 표시되는 텍스트: `2026-03-19(목)`

### 4.2 날짜 강조 및 색상 구분
| 구분 | 스타일 |
|------|--------|
| **오늘** | 배경색 강조 (파란색 계열), 굵은 글씨 |
| **토요일** | 텍스트 파란색 |
| **일요일** | 텍스트 빨간색 |
| **평일(과거)** | 기본 색상 |

### 4.3 클립보드 복사
- 날짜 항목 탭(클릭) → 클립보드에 복사
- 복사 문자열: `2026-03-19(목) ` (끝에 공백 1개)
- 복사 후 토스트 메시지: `"2026-03-19(목) 복사되었습니다"` (약 2초 표시)
- Clipboard API (`navigator.clipboard.writeText`) 사용

### 4.4 PWA 기능
- **홈 화면 추가**: Chrome에서 "홈 화면에 추가" 가능
- **오프라인 동작**: Service Worker로 정적 파일 캐싱
- **앱 모드**: `manifest.json`의 `display: "standalone"` 설정으로 주소창 없이 실행

---

## 5. UI 디자인

### 5.1 테마 색상
| 요소 | 색상 |
|------|------|
| 테마 색상 (상태바) | `#1976D2` (Material Blue 700) |
| 배경색 | `#F5F5F5` (밝은 회색) |
| 오늘 강조 배경 | `#E3F2FD` (연한 파란색) |
| 오늘 강조 좌측 보더 | `#1976D2` (파란색) |
| 토요일 텍스트 | `#1565C0` (파란색) |
| 일요일 텍스트 | `#D32F2F` (빨간색) |
| 토스트 배경 | `#323232` (진한 회색) |

### 5.2 레이아웃
```
┌─────────────────────────┐
│      DayPick            │  ← 헤더 (테마 색상 배경)
├─────────────────────────┤
│ ▶ 2026-03-19(목)  오늘  │  ← 오늘 강조 (파란 배경)
│   2026-03-18(수)        │
│   2026-03-17(화)        │
│   2026-03-16(월)        │
│   2026-03-15(일)        │  ← 빨간색 텍스트
│   2026-03-14(토)        │  ← 파란색 텍스트
│   2026-03-13(금)        │
│   ...                   │
│   2026-03-05(목)        │
├─────────────────────────┤
│  ✓ 복사되었습니다       │  ← 토스트 (하단, 2초 후 사라짐)
└─────────────────────────┘
```

### 5.3 앱 아이콘
- 달력 모양 아이콘
- 파란색(`#1976D2`) 배경에 흰색 날짜 숫자
- SVG로 생성 후 PNG 변환 (또는 직접 PNG 제작)

---

## 6. 배포 방법

### 6.1 GitHub Pages 배포 절차
1. 로컬에서 `Pages-WebApp` 리포지토리 clone (SSH: `git@github.com:cwheo/Pages-WebApp.git`)
2. `DayPick/` 폴더의 결과물을 리포지토리의 `DayPick/` 경로에 복사
3. commit & push
4. Settings → Pages → Source: `main` branch, `/ (root)` 선택
5. `https://cwheo.github.io/Pages-WebApp/DayPick/` 으로 접속

### 6.2 스마트폰 설치 (홈 화면 추가)
1. Chrome 브라우저로 위 URL 접속
2. 메뉴(⋮) → "홈 화면에 추가" 또는 자동 설치 배너
3. 홈 화면에 앱 아이콘 생성
4. 아이콘 탭 → 주소창 없이 앱처럼 실행

---

## 7. 개발 체계 (Agent Teams)

Claude Code Agent Teams를 구성하여 병렬 개발 진행.
모든 실행 Agent는 **Sonnet 4.6** 모델 사용.

### 7.1 Agent 구성

| Agent | 역할 | 산출물 |
|-------|------|--------|
| **Agent 1: UI Developer** | index.html 작성 (HTML + CSS + JS 통합) | `DayPick/index.html` |
| **Agent 2: PWA Engineer** | manifest.json + sw.js 작성 | `DayPick/manifest.json`, `DayPick/sw.js` |
| **Agent 3: Icon Designer** | SVG 기반 앱 아이콘 생성 | `DayPick/icons/icon-192.png`, `DayPick/icons/icon-512.png` |

### 7.2 실행 순서
1. **Agent 1, 2, 3 병렬 실행** — 각자 독립적 산출물 생성
2. **통합 검증** — 모든 Agent 완료 후 결과물 확인
3. **배포** — GitHub Pages에 push

---

## 8. 브라우저 호환성

| 기능 | Chrome (Android) | Safari (iOS) |
|------|:-:|:-:|
| Clipboard API | O | O (HTTPS 필수) |
| PWA 설치 | O | O (홈 화면 추가) |
| Service Worker | O | O |
| 오프라인 동작 | O | O |

> **참고**: GitHub Pages는 HTTPS를 기본 제공하므로 Clipboard API 사용에 문제없음.

---

## 9. 주의사항

- `manifest.json`의 `start_url`, `scope` 경로는 GitHub Pages 하위 경로(`/Pages-WebApp/DayPick/`)를 고려하여 설정
- Service Worker의 캐시 경로도 동일하게 하위 경로 기준으로 설정
- 아이콘 경로는 상대 경로 사용 권장 (`icons/icon-192.png`)
