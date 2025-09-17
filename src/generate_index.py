import os
from glob import glob

def generate_index_html(data_dir: str, output_path: str):
    files = sorted(glob(os.path.join(data_dir, '*.md')), reverse=True)
    items = []
    for f in files:
        date = os.path.splitext(os.path.basename(f))[0]
        items.append(f'<li><a href="data/{date}.md">{date}の日報</a></li>')
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
