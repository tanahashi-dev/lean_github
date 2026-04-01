#!/usr/bin/env python3
"""
Simple greeting script that displays the current time and Tokyo weather.
"""

import json
import urllib.request
from datetime import datetime, timedelta


WEATHER_CODES = {
    0: "快晴 (Clear sky)",
    1: "晴れ (Mainly clear)",
    2: "一部曇り (Partly cloudy)",
    3: "曇り (Overcast)",
    45: "霧 (Fog)",
    48: "霧氷 (Rime fog)",
    51: "霧雨(弱) (Light drizzle)",
    53: "霧雨(中) (Moderate drizzle)",
    55: "霧雨(強) (Dense drizzle)",
    61: "小雨 (Slight rain)",
    63: "雨 (Moderate rain)",
    65: "大雨 (Heavy rain)",
    71: "小雪 (Slight snow)",
    73: "雪 (Moderate snow)",
    75: "大雪 (Heavy snow)",
    80: "にわか雨(弱) (Slight showers)",
    81: "にわか雨 (Moderate showers)",
    82: "にわか雨(強) (Violent showers)",
    95: "雷雨 (Thunderstorm)",
    96: "雷雨(雹あり) (Thunderstorm with hail)",
    99: "雷雨(強い雹) (Thunderstorm with heavy hail)",
}


def get_tokyo_weather():
    """Fetch current weather for Tokyo from open-meteo API."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=35.6895&longitude=139.6917"
        "&current_weather=true"
        "&timezone=Asia%2FTokyo"
    )
    with urllib.request.urlopen(url, timeout=5) as response:
        data = json.loads(response.read().decode())
    current = data["current_weather"]
    temp = current["temperature"]
    code = current["weathercode"]
    condition = WEATHER_CODES.get(code, f"天気コード {code}")
    return temp, condition


def get_tokyo_tomorrow_weather():
    """Fetch tomorrow's weather forecast for Tokyo from open-meteo API."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=35.6895&longitude=139.6917"
        "&daily=weathercode,temperature_2m_max,temperature_2m_min"
        "&timezone=Asia%2FTokyo"
    )
    with urllib.request.urlopen(url, timeout=5) as response:
        data = json.loads(response.read().decode())
    daily = data["daily"]
    # Index 0 is today, index 1 is tomorrow
    code = daily["weathercode"][1]
    temp_max = daily["temperature_2m_max"][1]
    temp_min = daily["temperature_2m_min"][1]
    condition = WEATHER_CODES.get(code, f"天気コード {code}")
    tomorrow_date = daily["time"][1]
    return tomorrow_date, temp_max, temp_min, condition


def main():
    # Get current time
    current_time = datetime.now()

    # Display greeting with current time
    print("こんにちは！ Hello!")
    print(f"現在の時刻: {current_time.strftime('%Y年%m月%d日 %H:%M:%S')}")
    print(f"Current time: {current_time.strftime('%B %d, %Y %H:%M:%S')}")

    # Display Tokyo current weather
    try:
        temp, condition = get_tokyo_weather()
        print(f"東京都の現在の天気: {condition}、気温 {temp}°C")
        print(f"Current weather in Tokyo: {condition}, {temp}°C")
    except Exception as e:
        print(f"天気情報の取得に失敗しました: {e}")

    # Display Tokyo tomorrow's weather
    try:
        tomorrow_date, temp_max, temp_min, condition = get_tokyo_tomorrow_weather()
        print(f"東京都の明日({tomorrow_date})の天気: {condition}、最高 {temp_max}°C / 最低 {temp_min}°C")
        print(f"Tomorrow's weather in Tokyo ({tomorrow_date}): {condition}, High {temp_max}°C / Low {temp_min}°C")
    except Exception as e:
        print(f"明日の天気情報の取得に失敗しました: {e}")


if __name__ == "__main__":
    main()
