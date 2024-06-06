# seenable-server

cmakeのインストール:
```
pip install cmake
```

dlibの最新版19.24.4はエラーが多発しているため、一つ古いバージョンをインストール：
```
// pip install dlib
pip install dlib==19.24.2
```

face-recognitionのインストール：
```
pip install face-recognition
```

mongoDBをPythonから操作するためにインストール：
```
pip install pymongo
```

FastAPIを使用するためにインストール:
```
pip install fastapi
```

FastAPI
```
uvicorn main:app --reload

// 上記コマンドでエラーが出た場合、以下のコマンドでライブラリをインストールしてみてください！
// pip install "uvicorn[standard]"
```
