#!/usr/bin/env python3
"""
DayPick - GitHub Pages 배포 스크립트

DayPick PWA 웹앱을 GitHub Pages(Pages-WebApp) 저장소에 배포합니다.

사용법:
    python 11_DeployToPages.py              # 대화형 모드
    python 11_DeployToPages.py --yes        # 확인 프롬프트 건너뜀
    python 11_DeployToPages.py --draft      # git push 건너뜀 (로컬 commit만)
    python 11_DeployToPages.py --no-wait    # 완료 후 자동 종료

문서작성자: 허창원 ((주)그린파워)
AI 지원: Claude Code Assistant
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# ============================================================
# 설정
# ============================================================

# Pages 저장소 로컬 경로
PAGES_REPO_DIR = Path(r"D:\Temp\gh\cwheo\Pages-WebApp")

# Pages 저장소 SSH URL
PAGES_REPO_SSH = "git@github-cwheo:cwheo/Pages-WebApp.git"

# Pages 저장소 내 앱 폴더 (GitHub Pages source: /docs)
PAGES_APP_DIR = "docs/DayPick"

# 배포 대상 소스 폴더 (이 스크립트 기준 상대 경로)
SOURCE_DIR = Path(__file__).parent / "DayPick"

# GitHub Pages URL
PAGES_URL = "https://cwheo.github.io/Pages-WebApp/DayPick/"

# 배포 대상 파일 패턴
DEPLOY_PATTERNS = [
    "index.html",
    "manifest.json",
    "sw.js",
    "icons/icon-192.png",
    "icons/icon-512.png",
    "icons/icon.svg",
]


# ============================================================
# 유틸리티
# ============================================================

class Colors:
    """ANSI 색상 코드"""
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


def print_header(msg: str):
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'=' * 60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}  {msg}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'=' * 60}{Colors.END}")


def print_step(step: int, msg: str):
    print(f"\n{Colors.BOLD}{Colors.CYAN}[Step {step}]{Colors.END} {msg}")


def print_ok(msg: str):
    print(f"  {Colors.GREEN}✓{Colors.END} {msg}")


def print_warn(msg: str):
    print(f"  {Colors.YELLOW}⚠{Colors.END} {msg}")


def print_error(msg: str):
    print(f"  {Colors.RED}✗{Colors.END} {msg}")


def print_info(msg: str):
    print(f"  {Colors.BLUE}→{Colors.END} {msg}")


def run_git(args: list[str], cwd: Path = None) -> subprocess.CompletedProcess:
    """git 명령 실행"""
    cmd = ["git"] + args
    result = subprocess.run(
        cmd,
        cwd=cwd or PAGES_REPO_DIR,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result


def confirm_prompt(msg: str) -> bool:
    """사용자 확인 프롬프트"""
    answer = input(f"\n{Colors.YELLOW}? {msg} (y/N): {Colors.END}").strip().lower()
    return answer in ("y", "yes")


# ============================================================
# 배포 단계
# ============================================================

def check_source_files() -> list[Path]:
    """Step 1: 소스 파일 확인"""
    print_step(1, "배포 소스 파일 확인")

    if not SOURCE_DIR.exists():
        print_error(f"소스 폴더를 찾을 수 없습니다: {SOURCE_DIR}")
        return []

    print_ok(f"소스 폴더: {SOURCE_DIR}")

    files = []
    missing = []

    for pattern in DEPLOY_PATTERNS:
        filepath = SOURCE_DIR / pattern
        if filepath.exists():
            size = filepath.stat().st_size
            print_ok(f"{pattern} ({size:,} bytes)")
            files.append(filepath)
        else:
            print_error(f"{pattern} - 파일 없음")
            missing.append(pattern)

    if missing:
        print_error(f"누락 파일 {len(missing)}개: {', '.join(missing)}")
        return []

    print_info(f"배포 대상 파일: {len(files)}개")
    return files


def check_pages_repo() -> bool:
    """Step 2: Pages 저장소 확인 및 준비"""
    print_step(2, "Pages 저장소 확인")

    # git 설치 확인
    try:
        result = subprocess.run(
            ["git", "--version"], capture_output=True, text=True
        )
        print_ok(f"Git: {result.stdout.strip()}")
    except FileNotFoundError:
        print_error("git이 설치되어 있지 않습니다.")
        return False

    # 저장소 존재 확인
    if PAGES_REPO_DIR.exists() and (PAGES_REPO_DIR / ".git").exists():
        print_ok(f"Pages 저장소: {PAGES_REPO_DIR}")

        # git pull로 최신 상태 동기화
        print_info("git pull 실행 중...")
        result = run_git(["pull"])
        if result.returncode == 0:
            pull_msg = result.stdout.strip()
            if "Already up to date" in pull_msg or "Already up-to-date" in pull_msg:
                print_ok("이미 최신 상태")
            else:
                print_ok("최신 상태로 업데이트 완료")
        else:
            print_warn(f"git pull 경고: {result.stderr.strip()}")
    else:
        # 저장소 clone
        print_warn(f"Pages 저장소가 없습니다. clone합니다...")
        PAGES_REPO_DIR.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            ["git", "clone", PAGES_REPO_SSH, str(PAGES_REPO_DIR)],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if result.returncode != 0:
            print_error(f"git clone 실패: {result.stderr.strip()}")
            return False
        print_ok(f"clone 완료: {PAGES_REPO_DIR}")

    return True


def deploy_files(files: list[Path]) -> bool:
    """Step 3: 파일 복사"""
    print_step(3, "파일 배포")

    dest_dir = PAGES_REPO_DIR / PAGES_APP_DIR
    dest_icons_dir = dest_dir / "icons"

    # 대상 폴더 생성
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_icons_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    for filepath in files:
        # 소스 폴더 기준 상대 경로 유지
        rel_path = filepath.relative_to(SOURCE_DIR)
        dest_path = dest_dir / rel_path

        # 폴더 생성
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        # 파일 복사
        shutil.copy2(filepath, dest_path)
        size = dest_path.stat().st_size
        print_ok(f"{rel_path} → {dest_path.name} ({size:,} bytes)")
        copied += 1

    print_info(f"파일 {copied}개 복사 완료")
    return True


def git_commit_and_push(draft: bool = False) -> bool:
    """Step 4: git add, commit, push"""
    print_step(4, "Git 커밋 및 푸시")

    # git status 확인
    result = run_git(["status", "--porcelain", PAGES_APP_DIR])
    if not result.stdout.strip():
        print_warn("변경된 파일이 없습니다. 배포를 건너뜁니다.")
        return True

    # 변경 파일 표시
    changes = result.stdout.strip().split("\n")
    for change in changes:
        status = change[:2].strip()
        filename = change[3:].strip()
        if status in ("M", "??", "A"):
            label = {"M": "수정", "??": "추가", "A": "추가"}.get(status, status)
            print_info(f"[{label}] {filename}")

    # git add
    result = run_git(["add", PAGES_APP_DIR])
    if result.returncode != 0:
        print_error(f"git add 실패: {result.stderr.strip()}")
        return False
    print_ok("git add 완료")

    # commit 메시지
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_msg = f"Deploy DayPick PWA ({now})"

    result = run_git(["commit", "-m", commit_msg])
    if result.returncode != 0:
        print_error(f"git commit 실패: {result.stderr.strip()}")
        return False
    print_ok(f"git commit 완료: {commit_msg}")

    # push
    if draft:
        print_warn("--draft 모드: git push를 건너뜁니다.")
        return True

    print_info("git push 실행 중...")
    result = run_git(["push"])
    if result.returncode != 0:
        print_error(f"git push 실패: {result.stderr.strip()}")
        return False
    print_ok("git push 완료")

    return True


def print_result():
    """Step 5: 결과 출력"""
    print_step(5, "배포 완료")
    print()
    print(f"  {Colors.BOLD}{Colors.GREEN}배포가 완료되었습니다!{Colors.END}")
    print()
    print(f"  {Colors.BOLD}Pages URL:{Colors.END}")
    print(f"  {Colors.CYAN}{PAGES_URL}{Colors.END}")
    print()
    print(f"  {Colors.BOLD}스마트폰 설치 방법:{Colors.END}")
    print(f"  1. Chrome으로 위 URL 접속")
    print(f"  2. 메뉴(⋮) → '홈 화면에 추가'")
    print(f"  3. 홈 화면에서 DayPick 아이콘 실행")
    print()
    print(f"  {Colors.YELLOW}※ GitHub Pages 반영에 1~2분 소요될 수 있습니다.{Colors.END}")


# ============================================================
# 메인
# ============================================================

def main():
    # 인수 파싱
    args = sys.argv[1:]
    auto_yes = "--yes" in args
    draft = "--draft" in args
    no_wait = "--no-wait" in args

    print_header("DayPick - GitHub Pages 배포")
    print(f"  저장소: {PAGES_REPO_SSH}")
    print(f"  대상:   {PAGES_REPO_DIR / PAGES_APP_DIR}")
    print(f"  URL:    {PAGES_URL}")
    if draft:
        print(f"  {Colors.YELLOW}모드:   DRAFT (push 건너뜀){Colors.END}")

    # Step 1: 소스 파일 확인
    files = check_source_files()
    if not files:
        print_error("배포를 중단합니다.")
        sys.exit(1)

    # Step 2: Pages 저장소 확인
    if not check_pages_repo():
        print_error("배포를 중단합니다.")
        sys.exit(1)

    # 확인 프롬프트
    if not auto_yes:
        if not confirm_prompt("배포를 진행하시겠습니까?"):
            print_warn("배포가 취소되었습니다.")
            sys.exit(0)

    # Step 3: 파일 복사
    if not deploy_files(files):
        print_error("배포를 중단합니다.")
        sys.exit(1)

    # Step 4: git commit & push
    if not git_commit_and_push(draft=draft):
        print_error("배포를 중단합니다.")
        sys.exit(1)

    # Step 5: 결과 출력
    print_result()

    # 종료 대기
    if not no_wait:
        print()
        input(f"{Colors.CYAN}엔터를 누르면 종료합니다...{Colors.END}")


if __name__ == "__main__":
    main()
