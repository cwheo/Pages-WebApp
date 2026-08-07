# DayPick

날짜 선택 및 클립보드 복사 PWA 웹앱

## 기능

- 오늘 기준 최근 N주 이전까지의 날짜를 목록으로 표시 (기본 2주)
- 표시 기간을 1·2·3·4·6·8·12주 중 선택 가능 — 설정은 브라우저 localStorage에 저장
- 날짜를 탭하면 `2026-03-19(목) ` 형식으로 클립보드에 복사
- 오늘 날짜 강조, 토요일(파란색)/일요일(빨간색) 색상 구분
- 헤더 우측에 앱 버전 표시
- PWA: 스마트폰 홈 화면에 추가하여 앱처럼 사용 가능

## 기술 스택

- HTML + CSS + JavaScript (Vanilla)
- PWA (Progressive Web App)
- 빌드 도구 없음

## 배포

GitHub Pages로 호스팅됩니다.

**URL**: https://cwheo.github.io/Pages-WebApp/DayPick/

```bash
cd DayPick                          # 작업 폴더로 이동 후 실행
python 09_ChangeVersionName.py      # 버전 일괄 변경 (배포 전)
python 11_DeployToPages.py          # 대화형 배포
python 11_DeployToPages.py --yes    # 확인 없이 배포
```

## 스마트폰 설치

1. Chrome으로 위 URL 접속
2. 메뉴(⋮) → "홈 화면에 추가"
3. 홈 화면에서 DayPick 아이콘 실행

## 폴더 구조

```
DayPick/                              # 프로젝트 루트
├── README.md
├── CLAUDE.md
├── AiCollabDocs/                     # 개발 문서
├── Scripts/                          # 공통 유틸 스크립트
└── DayPick/                          # 앱 작업 폴더 (스크립트 실행 위치)
    ├── 001_Local_Repository_Pages_OpenFolder.bat   # 로컬 배포 폴더 열기
    ├── 001_Remote_Repository_GitHub_Pages.bat      # GitHub 페이지 열기
    ├── 09_ChangeVersionName.py       # 버전 일괄 변경
    ├── 11_DeployToPages.py           # GitHub Pages 배포
    └── DayPick/                      # 웹앱 결과물 (배포 대상)
        ├── index.html                # 메인 앱 (HTML + CSS + JS 통합)
        ├── manifest.json             # PWA 매니페스트
        ├── sw.js                     # Service Worker (오프라인 캐시)
        └── icons/                    # 앱 아이콘
```

두 파이썬 스크립트는 자신이 위치한 폴더의 `DayPick/` 하위를 배포 대상으로 찾습니다.
반드시 작업 폴더(`DayPick/`)에서 실행하세요.

## 작성자

허창원
