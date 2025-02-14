'''
source: Vamsi Bhavani YouTube Channel
Links: 
https://www.youtube.com/watch?v=Q4rmo-Stz5k&t=661s
https://openrouter.ai/docs/quickstart

Accessing the LLM Models using 'OpenAI SDK'.
API_KEY = "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"

'''

import requests
import json

API_KEY = "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"

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer "+ API_KEY,
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "deepseek/deepseek-r1:free", # Optional
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)

print(response.json())