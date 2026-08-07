#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DayPick 버전 변경 스크립트

이 스크립트는 DayPick 웹앱의 버전 관련 위치를 일괄 변경합니다:
  1. index.html      APP_VERSION      (권위: 헤더 우측 버전 표시)
  2. sw.js           CACHE_NAME       (권위: 'daypick-v<ver>' - PWA 캐시 무효화)
  3. manifest.json   "version"        (부수: PWA 매니페스트 메타데이터)

sw.js 의 CACHE_NAME 이 함께 바뀌어야 기존 사용자의 브라우저 캐시가 폐기되고
새 버전 파일을 내려받습니다. (버전만 올리고 캐시명을 그대로 두면 갱신 안 됨)

원본 줄바꿈(CRLF/LF)은 그대로 보존합니다.

사용법:
  python 09_ChangeVersionName.py              # 대화형 모드
  python 09_ChangeVersionName.py --no-wait    # 자동 종료

작성자: 허창원
AI 지원: Claude Code Assistant
"""

import sys
import re
from pathlib import Path
from datetime import datetime

# ==========================================
# 버전 설정 (이 부분만 수정하세요)
# ==========================================
NEW_VERSION = "1.0.1"
# ==========================================

SCRIPT_DIR = Path(__file__).parent
APP_DIR = SCRIPT_DIR / "DayPick"

INDEX_HTML = APP_DIR / "index.html"
SW_JS = APP_DIR / "sw.js"
MANIFEST_JSON = APP_DIR / "manifest.json"

SEMVER = r'\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.\-]+)?'


def read_text(path):
    # 줄바꿈 보존(newline='')·BOM 안전(utf-8-sig)
    with open(path, 'r', encoding='utf-8-sig', newline='') as f:
        return f.read()


def write_text(path, content):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)


def apply_patch(path, pattern, repl, label, required):
    """path 에서 pattern 을 repl 로 치환. (성공여부, 필수여부) 판단용 결과 반환."""
    p = path.resolve()
    if not p.exists():
        print(f"  X {label}: 파일 없음 ({p})")
        return (False, required)
    content = read_text(p)
    m = re.search(pattern, content)
    if not m:
        mark = "X" if required else "!"
        print(f"  {mark} {label}: 패턴을 찾지 못함")
        return (not required, required)
    old = m.group(0)
    new_content, n = re.subn(pattern, repl, content, count=1)
    if content == new_content:
        print(f"  = {label}: 이미 {NEW_VERSION} (변경 없음)")
        return (True, required)
    write_text(p, new_content)
    # 바뀐 값 추출(표시용)
    after = re.search(pattern, new_content)
    print(f"  V {label}: 변경 완료  ({old.strip()}  ->  {after.group(0).strip() if after else '?'})")
    return (True, required)


def show_current():
    print("-" * 60)
    print("현재 버전 정보")
    print("-" * 60)
    checks = [
        (INDEX_HTML, r"APP_VERSION\s*=\s*'([^']+)'", "index.html APP_VERSION"),
        (SW_JS, r"CACHE_NAME\s*=\s*'daypick-v([^']+)'", "sw.js CACHE_NAME"),
        (MANIFEST_JSON, r'"version"\s*:\s*"([^"]+)"', "manifest.json version"),
    ]
    for path, pat, label in checks:
        p = path.resolve()
        if not p.exists():
            print(f"  ? {label}: 파일 없음")
            continue
        m = re.search(pat, read_text(p))
        print(f"  {label}: {m.group(1) if m else '(못 찾음)'}")
    print()


def main():
    wait_exit = "--no-wait" not in sys.argv

    print("=" * 60)
    print("DayPick 버전 변경 스크립트")
    print("=" * 60)
    print(f"새 버전  : {NEW_VERSION}")
    print(f"실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    show_current()

    # (path, pattern, replacement, label, required)
    patches = [
        (INDEX_HTML,
         r"(APP_VERSION\s*=\s*')" + SEMVER + r"(')",
         r"\g<1>" + NEW_VERSION + r"\g<2>",
         "index.html APP_VERSION", True),
        (SW_JS,
         r"(CACHE_NAME\s*=\s*'daypick-v)" + SEMVER + r"(')",
         r"\g<1>" + NEW_VERSION + r"\g<2>",
         "sw.js CACHE_NAME", True),
        (MANIFEST_JSON,
         r'("version"\s*:\s*")' + SEMVER + r'(")',
         r'\g<1>' + NEW_VERSION + r'\g<2>',
         "manifest.json version", False),
    ]

    print("-" * 60)
    print("버전 변경 적용")
    print("-" * 60)

    all_required_ok = True
    for path, pat, repl, label, required in patches:
        ok, req = apply_patch(path, pat, repl, label, required)
        if req and not ok:
            all_required_ok = False

    print()
    print("=" * 60)
    if all_required_ok:
        print("V 버전 변경 완료!")
        print(f"  새 버전: {NEW_VERSION}")
        print()
        print("다음 단계:")
        print("  python 11_DeployToPages.py    # 새 버전으로 GitHub Pages 배포")
    else:
        print("X 필수 항목 변경 실패! (위 로그 확인)")
    print("=" * 60)

    if wait_exit:
        print()
        try:
            input("엔터 키를 눌러 종료하세요...")
        except Exception:
            pass

    return 0 if all_required_ok else 1


if __name__ == "__main__":
    sys.exit(main())
