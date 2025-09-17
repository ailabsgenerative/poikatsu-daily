import google.generativeai as genai
print("[Gemini][DEBUG] google-generativeai version:", genai.__version__, flush=True)
import os


import google.generativeai as genai

def generate_report_with_gemini(prompt: str, gemini_api_key: str) -> str:
    """
    Gemini APIと対話し、レポート用コンテンツを生成する（SDK経由でGoogle検索grounding有効化）
    """
    print("[Gemini][LOG] Google検索（grounding）をSDK経由で有効化して生成", flush=True)
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt, tools=[genai.tools.GoogleSearch()])
    return response.text

import datetime

import requests
    gemini_api_key = os.environ["GEMINI_API_KEY"]
    today = datetime.date.today().strftime("%Y-%m-%d")
    # $(date +'%Y-%m-%d') の部分をシステム日付で置換
    Gemini APIと対話し、レポート用コンテンツを生成する（REST APIでGoogle検索grounding有効化）
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
