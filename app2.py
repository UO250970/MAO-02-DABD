import streamlit as st
import os

from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain import PromptTemplate
from langchain.llms import CTransformers
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


from transformers import pipeline, AutoModel

# Configura el token de API como una variable de entorno
os.environ["TRANSFORMERS_TOKEN"] = "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"

# this function is responsible for splitting the data into smaller chunks and convert the data in document format
def chunks_and_document(txt):
    
    text_splitter = CharacterTextSplitter() # text splitter method by default it has chunk_size = 200 and chunk_overlap = 200
    texts = text_splitter.split_text(txt) # split the text into smaller chunks
    docs = [Document(page_content=t) for t in texts] # convert the splitted chunks into document format
    
    return docs
    
# Loading the Llama 2's LLM
def load_llm():
    
    model_url = pipeline("text-generation", model="TheBloke/CodeLlama-70B-Instruct-GGUF")
    # model = AutoModel.from_pretrained("TheBloke/CodeLlama-70B-Instruct-GGUF")
    llm = CTransformers(
        model=model_url,
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5   )

    return llm

# this functions is used for applying the llm model with our document 
def chains_and_response(docs):
    
    llm = load_llm()
    chain = load_summarize_chain(llm,chain_type='map_reduce')
    
    return chain.run(docs)
    
# Page title
st.set_page_config(page_title='🦜🔗 Text Summarization App')
st.title('🦜🔗 Text Summarization App')

# Text input
txt_input = st.text_area('Enter your text', '', height=200)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    #if submitted and openai_api_key.startswith('sk-'):
    if submitted:
        with st.spinner('Calculating...'):
            docs = chunks_and_document(txt_input)
            response = chains_and_response(docs)
            result.append(response)

if len(result):
    st.title('📝✅ Summarization Result')
    st.info(response)