import os
import requests

def generate_report_with_gemini(prompt: str, gemini_api_key: str) -> str:
    """
    Gemini APIと対話し、レポート用コンテンツを生成する
    """
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    params = {"key": gemini_api_key}
    response = requests.post(endpoint, headers=headers, params=params, json=data)
    response.raise_for_status()
    result = response.json()
    # Geminiの返答からテキスト部分を抽出
    return result["candidates"][0]["content"]["parts"][0]["text"]

if __name__ == "__main__":
    prompt = os.environ.get("REPORT_PROMPT", "今日のポイ活最新情報をまとめてください")
    gemini_api_key = os.environ["GEMINI_API_KEY"]
    report = generate_report_with_gemini(prompt, gemini_api_key)
    print(report)
