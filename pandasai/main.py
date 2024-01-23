import os 
from constants import openai_key
os.environ['OPENAI_API_KEY']=openai_key
import OpenAI

llm = OpenAI(api_token=OPENAI_API_KEY)

import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from pandasai.llm.open_assistant import OpenAssistant
     

