import os
from glob import glob


import markdown

def generate_index_html(data_dir: str, output_path: str):
    files = sorted(glob(os.path.join(data_dir, '*.md')), reverse=True)
    items = []
    for f in files:
        date = os.path.splitext(os.path.basename(f))[0]
        with open(f, encoding='utf-8') as mdfile:
            md_content = mdfile.read()
            html_content = markdown.markdown(md_content, extensions=['extra', 'tables'])
        # 個別HTMLも生成
        report_html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ポイ活日報 {date}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <h1>ポイ活日報</h1>
    <nav>
      <a href="../index.html">ホーム</a>
    </nav>
  </header>
  <main class="markdown-body">
    <h2>{date} の日報</h2>
    {html_content}
  </main>
  <footer>
    <p>&copy; 2025 ポイ活日報</p>
  </footer>
</body>
</html>'''
        html_path = os.path.join(data_dir, f"{date}.html")
        with open(html_path, 'w', encoding='utf-8') as rf:
            rf.write(report_html)
        # index用リンク
        items.append(f'<li><a href="data/{date}.html">{date}の日報</a></li>')
    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ポイ活日報</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>ポイ活日報</h1>
    <nav>
      <a href="index.html">ホーム</a>
    </nav>
  </header>
  <main class="markdown-body">
    <h2>最新レポート一覧</h2>
    <ul>
      {''.join(items)}
    </ul>
  </main>
  <footer>
    <p>&copy; 2025 ポイ活日報</p>
  </footer>
</body>
</html>'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    generate_index_html('data', 'index.html')
