#import gradio as gr
import os

from openai import OpenAI
from dotenv import load_dotenv
import csv
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai_api_key = os.getenv('OPENAI_API_KEY')
zhipu_api_key = os.getenv('ZHIPU_API_KEY')


# Set up the OpenAI client with zhipuAI key
client = OpenAI(
    api_key=openai_api_key,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
) 

def read_csv_dict(csv_file_path):
    """This function takes a csv file and loads it as a dict."""

    # Initialize an empty list to store the data
    data_list = []

    # Open the CSV file
    with open(csv_file_path, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
    
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append the row to the data list
            data_list.append(row)

    # Convert the list to a dictionary
    data_dict = {i: data_list[i] for i in range(len(data_list))}
    return data_dict


def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to Zhipu's GLM4-Flash model. The function then prints the response of the model.
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
    and passes it to Zhipu's GLM4-Flash model. The function then saves the response of the model as
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