# Sentiment Analysis & Tokopedia Review Scraper
Aplikasi berbasis **Streamlit** untuk melakukan analisis sentimen pada ulasan produk Tokopedia menggunakan model **CNN-LSTM** dan **embedding IndoBERT**.  
Selain itu, aplikasi ini juga menyediakan fitur **scraping otomatis** untuk mengumpulkan ulasan produk dari Tokopedia menggunakan **Selenium** dan **BeautifulSoup**.

---

## ✨ Fitur

- 🟢 Analisis sentimen ulasan produk Tokopedia.
- 🕸️ Scraping ulasan secara otomatis (bisa pilih jumlah halaman).
- 📊 Visualisasi data eksplorasi (EDA): distribusi sentimen & wordcloud.
- ✍️ Input manual ulasan untuk prediksi sentimen secara langsung.
- 📁 Unggah file CSV berisi ulasan untuk batch prediksi.
- 📤 Ekspor hasil analisis ke file CSV.

---

## 🛠️ Requirements
- Python 3.10.11
- streamlit
- pandas
- selenium
- webdriver-manager
- beautifulsoup4
- torch
- transformers
- tensorflow
- numpy
- tqdm
- spacy
- scikit-learn
- matplotlib
- seaborn
- plotly

---

## 🧑‍💻 Cara Penggunaan

1. **Upload file CSV**  
   Unggah file CSV yang berisi kolom *ulasan* untuk dianalisis sentimennya secara batch.

2. **Input manual**  
   Masukkan teks ulasan secara manual untuk mendapatkan prediksi sentimen langsung.

3. **Scraping ulasan Tokopedia**  
   Masukkan URL produk Tokopedia dan pilih jumlah halaman ulasan yang ingin di-*scrape* secara otomatis.

4. **Lihat hasil analisis**  
   Hasil prediksi sentimen akan ditampilkan dalam bentuk tabel, lengkap dengan *confidence score*.

5. **Visualisasi**  
   Lihat distribusi sentimen, *wordcloud*, dan statistik teks lainnya untuk mendapatkan *insight* yang lebih dalam.

6. **Download hasil**  
   Unduh hasil analisis dalam format CSV untuk dokumentasi atau analisis lanjutan.

---

## 📂 Struktur Proyek


<pre>
.
├── app.py                  # Aplikasi utama Streamlit
├── scraping.py             # Modul scraping ulasan Tokopedia
├── requirements.txt        \endensi Python
├── models/                 # Model deep learning yang sudah dilatih dari googlecolab
│   └── cnn_lstm_model.keras
├── pages/                  # Halaman tambahan Streamlit (halaman scraping)
│   └── chromedriver        # Digunakan untuk Scraping
│   └── scraping.py
├── utils/                  # Skrip utilitas (embedding, model, statistik, visualisasi)
│   ├── embedding_utils.py
│   ├── model_utils.py
│   ├── text_stats.py
│   └── visualization_utils.py
└── venv/                   # Virtual environment (opsional)
</pre>