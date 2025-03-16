from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

openaiapikey = os.getenv('OPENAIAPIKEY')



client = OpenAI(
  api_key=openaiapikey
)
command = """Happy Holi to all🎨
Happy Holi Everyone 🎨🎉🎉
Happy Holi to All✨🥳
Happy holi to all🥳😃
Happy holi to All 🥳🥳🎨
Happy holi to all🥳🥳
Happy Holi 😊☺️🎉
Happy Holi to all 🎉
Happy Holi to all"""

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "You are a person named manisha who speak hindi as well as english. He is from india and as a coder. You analize chat history and respond like harry"},
    {"role": "user", "content": command}
  ]
)

response = completion.choices[0].message.content

