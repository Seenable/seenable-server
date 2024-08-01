# seenable-server

## サーバーの準備

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


// 以下エラー文
// RuntimeError: Unsupported image type, must be 8bit gray or RGB image.

// 対策
pip uninstall -y numpy
python -m pip install numpy==1.26.4


// 以下エラー文
ModuleNotFoundError: No module named 'multipart'

// 対策
pip install python-multipart
```

## 顔認証の準備
### フォルダ構成
imagesフォルダがないので、appフォルダの直下にimagesフォルダを作成し、trainフォルダを作成する。
その後、そこに認証したい人の画像を入れる。
<pre>
.
├── README.md
├── app
│   ├── __init__.py
│   ├── feature
│   │   ├── db.py
│   │   └── face_recognition_summary.py
│   ├── images
│   │   └── train
│   │       └── 1.png  ＜ー　ここに認証したい人の画像を入れる。
│   └── main.py
├── docker-compose.yml
└── requirements.txt
</pre>

> [!WARNING]
> ファイル名とID名を紐づけているので、画像のファイル名は登録されているIDと同じにしてください。

### DBの準備(今回はMongoDBを使用しました)
DB作成

```
use seenable
```

テーブルの作成（コレクションの作成）
```
db.createCollection("students")
```

認証させたい人のデータを入れます
```
db.students.insert(
{
_id : '登録番号（ 例： 1 ）' ,
name : "認証したい人の名前( 例： 田中太郎 )" ,
}
)
```
