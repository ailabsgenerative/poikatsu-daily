import os

import requests
try:
    import google.generativeai as genai
    from google.generativeai import types
    _HAS_GENAI = True
except ImportError:
    _HAS_GENAI = False

def generate_report_with_gemini(prompt: str, gemini_api_key: str) -> str:
    """
    Gemini APIと対話し、レポート用コンテンツを生成する（v1beta gemini-2.0-flash対応）
    grounding（Google検索ツール）有効化もサポート
    """
    # 環境変数でgrounding有効化を切り替え
    use_grounding = os.environ.get("GEMINI_GROUNDING", "false").lower() == "true"
    if use_grounding and _HAS_GENAI:
        # google-generativeaiパッケージによるgrounding生成
        client = genai.Client()
        grounding_tool = types.Tool(google_search=types.GoogleSearch())
        config = types.GenerateContentConfig(tools=[grounding_tool])
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=config,
        )
        return response.text
    else:
        # 従来のREST API
        endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        params = {"key": gemini_api_key}
        response = requests.post(endpoint, headers=headers, params=params, json=data)
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]

import datetime

if __name__ == "__main__":
    base_prompt = os.environ.get("REPORT_PROMPT", "今日のポイ活最新情報をまとめてください")
    gemini_api_key = os.environ["GEMINI_API_KEY"]
    today = datetime.date.today().strftime("%Y-%m-%d")
    # $(date +'%Y-%m-%d') の部分をシステム日付で置換
    prompt = base_prompt.replace('$(date +\'%Y-%m-%d\')', today).replace('$(date +"%Y-%m-%d")', today)
    report = generate_report_with_gemini(prompt, gemini_api_key)
    print(report)
