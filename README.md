# 🧪 JSONPlaceholder API Automation
Project ini berisi contoh otomasi testing API menggunakan **Pytest** dan **Allure** untuk visualisasi laporan hasil testing.

---

## 📂 Struktur Folder
```
jsonplaceholder_API_Automate/
│
├── post_api.py      # Tes untuk POST (create data)
├── put_api.py       # Tes untuk PUT (update data)
├── delete_api.py    # Tes untuk DELETE (hapus data)
├── main_api.py      # Tes untuk GET (ambil data)
└── reports/         # Folder laporan Allure
```

---

## ⚙️ Instalasi & Persiapan
1. Pastikan sudah terinstall **Python** dan **pip**
   ```bash
   python --version
   pip --version
   ```

2. Install library yang dibutuhkan
   ```bash
   pip install pytest requests allure-pytest
   ```

3. Install **Allure Commandline** (pilih salah satu cara):
   - **Via Scoop (disarankan)**
     ```bash
     scoop install allure
     ```
   - **Atau via Chocolatey**
     ```bash
     choco install allure
     ```

4. Verifikasi instalasi Allure
   ```bash
   allure --version
   ```

---

## 🚀 Menjalankan Test dan Melihat Report
Gunakan perintah berikut di **PowerShell**:

```bash
pytest --alluredir=reports/ ; allure serve reports/
```

🟢 Penjelasan:
- `pytest --alluredir=reports/` → Menjalankan semua tes dan menyimpan hasilnya ke folder `reports/`.
- `allure serve reports/` → Membuka laporan interaktif di browser secara otomatis.

---

## 📊 Contoh Output
Setelah menjalankan perintah di atas, browser akan otomatis terbuka dan menampilkan laporan seperti ini:

✅ Semua test berstatus **passed**  
📈 Setiap endpoint API (GET, POST, PUT, DELETE) tampil dalam grafik dan log lengkap  
🕒 Disertai waktu eksekusi dan detail respons API
