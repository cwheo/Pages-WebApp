# DayPick Quick Reference

**최종 업데이트**: 2026-08-07  
**현재 버전**: v1.0.1  
**문서작성자**: 허창원  
**AI 지원**: Claude Code Assistant

---

## 1. 프로젝트 개요

### 기본 정보
- **프로젝트명**: DayPick
- **프레임워크**: HTML + CSS + JavaScript (Vanilla), PWA
- **호스팅**: GitHub Pages
- **배포 URL**: https://cwheo.github.io/Pages-WebApp/DayPick/

### 목적
- 오늘 날짜 기준 최근 N주 이전까지의 날짜를 목록으로 표시 (기본 2주, 사용자 설정 가능)
- 원하는 날짜를 탭하면 `2026-03-19(목) ` 형식으로 클립보드에 복사
- 스마트폰 홈 화면에 추가하여 앱처럼 사용

---

## 2. 최근 변경사항

### v1.0.1 (2026-08-07)
- 헤더 우측에 버전번호 표시, `sw.js` 캐시명을 버전과 동기화(`daypick-v1.0.1`)
- 표시 기간을 1~12주 중 선택하는 드롭다운 추가, 설정값은 localStorage(`daypick.weeks`)에 저장
- 폴더 구조 3중 중첩으로 재편 + 버전 변경/저장소 바로가기 스크립트 3종 추가

> 전체 릴리스 이력: [Release_History.md](DayPick_Release_History.md)

---

## 3. 프로젝트 구조

프로젝트 루트: `D:\Work_Claude\2026\03\DayPick`

```
DayPick/                                   # 프로젝트 루트
├── CLAUDE.md                              # Claude Code 지시 파일
├── README.md
├── Scripts/                               # 공통 유틸 스크립트
├── AiCollabDocs/
│   ├── 00_CommitMessage.txt
│   ├── Project_overview/
│   │   ├── DayPick_Quick_Reference.md
│   │   └── DayPick_Release_History.md
│   ├── Specification/
│   │   ├── 20260319_2106_DayPick_Development_Plan.md
│   │   └── 20260319_2129_DayPick_Development_Plan_v2.md
│   ├── 2026/03/
│   │   └── 20260319_2139_DayPick_Work_list.md
│   └── 2026/08/
│       └── 20260807_1056_DayPick_v1.0.1_Release.md
└── DayPick/                               # ★ 앱 작업 폴더 (스크립트 실행 위치)
    ├── 001_Local_Repository_Pages_OpenFolder.bat   # 로컬 배포 폴더 열기
    ├── 001_Remote_Repository_GitHub_Pages.bat      # GitHub 웹 페이지 열기
    ├── 09_ChangeVersionName.py            # 버전 일괄 변경
    ├── 11_DeployToPages.py                # GitHub Pages 배포
    └── DayPick/                           # ★ 웹앱 결과물 (배포 대상)
        ├── index.html                     # 메인 앱 (HTML + CSS + JS 통합)
        ├── manifest.json                  # PWA 매니페스트
        ├── sw.js                          # Service Worker (오프라인 캐시)
        └── icons/
            ├── icon.svg                   # 앱 아이콘 SVG 원본
            ├── icon-192.png               # 앱 아이콘 192x192
            └── icon-512.png               # 앱 아이콘 512x512
```

**주의**: `DayPick` 폴더가 3중 중첩입니다(루트 / 작업 폴더 / 배포 대상).
두 파이썬 스크립트는 `Path(__file__).parent / "DayPick"` 로 배포 대상을 찾으므로
반드시 **작업 폴더(`DayPick/`)에서 실행**합니다.

---

## 4. 핵심 기능

| 기능 | 설명 |
|------|------|
| 날짜 목록 | 오늘~N주 전 (오늘이 맨 위), 기본 2주 = 15개 |
| **표시 기간 설정** | 헤더 아래 드롭다운 — 1·2·3·4·6·8·12주 (8·15·22·29·43·57·85일) |
| **설정 저장** | localStorage 키 `daypick.weeks`, 값 없거나 목록 밖이면 기본 2주 |
| **버전 표시** | 헤더 우측 `v1.0.1` (반투명 흰색 0.72rem) |
| 복사 형식 | `2026-03-19(목) ` (끝에 공백 1개) |
| 오늘 강조 | 파란 배경(`#E3F2FD`), 좌측 보더, "오늘" 뱃지 |
| 토/일 색상 | 토요일 파란색(`#1565C0`), 일요일 빨간색(`#D32F2F`) |
| 토스트 | 복사 후 `"복사되었습니다"` 2초 표시 |
| PWA | 홈 화면 추가, 오프라인 동작, standalone 모드 |

