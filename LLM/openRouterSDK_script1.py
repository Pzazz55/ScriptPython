'''
source: Vamsi Bhavani YouTube Channel
Links: 
https://www.youtube.com/watch?v=Q4rmo-Stz5k&t=661s
https://openrouter.ai/docs/quickstart

Accessing the LLM Models using 'OpenAI SDK'.
API_KEY = "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"

'''

from openai import OpenAI

API_KEY = "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"

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY,
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)

print(completion.choices[0].message.content)