# Copy-ExportChatCmd.py
# Export Chat 명령어를 클립보드에 복사
# Usage: python Copy-ExportChatCmd.py

from datetime import datetime
import subprocess
import os

# ============================================
# Configuration - Modify this for your project
# ============================================
PROJECT_NAME = "Template"
# ============================================

# ANSI color codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Enable ANSI colors on Windows
os.system("")

# Get current timestamp
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
timestamp = now.strftime("%Y%m%d_%H%M")

# Create directory path
doc_path = f".\\AiCollabDocs\\{year}\\{month}"

# Generate export path
export_path = f"{doc_path}\\{timestamp}_{PROJECT_NAME}_Chat.txt"

# Output the command to execute in Claude Code
print()
print(f"{CYAN}Run this command in Claude Code:{RESET}")
print(f"{YELLOW}/export {export_path}{RESET}")
print()

# Copy to clipboard
command = f"/export {export_path}"
subprocess.run(['clip'], input=command.encode('utf-8'), check=True)
print(f"{GREEN}Command copied to clipboard!{RESET}")
