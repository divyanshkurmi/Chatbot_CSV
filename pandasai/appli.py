import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import os
from constants import openai_key
os.environ["OPENAI_API_KEY"]=openai_key
openai_key='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'
llm = OpenAI(api_token=openai_key)



# Instantiate a LLM
from pandasai.llm import OpenAI
llm = OpenAI()




import streamlit as st

# Define the main function for your web app
def main():
    # Give your app a title
    st.title("Visualization of your tabular data")
    # Add a sidebar with some options
    options = ["Home", "About"]
    choice = st.sidebar.selectbox("Navigate", options)

    
    if choice == "Home":
        st.sidebar.write("Welcome to the Home page.")
    elif choice == "About":
        st.sidebar.write("Welcome to the About page. We serve you as a helping hand for your analysis in a quicker.")

    uploaded_file=st.file_uploader("upload your file", type=["csv"])

    if uploaded_file is not None:
        df=pd.read_csv(uploaded_file)
        
        st.write(df.head(5))

        prompt=st.text_area("ENTER YOUR PROMPT")

        if st.button("generate"):
            if prompt:
                st.write("PANDAS AI IS GENERATING an answer, please wait...")
                data= SmartDataframe(df, config={"llm":llm})
                st.write(data.chat(prompt))

            else:
                st.warning("please enter a prompt")    
    # Add some text to the app
    st.write("Welcome to my visualization app!")



  

# Run the main function
if __name__ == "__main__":
    main()


