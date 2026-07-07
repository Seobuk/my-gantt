#!/usr/bin/env python3
"""
WBS Gantt 실행 런처 (루트에서 더블클릭 또는 `python run.py`).

하는 일:
  1) Flask 미설치면 python/requirements.txt 로 자동 설치
  2) 브라우저를 http://127.0.0.1:5173 로 자동 오픈
  3) python/app.py 의 Flask 서버 구동 (데이터는 data/wbs.json 에 저장)

종료: 이 창에서 Ctrl+C
"""
import os
import sys
import subprocess
import threading
import webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))
PYDIR = os.path.join(ROOT, "python")
REQ = os.path.join(PYDIR, "requirements.txt")
HOST, PORT = "127.0.0.1", 5173


def ensure_flask():
    try:
        import flask  # noqa: F401
        return
    except ImportError:
        pass
    print("Flask가 없어 설치합니다 ...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", REQ])


def main():
    ensure_flask()
    # app.py 를 모듈로 불러와 Flask app 사용
    sys.path.insert(0, PYDIR)
    import app as gantt  # python/app.py

    url = "http://%s:%d/" % (HOST, PORT)
    threading.Timer(1.2, lambda: webbrowser.open(url)).start()
    print("WBS Gantt 서버 시작 → %s  (종료: Ctrl+C)" % url)
    # debug=False: 리로더로 인한 브라우저 중복 오픈/이중 구동 방지
    gantt.app.run(host=HOST, port=PORT, debug=False)


if __name__ == "__main__":
    main()
