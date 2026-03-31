#!/usr/bin/env python3
"""
Simple greeting script that displays the current time.
"""

from datetime import datetime


def main():
    # Get current time
    current_time = datetime.now()
    
    # Display greeting with current time
    print("こんにちは！ Hello!")
    print(f"現在の時刻: {current_time.strftime('%Y年%m月%d日 %H:%M:%S')}")
    print(f"Current time: {current_time.strftime('%B %d, %Y %H:%M:%S')}")


if __name__ == "__main__":
    main()
