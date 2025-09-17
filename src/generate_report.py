import os

import requests

def generate_report_with_gemini(prompt: str, gemini_api_key: str) -> str:
    """
    Gemini APIと対話し、レポート用コンテンツを生成する（v1beta gemini-2.0-flash対応）
    grounding（Google検索ツール）はREST APIのtoolsパラメータで有効化
    """
    print("[Gemini][LOG] Google検索（grounding）をREST APIで有効化して生成", flush=True)
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "tools": [{"google_search": {}}]
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
