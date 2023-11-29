# Mengimpor modul yang diperlukan
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

# Inisialisasi virtual display untuk menjalankan browser tanpa GUI (headless)
display = Display(visible=0, size=(800, 800))
display.start()

# Menggunakan chromedriver_autoinstaller untuk menginstal ChromeDriver
chromedriver_autoinstaller.install()

# Konfigurasi opsi Chrome
chrome_options = webdriver.ChromeOptions()

# Daftar opsi yang ingin ditambahkan
options = [
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
]

# Menambahkan opsi-opsi ke dalam chrome_options
for option in options:
    chrome_options.add_argument(option)

# Definisi kelas pengujian
class TestFormElements:
    @classmethod
    def setup_class(cls):
        # Inisialisasi driver Chrome dengan opsi yang telah dikonfigurasi
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://localhost:5000")  # Ganti URL sesuai kebutuhan

    @classmethod
    def teardown_class(cls):
        # Tutup browser setelah selesai pengujian
        cls.driver.quit()

    def test_nama_label(self):
        # Mencari elemen label Nama dan memeriksa teksnya
        nama_label = self.driver.find_element(By.XPATH, "//label[@for='nama']")
        assert nama_label.text == "Nama Lengkap:", "Pengecekan Nama gagal"

    def test_nim_label(self):
        # Mencari elemen label NIM dan memeriksa teksnya
        nim_label = self.driver.find_element(By.XPATH, "//label[@for='nim']")
        assert nim_label.text == "Nomor Induk Mahasiswa:", "Pengecekan NIM gagal"

    def test_mata_kuliah_label(self):
        # Mencari elemen label Mata Kuliah dan memeriksa teksnya
        mata_kuliah_label = self.driver.find_element(By.XPATH, "//label[@for='mata_kuliah']")
        assert mata_kuliah_label.text == "Mata Kuliah:", "Pengecekan Mata Kuliah gagal"

    def test_jurusan_label(self):
        # Mencari elemen label Jurusan dan memeriksa teksnya
        jurusan_label = self.driver.find_element(By.XPATH, "//label[@for='jurusan']")
        assert jurusan_label.text == "Jurusan:", "Pengecekan Jurusan gagal"

# Jalankan pengujian jika file ini dieksekusi secara langsung
if __name__ == "__main__":
    pytest.main()