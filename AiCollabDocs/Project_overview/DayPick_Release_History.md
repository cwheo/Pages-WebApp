# DayPick Release History

**프로젝트명**: DayPick  
**문서작성자**: 허창원  
**AI 지원**: Claude Code Assistant

---

## v1.0.1 (2026-08-07)

### 버전번호 표시
- 헤더 우측에 앱 버전 표시 (`v1.0.1`, 반투명 흰색 0.72rem)
- `<header>` 를 `.top-bar` 래퍼로 감싸고 sticky/box-shadow를 래퍼로 이관
  → 헤더와 설정 바가 함께 상단 고정
- 버전 정의 3곳: `index.html` APP_VERSION(권위) / `sw.js` CACHE_NAME / `manifest.json` version
- `sw.js` CACHE_NAME을 `daypick-v1` → `daypick-v1.0.1` 로 변경
  (Cache-First 전략이므로 캐시명이 바뀌어야 기존 사용자에게 새 버전이 배포됨)

### 표시 기간 사용자 설정
- 헤더 아래 sticky 설정 바에 `<select>` 드롭다운 추가
- 선택지 1·2·3·4·6·8·12주 (각 8·15·22·29·43·57·85일) — `WEEK_OPTIONS` 배열에서 생성
- 설정값을 localStorage(`daypick.weeks`)에 저장, 재방문 시 복원
- 기본값 2주로 v1.0.0 과 동일하게 동작 (기존 사용자 영향 없음)
- 방어 처리: 시크릿 모드 등 저장소 예외는 try/catch, 허용 목록 밖 값은 기본값 폴백
- `renderDates()` → `renderDates(weeks)` 로 변경, 재렌더링 시 `innerHTML = ''` 초기화

### 폴더 구조 재편
- `DayPick` 3중 중첩 구조로 변경 (루트 / 작업 폴더 / 배포 대상)
- 스크립트는 `Path(__file__).parent / "DayPick"` 기준이라 코드 수정 없이 동작
- `CLAUDE.md`, `README.md`, Quick Reference 의 경로 안내 갱신

### 신규 스크립트 3종 (LinkTurnAd 에서 이식)
- `09_ChangeVersionName.py` — index.html / sw.js / manifest.json 버전 일괄 변경
  (CRLF 보존, BOM 안전 읽기, 필수/선택 대상 구분)
- `001_Local_Repository_Pages_OpenFolder.bat` — 로컬 `docs\DayPick` 폴더 열기
- `001_Remote_Repository_GitHub_Pages.bat` — GitHub 웹 페이지 열기

### 검증
- Node.js DOM 스텁으로 인라인 스크립트 실행 검증 (7개 선택지 렌더 개수/저장/복원/폴백 전부 통과)
- 버전 스크립트 `1.0.1 → 1.0.2 → 1.0.1` 왕복 테스트, CRLF·BOM 보존 확인
- 미수행: 실제 브라우저 육안 검증 (Chrome 확장 미연결)

> [릴리스 상세](../2026/08/20260807_1056_DayPick_v1.0.1_Release.md)

---

## v1.0.0 (2026-03-19)

### 신규 개발
- PWA 웹앱 초기 개발 (HTML + CSS + JS 단일 파일)
- 날짜 목록 표시: 오늘~14일 전, 총 15개
- 클립보드 복사: `2026-03-19(목) ` 형식 (끝에 공백 포함)
- 오늘 날짜 강조, 토요일/일요일 색상 구분
- 토스트 메시지: 복사 후 2초 표시

### PWA 설정
- manifest.json: standalone 모드, 세로 고정
- Service Worker: Cache-First 전략, 오프라인 동작

### 배포
- GitHub Pages 배포 스크립트(`11_DeployToPages.py`) 작성
- `cwheo/Pages-WebApp` 저장소 `docs/DayPick/` 경로에 배포

### 앱 아이콘
- 달력 모양 SVG 아이콘 디자인
- 192x192, 512x512 PNG 생성

> [작업 내역 상세](../2026/03/20260319_2139_DayPick_Work_list.md)

---

**문서 끝**
