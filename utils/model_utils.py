import torch
from transformers import AutoTokenizer, AutoModel
from tensorflow.keras.models import load_model
import streamlit as st
import os

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
    current_dir = os.path.dirname(os.path.abspath(__file__))  # path ke 'utils'

    # Naik satu folder ke root repositori
    root_repo_path = os.path.dirname(current_dir)
    # Bangun path relatif ke model
    model_path = os.path.join(root_repo_path, "models", "cnn_lstm_model.keras")

    # Load model menggunakan path absolut yang sudah dibangun
    model = load_model(model_path)
    return model