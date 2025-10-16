import requests
import pytest
import json

def test_delete_post():
    """Tes untuk mengirim permintaan hapus dan memverifikasi responsnya."""

    # 1️⃣ Tentukan URL dari data yang mau dihapus
    url_delete = "https://jsonplaceholder.typicode.com/posts/1"

    # 2️⃣ Kirim permintaan DELETE
    response_delete = requests.delete(url_delete)

    # 3️⃣ Verifikasi (Assertion)
    # A. Status code untuk DELETE yang berhasil biasanya 200 (OK)
    assert response_delete.status_code == 200
    print(f"\nStatus Code DELETE: {response_delete.status_code} (OK)")

    # B. Cek isi respons body
    # JSONPlaceholder akan mengembalikan objek kosong {}
    body = response_delete.json()
    print("Respons Body DELETE:", body)

    assert body == {}, "Respons body seharusnya kosong ({})."

    # --- Langkah tambahan ---
    # Tidak perlu cek data benar-benar hilang karena API ini dummy (tidak menyimpan perubahan)
    print("✅ Tes DELETE selesai: permintaan berhasil dikirim (simulasi).")
