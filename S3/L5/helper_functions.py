import os

from openai import OpenAI
import csv
import pandas as pd 
from IPython.display import display, HTML

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai_api_key = os.getenv('OPENAI_API_KEY')

# Set up the OpenAI client with zhipuAI key
client = OpenAI(
    api_key=openai_api_key,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
) 

def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to GLM4 Flash model. The function then prints the response of the model.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = client.chat.completions.create(
            model="glm-4-flash",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        print(response)
    except TypeError as e:
        print("Error:", str(e))


def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to GLM4 Flash model. The function then saves the response of the model as
    a string.
    """
    completion = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response

def get_chat_completion(prompt, history):
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    completion = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt_with_history},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response


def display_table(data):
    df = pd.DataFrame(data)

    # Display the DataFrame as an HTML table
    display(HTML(df.to_html(index=False)))

