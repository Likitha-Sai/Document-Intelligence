import streamlit as st
import warnings
#from transformers import AutoTokenizer,AutoModelForCausalLM
from pypdf import PdfReader
from groq import Groq
import os


client=Groq(api_key=os.environ.get("GROQ_API_KEY"))



st.title("Document Intelligence")
file=st.file_uploader("drag_here",type=["pdf"])
if file :
    st.write("file uploaded successfully")
    reader=PdfReader(file)
    context=" ".join(page.extract_text() for page in reader.pages if page.extract_text() is not None)
    que=st.text_area("enter question")
    if que:
    
        prompt = f"""
        Use the following PDF context to answer the question.

        Context:
        {context}

        Question:
        {que}

        Answer:
        """
        response=client.chat.completions.create(messages=[{"role": "user", "content": prompt}],model="openai/gpt-oss-20b")
        a=response.choices[0].message.content
        st.write(a)
    else:
        st.write("please provide question")
else:
    st.write("please provide file")
    


"""@st.cache_resource
def loadmodel():
    tokenizer=AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
    model=AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
    return tokenizer,model


warnings.filterwarnings("ignore")
st.title("Document Intelligence")
file=st.file_uploader("drag here",type=["pdf"])
if file:
    st.write("file uploaded successfully")
    reader=PdfReader(file)
    context=" ".join(page.extract_text() for page in reader.pages if page is not None)
    que=st.text_area("enter question")
    if que:
    
        prompt = f""""""
        Use the following PDF context to answer the question.

        Context:
        {context}

        Question:
        {que}

        Answer:
        """"""
        a=loadmodel()
        inputs = a[0](prompt,return_tensors="pt",
        
        max_length=2048,
        padding=True
        )
    
        old_token=inputs["input_ids"].shape[1]
        gen=a[1].generate(**inputs,max_new_tokens=100)
        #new_token=len(gen[0])-old_token
        answer =a[0] .decode(gen[0][old_token:], skip_special_tokens=True)
        st.write(answer)
    else:
        st.write("Please provide question")
else:
    st.write("please provide file")"""


    
     


    
