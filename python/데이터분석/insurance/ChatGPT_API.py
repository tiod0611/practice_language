import os
from dotenv import load_dotenv

from openai import OpenAI


load_dotenv()
API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)

def get_summarization(sentences):

    sentence = [sent for sent in sentences]

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user', 'content': f'''
{sent}
{sent}

''',
            },
        ]
    )

    return 

