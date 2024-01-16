"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flaskdb import apps

if __name__ == "__main__":
    apps.run(debug=False, host="0.0.0.0", port=8080)
