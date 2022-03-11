# coding: utf-8
# 参考 https://tomomai.com/python_cx_freeze/
# cx_Freeze 用セットアップファイル

import sys
from cx_Freeze import setup, Executable

base = None

# GUI=有効, CUI=無効 にする
if sys.platform == "win32":
    base = "Win32GUI"

# exe にしたい python ファイルを指定
exe = Executable(script="run.py", base=base, icon="icon.ico")

# セットアップ
setup(
    name="YouTubeDownloader",
    version="1.0",
    description="YouTubeDownloader",
    options={"build_exe": {"include_files": ["icon.png", "conf"]}},
    executables=[exe],
)
