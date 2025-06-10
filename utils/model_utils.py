import torch
from transformers import AutoTokenizer, AutoModel
from tensorflow.keras.models import load_model # type: ignore
import streamlit as st

# Load IndoBERT tokenizer dan model (pytorch)
@st.cache_resource(show_spinner=True)
def load_bert_model():
    tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p1")
    model = AutoModel.from_pretrained("indobenchmark/indobert-base-p1")
    model.eval()
    return tokenizer, model


# Load model CNN-LSTM yang sudah dilatih
@st.cache_resource(show_spinner=True)
def load_trained_model():
    model = load_model('models/cnn_lstm_model.keras')
    return model