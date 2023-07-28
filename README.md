# jp-giga_oneroster_api_hub

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![OneRoster Logo](https://img.shields.io/badge/OneRoster-1.2-blue.svg)](https://www.imsglobal.org/activity/onerosterlis)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![FastAPI Version](https://img.shields.io/badge/fastapi-0.99.1-blue.svg)](https://fastapi.tiangolo.com/)

# 概要
jp_giga_oneroster_api_hubは、OneRoster CSVファイルをアップロードして、OneRoster APIを提供するPython FastAPIベースのWebアプリケーションです。このツールを使うことで、学校や教育機関は異なる教育アプリケーションとシステム間で学生や教師の情報を簡単に共有できます。

# 特徴

- OneRoster準拠のCSVファイルをアップロードしてデータを管理
- OneRoster Japan Profile に準拠した学校、教室、生徒、教師などのデータエンティティをサポート
- PythonとFastAPIを使用して高速なAPIを提供
- シンプルなデプロイメントとスケーラビリティ
- セキュリティに焦点を置いた認証とアクセス制御
# 必要要件

- Python 3.11
- pip パッケージマネージャー
- DockerとDocker Compose (オプション、Dockerでのデプロイメントの場合)

# インストール

1. リポジトリをクローンします。

```bash
git clone https://github.com/hisahonakata/jp-giga_oneroster_api_hub
cd jp-giga_oneroster_api_hub
```

2. Docker コンテナを構築します。

```bash
docker compose build
```

# 使い方

1.  Docker コンテナを起動します。

```bash
docker compose up
```

2. ブラウザで以下のURLにアクセスします。

```
http://localhost:8000
```

Swagger UI が表示され、APIのエンドポイントのテストができます。
# Author

* Hisaho Nakata

# ライセンス
 
このプロジェクトはMITライセンスの下で提供されています。 詳細は[MIT license](https://en.wikipedia.org/wiki/MIT_License)をご参照ください。

# 貢献
バグの報告や新機能の提案、プルリクエストは歓迎します！貢献する前に、 [CONTRIBUTING ガイドライン](https://docs.github.com/ja/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)を確認してください。

# 作者
* Hisaho Nakata
* hisaho.nakata@outlook.com

# クレジット
このプロジェクトは FastAPI フレームワークを使用しています。感謝の意を表します。
