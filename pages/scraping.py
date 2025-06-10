import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os
import pandas as pd

def get_driver():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(current_dir, "chromedriver")
    service = Service(executable_path=chromedriver_path)

    options = Options()
    # Non-headless agar GUI muncul
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_reviews(driver, max_pages):
    wait = WebDriverWait(driver, 15)
    data = []
    page_count = 0

    while page_count < max_pages:
        st.info(f"Scraping halaman ke-{page_count + 1}")

        # Klik tombol Load More sampai habis
        try:
            load_more_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='css-89c2tx']"))
            )
            load_more_button.click()
            time.sleep(2)  # Tunggu konten termuat
        except:
            pass  #  tangani error dengan cara "tidak melakukan apa-apa"

        # kode disini masih di eksekusikan? jika try : error?

        # Ambil HTML review setelah load more selesai
        try:
            review_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-41l5iz")))
            review_html = review_element.get_attribute("outerHTML")
            soup = BeautifulSoup(review_html, "html.parser")
            containers = soup.find_all('article', class_="css-1pr2lii")

            for idx, container in enumerate(containers, start=1 + page_count * 100):  # nomor urut global
                try:
                    block_product = container.find('a', class_="styProduct")
                    product_name = block_product.find('p', attrs={'data-unify': 'Typography'}).text

                    block_rating = container.find('div', class_="rating")
                    rating_value = block_rating['aria-label'] if block_rating else None

                    review = container.find('span', attrs={'data-testid': 'lblItemUlasan'}).text

                    data.append({
                        # 'no': idx,
                        'nama_product': product_name,
                        'rating': rating_value,
                        'ulasan': review
                    })
                except AttributeError:
                    continue
        except Exception as e:
            st.error(f"Error saat mengambil review: {e}")
            break


        # Coba klik tombol "Laman berikutnya"
        try:
            next_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']"))
            )
            next_button.click()
            page_count += 1
            time.sleep(3)  # Tunggu halaman baru termuat
        except:
            st.info("Tidak ada tombol 'Laman berikutnya' atau sudah mencapai halaman terakhir.")
            break

    return data

def main():
    st.title("Scraping Ulasan Produk Tokopedia")

    st.text("1. Buka website Tokopedia.")
    st.text("2. Masuk ke halaman toko, lalu buka bagian ulasan.")
    st.image('pages/img1.png', caption="Contoh halaman ulasan toko")
    st.text("3. Salin link")
    st.image("pages/img2.png", caption="Contoh URL halaman ulasan")

    url = st.text_input("Masukkan URL Tokopedia:", "")

    # Slider untuk memilih jumlah halaman yang akan di-scrape
    max_pages = st.slider("Pilih jumlah halaman yang ingin di-scrape:", min_value=1, max_value=50, value=10)

    if st.button("Mulai Scraping"):
        driver = get_driver()
        driver.get(url)
        try:
            data = scrape_reviews(driver, max_pages)
            if data:
                df = pd.DataFrame(data)
                st.success(f"Berhasil scraping {len(df)} ulasan dari {max_pages} halaman.")
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='tokopedia_reviews.csv',
                    mime='text/csv'
                )
            else:
                st.warning("Tidak ada data ulasan yang ditemukan.")
        finally:
            driver.quit()

if __name__ == "__main__":
    main()
