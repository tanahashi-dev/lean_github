#!/usr/bin/env python3
"""
Simple greeting script that displays the current time.
"""

# Dummy

from datetime import datetime


def main():
    # Get current time
    current_time = datetime.now()
    
    # Display greeting with current time
    print("こんにちは！")
    print(f"現在の時刻: {current_time.strftime('%Y年%m月%d日 %H:%M:%S')}")


if __name__ == "__main__":
    main()
