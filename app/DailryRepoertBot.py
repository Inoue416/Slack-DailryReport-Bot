import os
import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
channel_id = os.environ['CHANNEL_ID']
LOG_FILE = './log.txt'
today: datetime = datetime.datetime.now()

try:

    send_message: str = "{}年{}月{}日\n本日の各タスクの進捗をスレッド下に記入してください\n\
```\n報告テンプレ\n①今日の活動時間\n\
○○:○○-○○:○○\n\
②活動内容\n\
・○○\n\
③次回活動予定内容\n\
・○○\n④今日のひとこと```\n".format(today.year, today.month, today.day)
    response = client.chat_postMessage(channel='#進捗報告', text=send_message)
    # assert response["message"]["text"] == "success sending message."
    with open(LOG_FILE, "a") as f:
        f.write(f"--- {today} ---\n")
        f.write(f"Sent a message: {response['message']['text']}\n\n")
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    # assert e.response["ok"] is False
    # assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    with open(LOG_FILE, "a") as f:
        f.write(f"--- {today} ---\n")
    with open(LOG_FILE, "a") as f:
        f.write(f"Got an error: {e.response['error']}" + "\n")
    # Also receive a corresponding status_code
    # assert isinstance(e.response.status_code, int)
    with open(LOG_FILE, "a") as f:
        f.write(f"Received a response status_code: {e.response.status_code}\n\n")