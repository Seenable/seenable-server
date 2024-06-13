# seenable-server

サービスに必要なライブラリのインストールをする：
```
pip install -r requirements.txt
```

Fast　API を建てる：
```
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

エラーが起こった場合の対策：
```
// 以下エラー文
// ImportError: libGL.so.1: cannot open shared object file

// 対策
apt -y update && apt -y upgrade
apt -y install libopencv-dev
```
