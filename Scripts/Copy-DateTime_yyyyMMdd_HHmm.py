# Copy-DateTime_yyyyMMdd_HHmm.py
# 현재 시스템 일시를 yyyyMMdd_HHmm 형식으로 클립보드에 복사

from datetime import datetime
import subprocess

datetime_string = datetime.now().strftime("%Y%m%d_%H%M")
subprocess.run(['clip'], input=datetime_string.encode('utf-8'), check=True)

print(f"Copied to clipboard: {datetime_string}")
