import torch
import numpy as np

# Fungsi untuk mendapatkan embedding dari teks input
def get_bert_embedding(text, tokenizer, model, max_length=128):
    inputs = tokenizer(text, padding='max_length', truncation=True, max_length=max_length, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
        token_embeddings = outputs.last_hidden_state.squeeze(0).numpy()  # shape (max_length, 768)
    return token_embeddings

# Fungsi prediksi sentimen dari teks
def predict_sentiment(texts, tokenizer, bert_model, cnn_lstm_model):
    embeddings = []
    for text in texts:
        emb = get_bert_embedding(text, tokenizer, bert_model)
        embeddings.append(emb)
    embeddings = np.array(embeddings)  # shape (n_samples, max_length, 768)
    preds = cnn_lstm_model.predict(embeddings)
    class_indices = np.argmax(preds, axis=1)
    confidences = np.max(preds, axis=1)
    classes = ['Negatif', 'Netral', 'Positif']
    sentiments = [classes[idx] for idx in class_indices]
    return sentiments, confidences