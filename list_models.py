import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
model_list_string = openai.Model.list()
print(model_list_string)
