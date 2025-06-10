import numpy as np
import streamlit as st

def text_statistics(texts):
    lengths = [len(t.split()) for t in texts]
    st.write(f"Jumlah data: {len(texts)}")
    st.write(f"Rata-rata panjang teks (kata): {np.mean(lengths):.2f}")
    st.write(f"Panjang teks terpendek (kata): {np.min(lengths)}")
    st.write(f"Panjang teks terpanjang (kata): {np.max(lengths)}")