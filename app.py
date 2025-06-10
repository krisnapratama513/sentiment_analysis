import streamlit as st
import pandas as pd
import io
from utils.visualization_utils import plot_sentiment_distribution, plot_wordcloud
from utils.text_stats import text_statistics
from utils.embedding_utils import predict_sentiment
from utils.model_utils import load_bert_model, load_trained_model


# Main Streamlit app
def main():
    st.title("Aplikasi Analisis Sentimen ulasan produk di Tokopedia dengan CNN-LSTM dan IndoBERT")
    st.write("Anda dapat mengunggah file CSV berisi teks ulasan, atau masukkan teks secara manual untuk analisis sentimen.")

    st.info(
        """Belum punya kumpulan ulasan? Kami siap membantu Anda dengan proses pengambilan data secara otomatis (scraping)!

    Silakan buka halaman 'pages/scraping.py' 
    pada aplikasi ini untuk memulai proses scraping."""
    )

    tokenizer, bert_model = load_bert_model()
    cnn_lstm_model = load_trained_model()

    # Upload file CSV
    uploaded_file = st.file_uploader("Unggah file CSV", type=['csv'])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("File berhasil diunggah!")
            st.write("Preview data:")
            st.dataframe(df.head())

            # Pastikan ada kolom teks bernama 'ulasan' (atau sesuaikan)
            if 'ulasan' not in df.columns:
                st.error("File CSV harus memiliki kolom bernama 'ulasan' yang berisi teks.")
                return

            texts = df['ulasan'].astype(str).tolist()

            # Prediksi sentimen
            with st.spinner("Melakukan prediksi sentimen..."):
                sentiments, confidences = predict_sentiment(texts, tokenizer, bert_model, cnn_lstm_model)

            df['sentimen'] = sentiments
            df['confidence'] = confidences

            st.write("Hasil prediksi sentimen:")
            st.dataframe(df[['ulasan', 'sentimen', 'confidence']])

            # Tampilkan visualisasi EDA
            st.header("Exploratory Data Analysis (EDA)")
            text_statistics(texts)
            plot_sentiment_distribution(sentiments)
            plot_wordcloud(texts)

            # Download hasil prediksi
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            st.download_button(
                label="Download hasil prediksi sebagai CSV",
                data=csv_buffer.getvalue(),
                file_name="hasil_prediksi_sentimen.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses file: {e}")

    # Input teks manual
    st.header("Prediksi Sentimen dari Teks Manual")
    user_input = st.text_area("Masukkan teks ulasan di sini", height=150)
    if st.button("Prediksi Sentimen"):
        if not user_input.strip():
            st.warning("Mohon masukkan teks terlebih dahulu.")
        else:
            with st.spinner("Melakukan prediksi..."):
                sentiment, confidence = predict_sentiment([user_input], tokenizer, bert_model, cnn_lstm_model)
            st.success(f"Sentimen: **{sentiment[0]}**")
            st.info(f"Confidence: {confidence[0]:.2%}")

if __name__ == "__main__":
    main()
