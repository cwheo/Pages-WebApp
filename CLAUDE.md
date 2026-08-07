# CLAUDE.md - DayPick

This file provides guidance to Claude Code when working with the DayPick project.

## 프로젝트 정보

- **프로젝트명**: DayPick (날짜 선택 및 클립보드 복사 PWA 웹앱)
- **기술 스택**: HTML + CSS + JavaScript (Vanilla), PWA
- **호스팅**: GitHub Pages (`https://cwheo.github.io/Pages-WebApp/DayPick/`)
- **Quick Reference**: `AiCollabDocs/Project_overview/DayPick_Quick_Reference.md`

## Documentation Standards

### Korean Documents
```
문서작성자: 허창원
AI 지원: Claude Code Assistant
```

### English Documents
```
Author: Changwon Heo
AI Assistant: Claude Code Assistant
```

## Language Rule

사용자와의 대화 및 코드 주석에서 **한국어와 영어만** 사용합니다.
일본어, 중국어 등 다른 언어는 사용하지 마세요.

- 대화: 한국어 기본, 필요 시 영어 혼용
- 코드 주석: 한국어 또는 영어
- 다른 언어(일본어 등)가 절대 섞이지 않도록 주의

## 배포

### 버전 변경
```bash
cd DayPick
python 09_ChangeVersionName.py      # NEW_VERSION 수정 후 실행
```
`index.html`(APP_VERSION), `sw.js`(CACHE_NAME), `manifest.json`(version) 3곳을 일괄 변경합니다.
`sw.js`의 CACHE_NAME이 함께 바뀌어야 기존 사용자의 PWA 캐시가 폐기됩니다.

### GitHub Pages 배포
```bash
cd DayPick
python 11_DeployToPages.py          # 대화형 모드
python 11_DeployToPages.py --yes    # 확인 없이 배포
```

### 저장소 바로가기 (DayPick/ 폴더)
- `001_Local_Repository_Pages_OpenFolder.bat` — 로컬 clone의 `docs\DayPick` 열기
- `001_Remote_Repository_GitHub_Pages.bat` — GitHub 웹 페이지 열기

### 저장소 정보
- **Repository**: `cwheo/Pages-WebApp`
- **SSH Host**: `github-cwheo` (SSH config 별칭, `git@github.com` 아님)
- **로컬 clone**: `D:\Temp\gh\cwheo\Pages-WebApp`
- **Pages 소스**: `main` 브랜치, `/docs` 폴더
- **배포 경로**: `docs/DayPick/`

## 파일 구조

프로젝트 루트: `D:\Work_Claude\2026\03\DayPick`

```
DayPick/                              # 프로젝트 루트
├── CLAUDE.md
├── README.md
├── AiCollabDocs/                     # 개발 문서
├── Scripts/                          # 공통 유틸 스크립트
└── DayPick/                          # ★ 앱 작업 폴더 (스크립트 실행 위치)
    ├── 001_Local_Repository_Pages_OpenFolder.bat
    ├── 001_Remote_Repository_GitHub_Pages.bat
    ├── 09_ChangeVersionName.py       # 버전 일괄 변경
    ├── 11_DeployToPages.py           # GitHub Pages 배포
    └── DayPick/                      # ★ 웹앱 결과물 (배포 대상)
        ├── index.html                # 메인 앱 (HTML + CSS + JS 통합)
        ├── manifest.json             # PWA 매니페스트
        ├── sw.js                     # Service Worker
        └── icons/                    # 앱 아이콘
```

**주의**: `DayPick` 폴더가 3중으로 중첩됩니다(루트 / 작업 폴더 / 배포 대상).
두 파이썬 스크립트는 모두 `Path(__file__).parent / "DayPick"` 기준으로
배포 대상 폴더를 찾으므로, 반드시 **작업 폴더(`DayPick/`)에서 실행**해야 합니다.

## Quick Reference 관리 규칙 (v2.0)

### 문서 3단계 구조
| 문서 | 역할 | 내용 수준 |
|------|------|----------|
| **Quick Reference** | 현재 상태 파악용 | 최신 1개 버전만 **요약** |
| **Release_History.md** | 전체 변경 이력 | 버전별 **중간 상세** |
| **개별 Release 노트** | 릴리스 당시 기록 | **코드 레벨 상세** |

### Chat 종료 시
1. Work_list.md 작성 (상세 내용)
2. Quick Reference 업데이트 — "최근 변경사항"은 최신 1개 버전 요약만
3. Release_History.md 업데이트 — 새 버전을 최상단에 중간 상세로 추가
4. "버전 히스토리" 테이블에 한 줄 요약 추가

### 업데이트 원칙
- Quick Reference "최근 변경사항"은 최신 1개 버전 요약만 (2~3줄)
- 버전별 파일 생성 금지 (단일 파일 유지)
- 상세 코드는 Work_list.md에만 포함
