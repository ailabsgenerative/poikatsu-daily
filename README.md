# poikatsu-daily

毎日「ポイ活」の最新情報を収集し、レポートを自動生成するプロジェクトです。

## はじめに

- まずはシンプルな仕組みからスタートします
- 今後、情報源や自動化の拡張を予定しています

## ディレクトリ構成

- `/src` ... レポート生成用スクリプト
- `/data` ... 日次レポートの保存先

---

このリポジトリは [generate-blog](https://github.com/ailabsgenerative/generate-blog) をベースにしています。

---

## 自動レポート生成の仕組み

- GitHub Actions で毎日定時にワークフローが実行されます
- Gemini APIと対話し、最新の「ポイ活」情報を自動で収集・要約します
- 生成されたレポートは `/data/YYYY-MM-DD.md` として保存されます
- `index.html` には最新レポート一覧が自動で反映されます

### 開発・運用のポイント
- Gemini APIキーはGitHubリポジトリのSecretsに `GEMINI_API_KEY` として登録してください
- レポート生成ロジックは `src/generate_report.py` で管理しています
- サイトのトップページは `index.html` です

---
