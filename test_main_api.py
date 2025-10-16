import requests
import pytest
import json

def test_get_single_user():
    """Tes untuk mengambil data satu posting dan memverifikasinya."""

    # 1️⃣ Tentukan alamat (endpoint) API
    #    Ini seperti memberitahu pelayan meja nomor berapa yang mau kita tanya
    url = "https://jsonplaceholder.typicode.com/posts/55"

    # 2️⃣ Kirim permintaan GET
    #    Ini adalah aksi kita 'bertanya' ke pelayan
    response = requests.get(url)

    # 3️⃣ Verifikasi (Assertion)
    # A. Pastikan pelayan merespons dengan 'OK' (status code 200)
    assert response.status_code == 200
    print(f"\nStatus Code: {response.status_code} (OK)")

    # B. Ubah respons (yang formatnya JSON) menjadi dictionary Python
    response_data = response.json()

    # Cetak respons agar kita bisa lihat isinya
    print("Respons Data:")
    print(json.dumps(response_data, indent=4))

    # C. Cek apakah ID post sudah benar
    assert response_data["id"] == 55
    print("✅ Verifikasi ID berhasil: 55")

    # D. Cek apakah title sesuai dengan data yang diharapkan
    expected_title = "sit vel voluptatem et non libero"
    actual_title = response_data["title"]
    assert actual_title == expected_title
    print(f"✅ Verifikasi Judul Berhasil: '{actual_title}'")
