import streamlit as st

from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain import PromptTemplate
from langchain.llms import CTransformers
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from transformers import AutoModelForCausalLM
from transformers import AutoModel

# this function is responsible for splitting the data into smaller chunks and convert the data in document format
def chunks_and_document(txt):
    
    text_splitter = CharacterTextSplitter() # text splitter method by default it has chunk_size = 200 and chunk_overlap = 200
    texts = text_splitter.split_text(txt) # split the text into smaller chunks
    docs = [Document(page_content=t) for t in texts] # convert the splitted chunks into document format
    
    return docs

def load_llm(model_name):
    # model = AutoModelForCausalLM.from_pretrained(model_name)
    # model = torch.load(model_name)
    model = AutoModel.from_pretrained(model_name)
     # model = torch.hub.load('huggingface/pytorch-transformers', model_name)
    return model
    
# model_name = "TheBloke/Llama-2-7B-Chat-GGML"
# model_name = "google-t5/t5-small"
model_name = "Falconsai/text_summarization"

# this functions is used for applying the llm model with our document 
def chains_and_response(docs):
    
    llm = load_llm(model_name)
    chain = load_summarize_chain(llm,chain_type='map_reduce')
    
    return chain.run(docs)
    
# Page title 
st.set_page_config(page_title='🧩 Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.title('Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.markdown('*Lucía Méndez López - lmendez31786@alumnos.uemc.es*')

st.header('🧩 Applicación para resumen de textos 🧩')

col1, col2 = st.columns(2)

# Text input
col1.subheader('Introduce tu texto aquí')
txt_input = col1.text_area('', '', height=300)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=False):
    submitted = st.form_submit_button('Submit')
    #if submitted and openai_api_key.startswith('sk-'):
    if submitted:
        with st.spinner('Calculating...'):
            docs = chunks_and_document(txt_input)
            response = chains_and_response(docs)
            result.append(response)

if len(result):
    col2.subheader('Tu texto resumido aquí')
    col2.info(response)
