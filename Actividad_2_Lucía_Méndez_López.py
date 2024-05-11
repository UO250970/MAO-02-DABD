import streamlit as st

from langchain.text_splitter import CharacterTextSplitter # used for splitter the text into smalle chunks
from langchain.docstore.document import Document # convert the chunks in document format
from langchain.chains.summarize import load_summarize_chain # connect prompt and llm model
from langchain import PromptTemplate # for creating prompt 
from langchain.llms import CTransformers # loading the llm model
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


st.title('Técnicas de desarrollo de aplicaciones de Big Data')