### 화면 구성
```
┌────────────────────────────────┐
│      DayPick          v1.0.1   │  ← sticky 헤더
├────────────────────────────────┤
│ 표시 기간   [ 2주 (15일) ▼ ]   │  ← sticky 설정 바
├────────────────────────────────┤
│  2026-08-07(금)      [오늘] 📋 │
│  2026-08-06(목)             📋 │
```

---

## 5. 배포

### GitHub 저장소
- **Repository**: https://github.com/cwheo/Pages-WebApp.git
- **SSH Host**: `github-cwheo` (SSH config 별칭)
- **로컬 clone**: `D:\Temp\gh\cwheo\Pages-WebApp`
- **Pages 소스**: `main` 브랜치, `/docs` 폴더
- **배포 경로**: `docs/DayPick/`

### 저장소 바로가기 (`DayPick/` 폴더)
- `001_Local_Repository_Pages_OpenFolder.bat` — `D:\Temp\gh\cwheo\Pages-WebApp\docs\DayPick` 열기
- `001_Remote_Repository_GitHub_Pages.bat` — `https://github.com/cwheo/Pages-WebApp/tree/main/docs/DayPick` 열기

### 버전 변경 스크립트
```bash
cd DayPick                              # 작업 폴더로 이동
python 09_ChangeVersionName.py          # NEW_VERSION 수정 후 실행
python 09_ChangeVersionName.py --no-wait
```
`index.html`(APP_VERSION) · `sw.js`(CACHE_NAME) · `manifest.json`(version) 3곳 일괄 변경.
`sw.js` CACHE_NAME이 함께 바뀌어야 기존 사용자의 PWA 캐시가 폐기됩니다.

### 배포 스크립트
```bash
cd DayPick                              # 작업 폴더로 이동
python 11_DeployToPages.py              # 대화형 모드
python 11_DeployToPages.py --yes        # 확인 없이 배포
python 11_DeployToPages.py --draft      # push 없이 로컬 commit만
python 11_DeployToPages.py --no-wait    # 완료 후 자동 종료
```

### 스마트폰 설치
1. Chrome으로 https://cwheo.github.io/Pages-WebApp/DayPick/ 접속
2. 메뉴(⋮) → "홈 화면에 추가"
3. 홈 화면에서 DayPick 아이콘 실행

---

## 6. 기술 상세

### 테마 색상
| 요소 | 색상 |
|------|------|
| 테마/헤더 | `#1976D2` (Material Blue 700) |
| 배경 | `#F5F5F5` |
| 오늘 강조 배경 | `#E3F2FD` |
| 토요일 | `#1565C0` |
| 일요일 | `#D32F2F` |
| 토스트 | `#323232` |

### Service Worker
- 캐시명: `daypick-v1.0.1` (**앱 버전과 동기화** — 버전 변경 시 반드시 함께 변경)
- 전략: Cache-First (캐시 우선, 네트워크 폴백)
- 캐시 대상: `index.html`, `manifest.json`, 아이콘 파일
- 캐시명이 바뀌면 `activate` 시 이전 캐시를 삭제하여 새 버전이 배포됨

### 버전 정의 위치 (3곳)
| 파일 | 코드 | 역할 |
|------|------|------|
| `index.html` | `const APP_VERSION = '1.0.1';` | 헤더 표시 (권위) |
| `sw.js` | `const CACHE_NAME = 'daypick-v1.0.1';` | PWA 캐시 무효화 (필수) |
| `manifest.json` | `"version": "1.0.1"` | 매니페스트 메타데이터 |

### 설정 저장 (localStorage)
| 항목 | 값 |
|------|-----|
| 키 | `daypick.weeks` |
| 값 | 주간 수 문자열 (`"1"`,`"2"`,`"3"`,`"4"`,`"6"`,`"8"`,`"12"`) |
| 기본값 | `2` (2주 = 15일) |
| 폴백 | 저장소 접근 예외(시크릿 모드) 또는 허용 목록 밖 값 → 기본값 |

---

## 7. 버전 히스토리

| 버전 | 날짜 | 주요 변경 |
|------|------|----------|
| v1.0.1 | 2026-08-07 | 버전 표시 + 표시 기간 설정(localStorage) + 폴더 재편/스크립트 3종 |
| v1.0.0 | 2026-03-19 | 초기 개발 완료 - PWA 웹앱 + 배포 스크립트 |

---

## 참고 문서
- [Release History](DayPick_Release_History.md)
- [v1.0.1 릴리스 노트](../2026/08/20260807_1056_DayPick_v1.0.1_Release.md)
- [개발 계획서 v2](../Specification/20260319_2129_DayPick_Development_Plan_v2.md)

---

**문서 끝**
