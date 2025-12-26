import pandas as pd
import numpy as np
import time


def clean_and_preprocess(input_filepath, output_filepath):
    """
    Fungsi ini memuat dataset mentah, melakukan serangkaian langkah pembersihan
    dan prapemrosesan, lalu menyimpan hasilnya ke file CSV baru.

    Langkah-langkah yang dilakukan:
    1. Membuat salinan data untuk menjaga data asli.
    2. Membersihkan spasi pada nama kolom.
    3. Mengganti placeholder '-' menjadi nilai NaN.
    4. Mengonversi kolom-kolom yang seharusnya numerik ke tipe data numerik.
    5. Mengisi (imputasi) nilai NaN yang ada:
        - Kolom numerik diisi dengan nilai median.
        - Kolom kategorikal diisi dengan nilai modus (nilai yang paling sering muncul).
    """

    print("Memulai proses pembersihan data...")
    start_time = time.time()

    # --- LANGKAH 1: Memuat Data ---
    try:
        df_raw = pd.read_csv(input_filepath)
        print(
            f"[1/5] Data mentah '{input_filepath}' berhasil dimuat ({df_raw.shape[0]} baris)."
        )
    except FileNotFoundError:
        print(
            f"ERROR: File '{input_filepath}' tidak ditemukan. Mohon periksa kembali path file."
        )
        return

    # --- LANGKAH 2: Prapemrosesan Awal ---
    # Membuat salinan dan membersihkan nama kolom
    df_clean = df_raw.copy()
    df_clean.columns = df_clean.columns.str.strip()

    # Mengganti '-' dengan NaN
    df_clean.replace("-", np.nan, inplace=True)
    print("[2/5] Nama kolom dibersihkan dan placeholder '-' diubah menjadi NaN.")

    # --- LANGKAH 3: Konversi Tipe Data ---
    numeric_columns = [
        "duration",
        "src_bytes",
        "dst_bytes",
        "missed_bytes",
        "src_pkts",
        "src_ip_bytes",
        "dst_pkts",
        "dst_ip_bytes",
        "http_trans_depth",
        "http_request_body_len",
        "http_response_body_len",
        "dns_qclass",
        "dns_qtype",
        "dns_rcode",
        "http_status_code",
        "src_port",
        "dst_port",
    ]

    for col in numeric_columns:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")
    print("[3/5] Tipe data kolom numerik telah dikonversi.")

    # --- LANGKAH 4: Mengisi Nilai Hilang (Imputasi) ---
    # Isi kolom numerik dengan median
    for col in df_clean.select_dtypes(include=np.number).columns:
        if df_clean[col].isnull().any():
            df_clean[col].fillna(df_clean[col].median(), inplace=True)

    # Isi kolom kategorikal dengan modus
    for col in df_clean.select_dtypes(include=["object"]).columns:
        if df_clean[col].isnull().any():
            mode_val = "Unknown"
            if not df_clean[col].mode().empty:
                mode_val = df_clean[col].mode()[0]
            df_clean[col].fillna(mode_val, inplace=True)

    print("[4/5] Nilai yang hilang (NaN) telah diisi dengan median/modus.")

    # --- LANGKAH 5: Menyimpan Hasil ---
    try:
        df_clean.to_csv(output_filepath, index=False)
        duration = time.time() - start_time
        print(f"[5/5] Data bersih berhasil disimpan di '{output_filepath}'.")
        print(f"Proses selesai dalam {duration:.2f} detik.")
    except Exception as e:
        print(f"ERROR saat menyimpan file: {e}")


# --- BAGIAN EKSEKUSI UTAMA ---
if __name__ == "__main__":
    # Tentukan nama file input dan output
    # Pastikan file 'train_test_network.csv' ada di folder yang sama
    # dengan skrip Python ini.
    raw_file = "/home/elnoersan/Skripsi/Paper/NotebookTODO/train_test_network.csv"
    cleaned_file = "cleaned_train_test_network.csv"

    # Jalankan fungsi pembersihan
    clean_and_preprocess(raw_file, cleaned_file)
