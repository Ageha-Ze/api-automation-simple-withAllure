import requests
import pytest
import json

def test_update_post():
    """Tes untuk memperbarui/mengubah data postingan yang sudah ada."""

    # 1️⃣ Siapkan payload dengan data baru
    #    Kita akan mengubah total data dari postingan nomor 99
    payload = {
        "id": 55,  # Sertakan ID yang sama agar konsisten
        "title": "Agha update data",
        "body": "VAJURA ON~ YOU GOT THE THUNDER!!",
        "userId": 1
    }

    # 2️⃣ Tentukan URL endpoint (harus menyertakan ID data yang mau diubah)
    url = "https://jsonplaceholder.typicode.com/posts/55"

    # 3️⃣ Kirim permintaan PUT
    response = requests.put(url, json=payload)

    # 4️⃣ Verifikasi (Assertion)
    # A. Status code untuk PUT yang berhasil adalah 200 (OK)
    assert response.status_code == 200
    print(f"\nStatus Code: {response.status_code} (OK)")

    # B. Ubah respons menjadi JSON agar mudah dibaca
    response_data = response.json()
    print("Respons Data:")
    print(json.dumps(response_data, indent=4))

    # C. Verifikasi bahwa judul di respons sudah sesuai dengan yang kita kirim
    assert response_data["title"] == payload["title"]
    print(f"✅ Verifikasi Judul Berhasil: '{response_data['title']}'")

    # D. Pastikan kita mengubah ID yang benar
    assert response_data["id"] == 55
    print("✅ ID yang diubah sudah benar (55)")
