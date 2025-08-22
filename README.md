# cat-watch (scaffold)


Windows で開発（ホットリロード）、Raspberry Pi で検証（常時稼働）を同一コードで回すための最小雛形。
* WindowsPCで開発する時にLinux環境で動作するかどうかだけ確認したい場合はDockerを使用してますが、その場合カメラの動作確認まではできません。
* Raspberry piでは今のところ動作しません。
## Quick Start


### 1) Windows (dev, hot reload)
#### 初期設定
デバイスの識別等のための環境変数を記述した.envファイルを作成してください。記述内容については.env.example を参考。
#### 実行例
```bash
copy .env.example .env
set ENV=env
pip install -r requirments.txt
uvicorn.exe app.main:app --reload --port 8000
```
Open: http://localhost:8000

#### Dockerを使う場合
```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

### 2) Raspberry Pi (prod)
```bash
cp .env.example .env
set ENV=env
pip install -r requirments.txt
uvicorn.exe app.main:app --reload --port 8000
docker compose -f docker-compose.yml -f docker-compose.pi.yml up -d --build
```
Open: http://localhost:8000
