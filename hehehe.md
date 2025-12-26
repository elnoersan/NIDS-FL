DETEKSI DAN KLASIFIKASI SERANGAN JARINGAN SMART CITY MENGGUNAKAN
FEDERATED LEARNING PADA LALU LINTAS JARINGAN

## HALAMAN JUDUL

![](media/image1.png){width="2.106531058617673in"
height="2.8854166666666665in"}

Disusun Oleh:

+----------------------+------------------------+
| N a m a              | : Informatika          |
|                      |                        |
| NIM                  | : 94523999             |
+======================+========================+

**PROGRAM STUDI INFORMATIKA -- PROGRAM SARJANA**

**FAKULTAS TEKNOLOGI INDUSTRI**

**UNIVERSITAS ISLAM INDONESIA**

**2020**

## HALAMAN PENGESAHAN DOSEN PEMBIMBING

DETEKSI DAN KLASIFIKASI SERANGAN JARINGAN SMART CITY MENGGUNAKAN
FEDERATED LEARNING PADA LALU LINTAS JARINGAN

![Background Lembar
Pengesahaan](media/image2.png){width="3.543307086614173in"
height="4.862204724409449in"}TUGAS AKHIR

Disusun Oleh:

+----------------------+------------------------+
| N a m a              | : Rian Nur Ikhsan      |
|                      |                        |
| NIM                  | : 22523297             |
+======================+========================+

Yogyakarta, 25 Desember 2025

Pembimbing,

( Fayruz Rahma, S.T., M.Eng. )

## HALAMAN PENGESAHAN DOSEN PENGUJI

DETEKSI DAN KLASIFIKASI SERANGAN JARINGAN SMART CITY MENGGUNAKAN
FEDERATED LEARNING PADA LALU LINTAS JARINGAN

TUGAS AKHIR

Telah dipertahankan di depan sidang penguji sebagai salah satu syarat
untuk\
memperoleh gelar Sarjana Komputer dari Program Studi Informatika --
Program Sarjana\
di Fakultas Teknologi Industri Universitas Islam Indonesia

Yogyakarta, 1 Nopember 2017

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| ###### ![C:\\Users\\Windows\\AppData\\Local\\Microsoft\\Windows\\INetCache\\Content.Word\\Background Lembar Pengesahaan.png](media/image2.png){width="3.5430555555555556in" height="4.861805555555556in"}Tim Penguji | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+                                                |
| Hendrik, S.T., M.Eng.                                                                                                                                                                                                |                                                |
+======================================================================================================================================================================================================================+:===============================================+
| **Anggota 1**                                                                                                                                                                                                        | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+                                                |
| Dr. Raden Teduh Dirgahayu, S.T., M.Sc.                                                                                                                                                                               |                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| **Anggota 2**                                                                                                                                                                                                        | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+                                                |
| Dr. Mukhammad A Setiawan, S.T., M.Sc.                                                                                                                                                                                |                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+

Mengetahui,

Ketua Program Studi Informatika -- Program Sarjana

Fakultas Teknologi Industri

Universitas Islam Indonesia

( Dr. Raden Teduh Dirgahayu, S.T., M.Sc. )

## HALAMAN PERNYATAAN KEASLIAN TUGAS AKHIR

Yang bertanda tangan di bawah ini:

> Nama : Rian Nur Ikhsan
>
> NIM : 22523297

Tugas akhir dengan judul:

DETEKSI DAN KLASIFIKASI SERANGAN JARINGAN SMART CITY MENGGUNAKAN
FEDERATED LEARNING PADA LALU LINTAS JARINGAN

Menyatakan bahwa seluruh komponen dan isi dalam tugas akhir ini adalah
hasil karya saya sendiri. Apabila di kemudian hari terbukti ada beberapa
bagian dari karya ini adalah bukan hasil karya sendiri, tugas akhir yang
diajukan sebagai hasil karya sendiri ini siap ditarik kembali dan siap
menanggung risiko dan konsekuensi apapun.

Demikian surat pernyataan ini dibuat, semoga dapat dipergunakan
sebagaimana mestinya.

Yogyakarta, 25 Desember 2025

( Rian Nur Ikhsan )

## HALAMAN PERSEMBAHAN

Alhamdulillahirobbil'alamin, puji syukur atas berkah dan nikmat dari
Allah SWT. Tuhan dari semesta ala mini yang akbar. Tidak lupa Shalawat
juga salam kita haturkan kepada junjungan kita Nabi Muhammad SAW. Yang
akan memberikan safa'atnya di hari akhir kelak.

Terima kasih telah menjadi penyambung saya kedunia ini kepada orang tua
saya, mengasuh, membimbing, menemani saya sejak di alam rahim. Mendukung
saya untuk selalu semangat walaupun saya sering berkecil hati. Semoga
amal-amal mereka diterima disisi-Nya dan diberi karahmat sepanjang masa.

Terima kasih kepada Dosen Pembimbing Tugas akhir saya, Ibu Fayruz Rahma
dan Bapak Kurniawan Dwi Irianto yang selalu memberi nasihat dan
membimbing saya dengan sabar selama ini.

Terima kasih kepada semua pihak yang tidak dapat saya sebutkan satu
persatu atas bantuan, dukungan dan semangat baik secara langsung maupun
tidak.

## HALAMAN MOTO

"Maaf..."

"Terima kasih"

"Allah mengetahui, sedangkan kamu tidak mengetahui." (Q.S Al-Baqarah:
216)

"Nilai kehidupanku lemah, tapi diriku tetap menunggu nilainya terkena
inflasi, cihuuy"

## KATA PENGANTAR

Assalamu'alaikum warahmatullahi wabarakatuh.

Segala puji dan syukur penulis panjatkan ke hadirat Allah Swt. atas
limpahan rahmat, taufik, dan karunia-Nya sehingga penulis dapat
menyelesaikan Tugas Akhir ini dengan baik. Laporan ini berjudul "Deteksi
dan Klasifikasi Serangan Jaringan Smart City dengan Federated Learning
pada Lalu Lintas Jaringan", yang disusun sebagai salah satu syarat untuk
memperoleh gelar Sarjana (S1) pada Program Studi Informatika, Fakultas
Teknologi Industri, Universitas Islam Indonesia.

Pada kesempatan ini, penulis ingin menyampaikan rasa terima kasih yang
sebesar-besarnya kepada pihak-pihak yang telah memberikan dukungan, baik
secara langsung maupun tidak langsung, selama proses penyusunan Tugas
Akhir ini, yaitu:

1.  Kedua orang tua penulis yang telah menuntun dari kecil hingga besar
    dengan nilai yang tidak bisa dihitungkan secara materi dan batin.

2.  Prof. Fathul Wahid, S.T., M.Sc., Ph.D., selaku Rektor Universitas
    Islam Indonesia.

3.  Dhomas Hatta Fudholi, S.T., M.Eng., Ph.D., selaku Ketua Program
    Studi Informatika -- Program Sarjana UII.

4.  Ibu Fayruz Rahma, S.T., M.Eng., yang selalu memberi nasihat dan
    membimbing dengan sabar selama ini.

5.  Bapak Kurniawan Dwi Irianto, S.T., M.Sc., yang memberikan petunjuk
    serta arahan selama ini.

6.  Paman-Paman yang memberikan ilmu apa itu sabar dan percaya diri.

7.  Semua pihak yang tidak dapat disebutkan satu per satu, namun telah
    berkontribusi dalam bentuk apapun

Penulis secara sadah bahwa Tugas Akhir ini masih jauh dari kata cukup.
Oleh karena itu, kritik, masukan, dan saran yang terbuka untuk membangun
sangat diharapkan. Semoga dengan karya ini kelak dapat memberikan
manfaat serta dasar pengembangan penelitian yang lebih lanjut di masa
yang akan datang.

Yogyakarta, 25 Desember 2025

( Rian Nur Ikhsan )

## SARI

Perkembangan teknologi digital mendorong implementasi konsep Smart City
yang mengandalkan jaringan IoT untuk meningkatkan efisiensi layanan
publik. Namun, kompleksitas jaringan ini meningkatkan risiko serangan
siber yang dapat mengganggu layanan kritis. Penelitian ini mengkaji
penerapan Federated Learning (FL) sebagai pendekatan terdistribusi untuk
membangun Network Intrusion Detection System (NIDS) tanpa memusatkan
data mentah, sehingga privasi tetap terjaga. Dataset yang digunakan
adalah ToN-IoT, dengan simulasi distribusi data IID dan Non-IID
menggunakan Dirichlet untuk merepresentasikan heterogenitas antar klien.
Dua algoritma FL, yaitu Federated Averaging (FedAvg) dan Federated
Proximal (FedProx), dibandingkan pada dua arsitektur deep learning:
Multi-Layer Perceptron (MLP) dan Convolutional Neural Network 1D
(CNN-1D), untuk skenario klasifikasi biner dan multi-kelas.

Hasil eksperimen menunjukkan bahwa FedProx lebih stabil pada kondisi
Non-IID dibanding FedAvg, meskipun dengan biaya komputasi lebih tinggi.
CNN-1D memberikan performa lebih baik daripada MLP, terutama pada
skenario multi-kelas, dengan peningkatan akurasi dan F1-Score yang
signifikan. Penelitian ini merekomendasikan penggunaan FedProx dengan
CNN-1D untuk lingkungan smart city yang heterogen, karena mampu menjaga
stabilitas pelatihan dan akurasi deteksi serangan. Temuan ini diharapkan
menjadi referensi awal bagi pengembangan IDS berbasis FL yang aman dan
efisien..

Kata kunci: smart city, federated learning, ton-iot, nids, non-iid,
privacy.

## GLOSARIUM

Glosarium memuat daftar kata tertentu yang digunakan dalam laporan dan
membutuhkan penjelasan, misalnya kata serapan yang belum lazim
digunakan. Urutkan sesuai abjad. Contoh penulisannya seperti di bawah
ini:

> Backdoor Serangan yang memungkinkan akses tidak sah ke sistem melalui
> celah tersembunyi.

Batch Size Jumlah sampel data yang diproses dalam satu iterasi pelatihan
model.

Confusion Matrix Matriks yang digunakan untuk mengevaluasi performa
model klasifikasi dengan membandingkan prediksi dan label aktual.

Dirichlet Distribusi probabilitas yang digunakan untuk mensimulasikan
ketimpangan data antar klien dalam skenario Non-IID.

Federated Learning Paradigma pembelajaran mesin terdistribusi yang
memungkinkan pelatihan model tanpa memindahkan data mentah ke server
pusat.

MITM Jenis serangan di mana penyerang menyusup di antara komunikasi dua
pihak untuk mengintip atau memanipulasi data.

Micro (μ) Simbol yang digunakan untuk merepresentasikan koefisien
proximal term pada algoritma FedProx, yang mengontrol kekuatan
regularisasi terhadap deviasi model lokal dari model global.

Non-IID Kondisi distribusi data antar klien yang tidak identik dan
independen, umum terjadi pada lingkungan terdistribusi.

Proximal Term Komponen tambahan pada fungsi loss FedProx yang membatasi
penyimpangan model lokal dari model global untuk mengurangi client
drift.

Skew Ketidakseimbangan distribusi data atau kelas yang menyebabkan bias
dalam pelatihan model.

## DAFTAR ISI

[HALAMAN JUDUL [i](#halaman-judul)](#halaman-judul)

[HALAMAN PENGESAHAN DOSEN PEMBIMBING
[ii](#halaman-pengesahan-dosen-pembimbing)](#halaman-pengesahan-dosen-pembimbing)

[HALAMAN PENGESAHAN DOSEN PENGUJI
[iii](#halaman-pengesahan-dosen-penguji)](#halaman-pengesahan-dosen-penguji)

[HALAMAN PERNYATAAN KEASLIAN TUGAS AKHIR
[iv](#halaman-pernyataan-keaslian-tugas-akhir)](#halaman-pernyataan-keaslian-tugas-akhir)

[HALAMAN PERSEMBAHAN [v](#halaman-persembahan)](#halaman-persembahan)

[HALAMAN MOTO [vi](#halaman-moto)](#halaman-moto)

[KATA PENGANTAR [vii](#kata-pengantar)](#kata-pengantar)

[SARI [viii](#sari)](#sari)

[GLOSARIUM [ix](#glosarium)](#glosarium)

[DAFTAR ISI [x](#_Toc217663818)](#_Toc217663818)

[DAFTAR TABEL [xiii](#daftar-tabel)](#daftar-tabel)

[DAFTAR GAMBAR [xv](#daftar-gambar)](#daftar-gambar)

[BAB I PENDAHULUAN [1](#bab-i-pendahuluan)](#bab-i-pendahuluan)

[1.1 Latar belakang [1](#latar-belakang)](#latar-belakang)

[1.2 Rumusan Masalah [2](#rumusan-masalah)](#rumusan-masalah)

[1.3 Batasan Masalah [2](#batasan-masalah)](#batasan-masalah)

[1.4 Tujuan Penelitian [3](#tujuan-penelitian)](#tujuan-penelitian)

[1.5 Manfaat Penelitian [3](#manfaat-penelitian)](#manfaat-penelitian)

[1.6 Metodologi Penelitian
[4](#metodologi-penelitian)](#metodologi-penelitian)

[1.7 Metodologi Penelitian
[5](#metodologi-penelitian-1)](#metodologi-penelitian-1)

[BAB II LANDASAN TEORI
[7](#bab-ii-landasan-teori)](#bab-ii-landasan-teori)

[2.1 Network Intrusion Detection System
[7](#network-intrusion-detection-system)](#network-intrusion-detection-system)

[2.2 CRIPS-DM [8](#crips-dm)](#crips-dm)

[2.3 Dataset UNSW: ToN IoT
[9](#dataset-unsw-ton-iot)](#dataset-unsw-ton-iot)

[2.4 Teknik Pre-Processing
[15](#teknik-pre-processing)](#teknik-pre-processing)

[2.5 Federated Learning [16](#federated-learning)](#federated-learning)

[2.5.1 Arsitektur Horizontal Federated Learning
[16](#arsitektur-horizontal-federated-learning)](#arsitektur-horizontal-federated-learning)

[2.5.2 Karakteristik Distribusi Data (IID dan Non-IID)
[17](#karakteristik-distribusi-data-iid-dan-non-iid)](#karakteristik-distribusi-data-iid-dan-non-iid)

[2.5.3 Algoritma Agregasi
[18](#algoritma-agregasi)](#algoritma-agregasi)

[2.6 Deep Learning [20](#deep-learning)](#deep-learning)

[2.6.1 Multi-Layer Perceptron
[20](#multi-layer-perceptron)](#multi-layer-perceptron)

[2.6.2 Convolutional Neural Network 1 Dimensional (CNN-1D)
[21](#convolutional-neural-network-1-dimensional-cnn-1d)](#convolutional-neural-network-1-dimensional-cnn-1d)

[2.7 Hyperparameter: Grid Search
[21](#hyperparameter-grid-search)](#hyperparameter-grid-search)

[2.7.1 Mekanisme Grid Search
[22](#mekanisme-grid-search)](#mekanisme-grid-search)

[2.7.2 Parameter Kunci dalam Pembelajaran Terdistribusi
[22](#parameter-kunci-dalam-pembelajaran-terdistribusi)](#parameter-kunci-dalam-pembelajaran-terdistribusi)

[2.7.3 Strategi Pemilihan Hyperparameter Berbasis Multi-Kriteria
[22](#strategi-pemilihan-hyperparameter-berbasis-multi-kriteria)](#strategi-pemilihan-hyperparameter-berbasis-multi-kriteria)

[2.8 Teknik Evaluasi [23](#teknik-evaluasi)](#teknik-evaluasi)

[2.8.1 Confuse Matrix [23](#confuse-matrix)](#confuse-matrix)

[2.8.2 Metrik Kinerja Klasifikasi
[24](#metrik-kinerja-klasifikasi)](#metrik-kinerja-klasifikasi)

[2.8.3 Metrik Kinerja Klasifikasi
[25](#metrik-kinerja-klasifikasi-1)](#metrik-kinerja-klasifikasi-1)

[2.9 Penelitian Terkait [26](#penelitian-terkait)](#penelitian-terkait)

[BAB III METODOLOGI PENELITIAN
[34](#bab-iii-metodologi-penelitian)](#bab-iii-metodologi-penelitian)

[3.1 Alur Pengerjaan [34](#alur-pengerjaan)](#alur-pengerjaan)

[3.2 Lingkungan Penelitian
[35](#lingkungan-penelitian)](#lingkungan-penelitian)

[3.3 Businisse Understanding
[37](#businisse-understanding)](#businisse-understanding)

[3.3.1 Tujuan Bisnis (Business Objectives)
[38](#tujuan-bisnis-business-objectives)](#tujuan-bisnis-business-objectives)

[3.3.2 Kriteria Keberhasilan (Success Criteria)
[38](#kriteria-keberhasilan-success-criteria)](#kriteria-keberhasilan-success-criteria)

[3.4 Data Understanding [39](#data-understanding)](#data-understanding)

[3.4.1 Analisis Distribusi Kelas
[39](#analisis-distribusi-kelas)](#analisis-distribusi-kelas)

[3.4.2 Analisis Integritas dan Kualitas Data
[40](#analisis-integritas-dan-kualitas-data)](#analisis-integritas-dan-kualitas-data)

[3.4.3 Analisis Korelasi Fitur
[40](#analisis-korelasi-fitur)](#analisis-korelasi-fitur)

[3.5 Data Preparation [41](#data-preparation)](#data-preparation)

[3.5.1 Pembersihan Data [41](#pembersihan-data)](#pembersihan-data)

[3.5.2 Transformasi Variabel Kategorikal (Encoding)
[42](#transformasi-variabel-kategorikal-encoding)](#transformasi-variabel-kategorikal-encoding)

[3.5.3 Seleksi Fitur Berbasis Variansi
[42](#seleksi-fitur-berbasis-variansi)](#seleksi-fitur-berbasis-variansi)

[3.5.4 Standardisasi Fitur (Feature Scaling)
[42](#standardisasi-fitur-feature-scaling)](#standardisasi-fitur-feature-scaling)

[3.5.5 Pembagian Data Terstratifikasi
[43](#pembagian-data-terstratifikasi)](#pembagian-data-terstratifikasi)

[3.5.6 Pembersihan Data [43](#pembersihan-data-1)](#pembersihan-data-1)

[3.6 Modeling [43](#modeling)](#modeling)

[3.6.1 Strategi Horizontal Federated Learning
[44](#strategi-horizontal-federated-learning)](#strategi-horizontal-federated-learning)

[3.6.2 Arsitektur Deep Learning
[44](#arsitektur-deep-learning)](#arsitektur-deep-learning)

[3.6.3 Strategi Distribusi Data Antar Klien (Non-IID Simulation)
[45](#strategi-distribusi-data-antar-klien-non-iid-simulation)](#strategi-distribusi-data-antar-klien-non-iid-simulation)

[3.6.4 Optimasi Hyperparameter dan Reprodusibilitas
[46](#optimasi-hyperparameter-dan-reprodusibilitas)](#optimasi-hyperparameter-dan-reprodusibilitas)

[3.7 Evaluation [48](#evaluation)](#evaluation)

[3.7.1 Evaluasi Kinerja Klasifikasi
[48](#evaluasi-kinerja-klasifikasi)](#evaluasi-kinerja-klasifikasi)

[3.7.2 Evaluasi pada Lingkungan Federated Learning
[48](#evaluasi-pada-lingkungan-federated-learning)](#evaluasi-pada-lingkungan-federated-learning)

[3.7.3 Keterkaitan Evaluasi dengan Tujuan Penelitian
[49](#keterkaitan-evaluasi-dengan-tujuan-penelitian)](#keterkaitan-evaluasi-dengan-tujuan-penelitian)

[BAB IV HASIL EKSPERIMEN
[50](#bab-iv-hasil-eksperimen)](#bab-iv-hasil-eksperimen)

[4.1 Hasil Data Understanding
[50](#hasil-data-understanding)](#hasil-data-understanding)

[4.1.1 Distribusi Kelas dan Implikasi Non-IID
[50](#distribusi-kelas-dan-implikasi-non-iid)](#distribusi-kelas-dan-implikasi-non-iid)

[4.1.2 Kualitas dan Integritas Data
[51](#kualitas-dan-integritas-data)](#kualitas-dan-integritas-data)

[4.1.3 Karakteristik statistic dan Relevansi Fitur
[52](#karakteristik-statistic-dan-relevansi-fitur)](#karakteristik-statistic-dan-relevansi-fitur)

[4.2 Hasil Data Preparation
[54](#hasil-data-preparation)](#hasil-data-preparation)

[4.2.1 Implementasi Pembersihan Data
[54](#implementasi-pembersihan-data)](#implementasi-pembersihan-data)

[4.2.2 Transformasi dan Seleksi Fitur
[55](#transformasi-dan-seleksi-fitur)](#transformasi-dan-seleksi-fitur)

[4.2.3 Hasil Pembagian Data (Data Splitting)
[56](#hasil-pembagian-data-data-splitting)](#hasil-pembagian-data-data-splitting)

[4.2.4 Implementasi Pipeline (Core Code)
[56](#implementasi-pipeline-core-code)](#implementasi-pipeline-core-code)

[4.2.5 Output Artifacts [58](#output-artifacts)](#output-artifacts)

[4.3 Modeling dan Implementasi Sistem
[58](#modeling-dan-implementasi-sistem)](#modeling-dan-implementasi-sistem)

[4.3.1 Konfigurasi Lingkungan Eksperimen
[59](#konfigurasi-lingkungan-eksperimen)](#konfigurasi-lingkungan-eksperimen)

[4.3.2 Strategi Horizontal Federated Learning
[59](#strategi-horizontal-federated-learning-1)](#strategi-horizontal-federated-learning-1)

[4.3.3 Implementasi Arsitektur Deep Learning
[60](#implementasi-arsitektur-deep-learning)](#implementasi-arsitektur-deep-learning)

[4.3.4 Simulasi Distribusi Data Non-IID
[62](#simulasi-distribusi-data-non-iid)](#simulasi-distribusi-data-non-iid)

[4.3.5 Implementasi Federated Learning dengan Flower
[66](#implementasi-federated-learning-dengan-flower)](#implementasi-federated-learning-dengan-flower)

[4.3.6 Simulasi Distribusi Data Non-IID
[67](#simulasi-distribusi-data-non-iid-1)](#simulasi-distribusi-data-non-iid-1)

[4.4 Analisis Federated Learning dari Eksperiment
[71](#analisis-federated-learning-dari-eksperiment)](#analisis-federated-learning-dari-eksperiment)

[4.4.1 Gambaran Umum Hasil Eksperimen (Global Metrics)
[71](#gambaran-umum-hasil-eksperimen-global-metrics)](#gambaran-umum-hasil-eksperimen-global-metrics)

[4.4.2 Analisis Performa Arsitektur Model: MLP vs CNN (Skenario
Baseline)
[74](#analisis-performa-arsitektur-model-mlp-vs-cnn-skenario-baseline)](#analisis-performa-arsitektur-model-mlp-vs-cnn-skenario-baseline)

[4.4.3 Dampak Heterogenitas Data: IID vs Non-IID
[75](#dampak-heterogenitas-data-iid-vs-non-iid)](#dampak-heterogenitas-data-iid-vs-non-iid)

[4.4.4 Analisis Efektivitas Algoritma: FedAvg vs FedProx
[77](#analisis-efektivitas-algoritma-fedavg-vs-fedprox)](#analisis-efektivitas-algoritma-fedavg-vs-fedprox)

[4.4.5 Analisis Sensitivitas Parameter Proximal $\mathbf{\mu}$
[80](#analisis-sensitivitas-parameter-proximal-mathbfmu)](#analisis-sensitivitas-parameter-proximal-mathbfmu)

[4.5 Dokumentasi Hasil Penelitian
[82](#dokumentasi-hasil-penelitian)](#dokumentasi-hasil-penelitian)

[BAB V Kesimpulan [84](#bab-v-kesimpulan)](#bab-v-kesimpulan)

[5.1 Kesimpulan [84](#kesimpulan)](#kesimpulan)

[5.2 Saran [85](#saran)](#saran)

[DAFTAR PUSTAKA [87](#daftar-pustaka)](#daftar-pustaka)

[LAMPIRAN [91](#lampiran)](#lampiran)

## DAFTAR TABEL

[Tabel 2.1 Connection Features [10](#_Ref217636046)](#_Ref217636046)

[Tabel 2.2 Statiscal Features [10](#_Ref475774222)](#_Ref475774222)

[Tabel 2.3 Statiscal Features [11](#_Hlk217629630)](#_Hlk217629630)

[Tabel 2.4 SSL Features [11](#_Toc217653217)](#_Toc217653217)

[Tabel 2.5 HTTP Features [12](#_Toc217653218)](#_Toc217653218)

[Tabel 2.6 HTTP Features [13](#_Toc217653219)](#_Toc217653219)

[Tabel 2.7 Labelling Attributes [13](#_Toc217653220)](#_Toc217653220)

[Tabel 2.8 Distribusi Data dan Karakteristik Kelas
[14](#_Toc217653221)](#_Toc217653221)

[Tabel 2.9 Penelitian Terkait [27](#_Toc217653222)](#_Toc217653222)

[Tabel 3.1 Hardware [36](#_Toc217653223)](#_Toc217653223)

[Tabel 3.2 Perangkat Lunak dan Pustaka Pendukung
[36](#_Toc217653224)](#_Toc217653224)

[Tabel 4.1 Statistik Deskriptif Fitur Utama per Tipe Serangan
[53](#_Toc217653225)](#_Toc217653225)

[Tabel 4.2 Strategi Implementasi Penanganan Missing Values
[55](#_Toc217653226)](#_Toc217653226)

[Tabel 4.3 Pemetaan Label Encoding (*Multi-class*)
[55](#_Toc217653227)](#_Toc217653227)

[Tabel 4.4 Dimensi Data Hasil Preprocessing
[56](#_Toc217653228)](#_Toc217653228)

[Tabel 4.5 Konfigurasi Lingkungan Tetap
[59](#_Ref217634792)](#_Ref217634792)

[Tabel 4.6 Distribusi Binary (α=0.3 - Non-IID)
[62](#_Ref217634890)](#_Ref217634890)

[Tabel 4.7 Distribusi Binary (α=5 - IID)
[63](#_Ref217634915)](#_Ref217634915)

[Tabel 4.8 Distribusi Binary (α=0.3 - Non-IID)
[64](#_Ref217634957)](#_Ref217634957)

[Tabel 4.9 Distribusi Binary (α=5 - IID)
[64](#_Ref217634964)](#_Ref217634964)

[Tabel 4.10 Distribusi Binary (α=0.3 -- Non-IID)
[67](#_Ref217635064)](#_Ref217635064)

[Tabel 4.11 Distribusi Binary (α=5 -- IID)
[69](#_Ref217635093)](#_Ref217635093)

[Tabel 4.12 Perbandingan Performa Algoritma (Global Metrics) pada
Skenario IID [72](#_Ref217635177)](#_Ref217635177)

[Tabel 4.13 Detail Per Kelas (F1-Score) untuk CNN Multi-class pada
Skenario IID [72](#_Ref217635204)](#_Ref217635204)

[Tabel 4.14 Efisiensi Waktu Pelatihan (Training Cost) pada Skenario IID
[73](#_Ref217635233)](#_Ref217635233)

[Tabel 4.15 Perbandingan Performa Algoritma (Global Metrics) pada
Skenario Non-IID (Dirichlet α=0.3) [75](#_Ref217635680)](#_Ref217635680)

[Tabel 4.16 Detail Per Kelas (F1-Score) untuk CNN Multi-class pada
Skenario Non-IID (Dirichlet α=0.3) [77](#_Ref217635632)](#_Ref217635632)

[Tabel 4.17 Efisiensi Waktu Pelatihan (Training Cost) pada Skenario
Non-IID [79](#_Ref217635607)](#_Ref217635607)

[*Tabel 4.18 Perilaku FedProx terhadap Variasi Parameter Proximal (μ)
pada Skenario IID dan Non-IID* [80](#_Ref217635723)](#_Ref217635723)

## DAFTAR GAMBAR

[Gambar 2.1 Ilustrasi *Horizontal Federated Learning*
[16](#_Ref465798961)](#_Ref465798961)

[Gambar 2.2 Ilustrasi *Horizontal Federated Learning*
[24](#_Toc217653244)](#_Toc217653244)

[Gambar 3.1 Alur kerja penelitian [35](#_Ref217646411)](#_Ref217646411)

[Gambar 4.1 Distribusi kategori serangan pada dataset ToN-IoT Network
[51](#_Toc217653246)](#_Toc217653246)

[Gambar 4.2 Persentase Missing Values pada Fitur Spesifik Protokol
[52](#_Toc217653247)](#_Toc217653247)

[Gambar 4.3 Distribusi Fitur Numerik Utama
[52](#_Toc217653248)](#_Toc217653248)

[Gambar 4.4 Distribusi Fitur Numerik Utama
[53](#_Toc217653249)](#_Toc217653249)

[Gambar 4.5 Heatmap Korelasi Pearson Antar Fitur Numerik
[54](#_Toc217653250)](#_Toc217653250)

[Gambar 4.6 Pipeline Klasifikasi *Binary Class*
[57](#_Toc217653251)](#_Toc217653251)

[Gambar 4.7 Pipeline Klasifikasi *Binary Class*
[58](#_Toc217653252)](#_Toc217653252)

[Gambar 4.8 konfigurasi Tetap [59](#_Ref217634817)](#_Ref217634817)

[Gambar 4.9 Pipeline MLP [61](#_Toc217653254)](#_Toc217653254)

[Gambar 4.10 Pipeline CCN-1D [62](#_Toc217653255)](#_Toc217653255)

[Gambar 4.11 Pipeline *Dirichlet* [62](#_Toc217653256)](#_Toc217653256)

[Gambar 4.12 Pipeline klient [66](#_Toc217653257)](#_Toc217653257)

[Gambar 4.13 Contoh inisiasi server *Federated Learning*
[67](#_Toc217653258)](#_Toc217653258)

[Gambar 4.14 Confusion Matrix FedAvg pada Skenario IID (MLP Binary, CNN
Binary, MLP Multi-class, CNN Multi-class)
[74](#_Ref217635364)](#_Ref217635364)

[Gambar 4.15 Confusion Matrix FedAvg pada Skenario Non-IID (MLP Binary,
CNN Binary, MLP Multi-class, CNN Multi-class)
[76](#_Toc217653260)](#_Toc217653260)

[Gambar 4.16 Confusion Matrix FedProx (μ=0.01) pada Skenario Non-IID
[78](#_Ref217635527)](#_Ref217635527)

[Gambar 4.17 Confusion Matrix FedProx (μ=0.001) pada Skenario Non-IID
[79](#_Ref217635551)](#_Ref217635551)

[Gambar 4.18 Confusion Matrix FedProx (μ=0.01) pada Skenario IID
[81](#_Ref217635768)](#_Ref217635768)

[Gambar 4.19 Confusion Matrix FedProx (μ=0.001) pada Skenario IID
[82](#_Toc217653264)](#_Toc217653264)

## BAB I PENDAHULUAN

### Latar belakang

Seiring perkembangan teknologi digital, internet telah menjadi kebutuhan
fundamental dalam kehidupan modern. Pada tahun 2025, lebih dari 6 miliar
orang di seluruh dunia memiliki akses internet, dengan lebih dari 70%
populasi global menggunakan perangkat yang terhubung ke jaringan digital
(Statista, 2025). Pertumbuhan konektivitas ini mendorong berbagai kota
untuk mengadopsi konsep *Smart City*, yang memanfaatkan teknologi
*Internet of Things* (IoT) dan interkoneksi jaringan untuk meningkatkan
efisiensi layanan publik. Lebih dari 2,000 kota di dunia telah
mengimplementasikan inisiatif *Smart City*, mulai dari sistem
transportasi , pengelolaan energi, hingga layanan kesehatan dan keamanan
publik (Barker & Brooks, 2023). Namun, semakin berkembangnya
infrastruktur jaringan digital juga meningkatkan permukaan serangan
(attack surface) yang rentan terhadap ancaman siber.

*Smart City* menuntut pengelolaan jaringan yang kompleks dan
terdistribusi. *Smart City* umumnya memiliki puluhan hingga ratusan
*gateway* dan router yang menghubungkan ribuan perangkat IoT, sensor,
dan sistem kontrol. Setiap *gateway* berfungsi sebagai titik agregasi
yang mengelola lalu lintas data dari perangkat di sekitarnya sebelum
diteruskan ke sistem pusat atau *cloud*. *Gateway* tidak hanya sebagai
jalur komunikasi, tetapi juga sebagai titik kritis yang memantau dan
memfilter trafik untuk menjaga integritas dan keamanan data.
Ketergantungan pada jaringan ini membuat pengelolaan *gateway* menjadi
penting, karena gangguan atau serangan pada salah satu titik akses dapat
berdampak pada layanan publik, mulai dari transportasi hingga sistem
darurat.

Seiring meningkatnya konektivitas, ancaman keamanan siber terhadap
*Smart City* juga mengalami eskalasi. Kerugian karena serangan siber
dapat proyeksikan secara global mencapai \$10,5 triliun pada 2025,
menggarisbawahi pentingnya investasi dalam infrastruktur keamanan siber
yang kokoh (Morgan, 2025). Intrusion Detection System (IDS) menjadi
mekanisme utama untuk mendeteksi aktivitas mencurigakan pada lalu lintas
jaringan dengan memantau pola trafik dan mengidentifikasi anomali (Ahmad
dkk., 2021). Volume data yang besar membuat pendekatan berbasis machine
learning semakin relevan, karena model dapat mempelajari pola serangan
dari data historis dan mendeteksi anomali secara otomatis (Panahi dkk.,
t.t.).

Pendekatan pembelajaran terdistribusi menawarkan solusi untuk mengatasi
keterbatasan tersebut. *Federated Learning* (FL) memungkinkan pelatihan
model dilakukan secara lokal di masing-masing *gateway* tanpa
memindahkan data mentah ke server pusat (McMahan dkk., 2023). Setiap
*gateway* melatih model IDS secara lokal, kemudian hanya mengirim
pembaruan model ke server pusat untuk digabung menjadi model global.
Pendekatan ini sesuai untuk lingkungan dengan banyak *gateway*, karena
mengurangi beban komunikasi dan memungkinkan pelatihan paralel tanpa
mengorbankan data lokal (Thantharate & T, 2023).

Namun, penerapan *Federated Learning* pada *Smart City* menghadapi
tantangan. Data yang dikumpulkan tiap *gateway* berbeda berdasarkan
lokasi, waktu, dan jenis layanan. Sebagai contoh, *gateway* untuk sistem
transportasi publik memiliki pola trafik berbeda dengan *gateway* di
fasilitas kesehatan atau area residensial. Kondisi ini menghasilkan
distribusi data yang tidak seragam, atau *Non-Independent and
Identically Distributed* (Non-IID) (Al-Huthaifi dkk., 2023). Non-IID
dapat menyebabkan ketidakstabilan dalam pelatihan model, karena model
lokal pada satu *gateway* mungkin berbeda signifikan dari *gateway*
lainnya, sehingga performa model global bisa menurun (Li dkk., 2020).
Tantangan ini menjadi fokus penelitian agar IDS berbasis FL tetap
efektif dan andal dalam mendeteksi serangan pada Smart City yang
kompleks (Li dkk., 2020).

### Rumusan Masalah

Penelitian ini membahas beberapa permasalahan utama:

a.  Bagaimana penerapan Federated Learning serta implikasi performanya
    untuk deteksi dan klasifikasi serangan pada lalu lintas jaringan
    *smart city*.

b.  Bagaimana pengaruh perbedaan distribusi data antar klien terhadap
    performa sistem IDS berbasis FL.

c.  Bagaimana perbandingan performa beberapa pendekatan FL dan
    arsitektur model pada skenario tersebut.

### Batasan Masalah

Penelitian ini berfokus pada penerapan Federated Learning untuk deteksi
dan klasifikasi serangan pada lalu lintas jaringan *smart city*:

a.  Dataset yang digunakan adalah ToN-IoT subset network traffic, yang
    merepresentasikan lalu lintas jaringan dengan beberapa jenis
    serangan pada lingkungan IoT dan jaringan konvensional

b.  Lingkungan eksperimen berupa simulasi dengan beberapa klien yang
    merepresentasikan *gateway* atau *node* jaringan terdistribusi.

c.  Algoritma Federated Learning yang dibandingkan terbatas pada
    Federated Averaging (FedAvg) dan Federated Proximal (FedProx). 4.

d.  Arsitektur model yang dievaluasi terbatas pada Multi-Layer
    Perceptron (MLP) dan Convolutional Neural Network (CNN) 1D untuk dua
    skenario klasifikasi, yaitu binary dan *multi-class*.

e.  Fokus penelitian adalah simulasi dan analisis performa sistem, tidak
    mencakup deployment pada infrastruktur fisik *smart city* atau
    optimisasi perangkat embedded.

### Tujuan Penelitian

Penelitian ini memiliki beberapa tujuan:

a.  Mengkaji penerapan Federated Learning untuk sistem deteksi dan
    klasifikasi serangan pada lalu lintas jaringan *smart city*
    Menggunakan dataset ToN-IoT

b.  Menganalisis pengaruh heterogenitas data antar klien terhadap
    performa sistem NIDS berbasis *Federated Learning*.

c.  Membadingkan performa algoritma *Federated Averaging* (FedAvg) dan
    *Federated Proximal* (FedProx) dalam konteks deteksi intrusi.

d.  Mengevaluasi performa dua arsitektur model, yaitu *MLP* dan CNN 1D
    pada skenario *binary* dan *multi-class classification*.

e.  Memberikan rekomendasi praktis terkait pemilihan algoritma dan
    arsitektur model untuk implementasi NIDS berbasis *Federated
    Learning*pada lingkungan jaringan heterogen, disesuaikan kembali
    dengan konteks lapangan.

### Manfaat Penelitian 

Penelitian ini diharapkan memberikan manfaat bagi beberapa pihak, baik
secara akademis maupun praktis:

a.  Manfaat Akademis:

    Penelitian ini diharapkan dapat menambah referensi ilmiah terkait
    penerapan *Federated Learning* pada sistem deteksi intrusi jaringan,
    khususnya pada kondisi data heterogen (Non-IID).

b.  Manfaat Praktis:

    Penelitian ini diharapkan dapat menjadi acuan awal bagi praktisi
    keamanan jaringan dalam memilih algoritma dan arsitektur model pada
    implementasi FL-based IDS tanpa memusatkan data sensitif.

### Metodologi Penelitian

Penelitian ini menggunakan pendekatan *CRISP-DM* (Cross-Industry
Standard Process for Data Mining) untuk memastikan proses penelitian
sistematis dan terstruktur. Metodologi yang diterapkan mencakup lima
tahap sebagai berikut:

a.  Business Understanding

    Menelaah kebutuhan *smart city* terkait keamanan jaringan dan
    memahami karakteristik dataset lalu lintas IoT yang digunakan untuk
    *Network Intrusion Detection System* (NIDS). Tujuannya adalah untuk
    menetapkan fokus penelitian dan sasaran performa sistem yang akan
    dibangun.

b.  Data Understanding

    Melakukan eksplorasi dan verifikasi terhadap data yang dikumpulkan,
    termasuk memahami distribusi trafik jaringan, jenis serangan, dan
    karakteristik heterogen antar *gateway* atau *node*. Tahap ini
    bertujuan memastikan kualitas dan relevansi data untuk analisis
    lebih lanjut.

c.  Data Preparation

    Memproses data mentah agar siap digunakan dalam pembelajaran mesin,
    termasuk tahap filtering, normalisasi, dan pembagian data ke subset
    yang merepresentasikan masing-masing klien/*gateway*. Persiapan data
    ini penting untuk memastikan setiap *node* memiliki data yang sesuai
    untuk pelatihan lokal dalam skema *Federated Learning*.

d.  Modeling

    Mengonfigurasi skenario *Federated Learning horizontal*, dimana
    setiap klien melatih model secara lokal menggunakan data
    masing-masing. Model lokal kemudian digabungkan menjadi model global
    melalui algoritma *Federated Averaging* (FedAvg). Tahap ini fokus
    pada pengembangan dan penerapan model machine learning sederhana
    untuk deteksi intrusi.

e.  Evaluation

    Menilai performa model global yang dihasilkan menggunakan metrik
    numerik seperti akurasi dan *F1-score*. Evaluasi juga
    mempertimbangkan aspek efisiensi, termasuk jumlah iterasi komunikasi
    dan waktu pelatihan. Tahap ini bertujuan untuk memastikan model
    dapat mendeteksi serangan dengan efektif di lingkungan *smart city*
    yang heterogen.

### Metodologi Penelitian

Untuk memberikan gambaran yang singkat tentang penelitian ini, penulisan
disusun dalam lima bab yang saling berhubungan. Penyusunan penelitian
ini mengikuti kaidah penulisan ilmiah dengan sistematika sebagai
berikut:

1.  BAB I PENDAHULUAN

    Bab ini berisi latar belakang yang menjelaskan konteks *smart city*,
    tantangan keamanan jaringan, keterbatasan pendekatan terpusat, dan
    pengenalan *Federated Learning* sebagai solusi alternatif. Selain
    itu, bab ini juga memuat rumusan masalah, batasan masalah, tujuan
    penelitian, manfaat penelitian, metodologi penelitian, dan
    sistematika penulisan.

2.  BAB II LANDASAN TEORI

    Bab ini berisi teori-teori yang menjadi dasar penelitian, mencakup
    *Network Intrusion Detection System* (NIDS), konsep *Federated
    Learning*, algoritma *Federated Averaging* (FedAvg) dan *Federated
    Proximal* (FedProx), arsitektur model *deep learning* (MLP dan CNN
    1D), distribusi Non-IID dengan *Dirichlet*, dataset ToN-IoT, metrik
    evaluasi, serta tinjauan penelitian terkait.

3.  BAB III METODOLOGI PENELITIAN

    Bab ini berisi kerangka kerja penelitian yang mengadaptasi
    *CRISP-DM* untuk konteks *Federated Learning*, meliputi tahapan
    *Business Understanding*, *Data Understanding*, *Data Preparation*,
    partisi data Non-IID, pemilihan arsitektur model dan algoritma,
    *hyperparameter tuning* dengan *Grid Search*, rencana implementasi
    FedAvg dan FedProx, serta metode evaluasi yang digunakan.

4.  BAB IV HASIL DAN PEMBAHASAN

    Bab ini berisi hasil eksplorasi data, *preprocessing*, partisi data
    Non-IID, hasil *hyperparameter tuning*, perbandingan performa
    algoritma *Federated Averaging* dan *Federated Proximal* pada
    kondisi data heterogen, analisis pengaruh parameter α dan μ,
    perbandingan arsitektur model *MLP* dan CNN, serta diskusi implikasi
    praktis dari temuan penelitian.

5.  BAB V KESIMPULAN DAN SARAN

    Bab ini berisi kesimpulan yang diperoleh dari hasil penelitian
    terkait efektivitas *Federated Learning* untuk deteksi intrusi pada
    lalu lintas jaringan *smart city*, serta saran-saran untuk
    penelitian lanjutan dan implementasi praktis di masa depan.

## BAB II LANDASAN TEORI

Bab ini menyusun landasan teori yang menjadi dasar bagi perancangan dan
analisis sistem dalam penelitian ini. Pembahasan diawali dengan *Network
Intrusion Detection System* (NIDS) sebagai komponen fundamental dalam
deteksi serangan jaringan. Selanjutnya, kerangka kerja *CRISP-DM*
(Cross-Industry Standard Process for Data Mining) digunakan untuk
menstrukturkan alur penelitian secara metodologis. Aspek data dibahas
melalui karakteristik dataset yang digunakan serta tahapan
*preprocessing* yang diterapkan guna memastikan kesiapan data sebelum
pemodelan. Fokus kemudian diarahkan pada tahapan *modeling*, khususnya
arsitektur dan algoritma yang digunakan dalam skema *Federated
Learning*. Lalu terdapat fokus untuk mecari *hyperparameter* yang
optimal secara komputasi. Terakhir, bab ini ditutup dengan pembahasan
teknik evaluasi yang digunakan sebagai dasar penilaian kinerja sistem.

### Network Intrusion Detection System

*Network Intrusion Detection System* (NIDS) merupakan sistem perangkat
lunak yang berfungsi untuk memantau lalu lintas jaringan secara kontinu
dengan tujuan mendeteksi aktivitas yang mencurigakan atau pelanggaran
kebijakan keamanan. Dalam arsitektur keamanan siber, NIDS berperan
sebagai mekanisme pertahanan awal yang menganalisis aliran paket data
guna mengidentifikasi indikasi serangan sebelum berdampak langsung pada
sistem yang dilindungi (Feng & Sakurai, 2025). Berdasarkan mekanisme
pendeteksiannya, NIDS secara umum diklasifikasikan ke dalam dua
pendekatan utama, yaitu *signature-based detection* dan *anomaly-based
detection*.

Pendekatan signature-based detection bekerja dengan melakukan pencocokan
pola (pattern matching) antara lalu lintas jaringan yang diamati dan
basis data tanda tangan (signature) serangan yang telah diketahui
sebelumnya. Apabila karakteristik paket data yang dianalisis sesuai
dengan salah satu signature dalam basis data, sistem akan menghasilkan
peringatan atau mengambil tindakan mitigasi yang telah ditentukan (Feng
& Sakurai, 2025). Pendekatan ini memiliki tingkat akurasi yang tinggi
serta tingkat false positive yang relatif rendah untuk serangan yang
telah terdokumentasi. Namun, keterbatasan utamanya terletak pada
ketergantungan terhadap pembaruan basis data, sehingga metode ini tidak
efektif dalam mendeteksi serangan baru atau zero-day attacks yang belum
memiliki pola yang terdefinisi.

Berbeda dengan pendekatan berbasis *signature-based*, *anomaly-based
detection* berfokus pada pembentukan model perilaku normal lalu lintas
jaringan sebagai acuan deteksi. Model ini dibangun menggunakan
pendekatan statistik atau teknik pembelajaran mesin (machine learning)
untuk mempelajari pola trafik yang dianggap normal. Aktivitas jaringan
kemudian dievaluasi berdasarkan tingkat penyimpangannya terhadap
baseline tersebut, di mana deviasi yang signifikan diasumsikan sebagai
indikasi serangan atau anomali (Bierbrauer dkk., 2025a). Keunggulan
pendekatan ini terletak pada kemampuannya dalam mendeteksi pola serangan
baru yang tidak terdefinisi sebelumnya. Oleh karena itu, penelitian ini
mengadopsi pendekatan *anomaly-based detection* karena lebih sesuai
dengan karakteristik lingkungan IoT yang dinamis dan memiliki variasi
pola lalu lintas yang tinggi.

### CRIPS-DM

*Cross-Industry Standard Process for Data Mining* (CRISP-DM) merupakan
kerangka kerja proses yang digunakan secara luas untuk merancang dan
mengelola proyek berbasis data. Kerangka ini menyediakan struktur
metodologis yang jelas dalam menghubungkan tujuan penelitian dengan
tahapan teknis pengolahan dan analisis data (Schröer dkk., 2021). Dalam
*CRISP-DM*, siklus penelitian dibagi ke dalam enam tahap utama yang
saling berkaitan sebagai berikut.

a.  *Business Understanding*

> Tahap business understanding berfokus pada perumusan tujuan penelitian
> dan permasalahan utama yang ingin diselesaikan. Dalam konteks
> penelitian ini, tahap ini digunakan untuk mendefinisikan kebutuhan
> keamanan jaringan *smart city* serta batasan penggunaan data,
> khususnya terkait penerapan Federated Learning sebagai pendekatan yang
> menjaga privasi data antar *node* jaringan (Schröer dkk., 2021).

b.  *Data Understanding*

> Tahap *data understanding* mencakup eksplorasi awal terhadap dataset
> yang digunakan, termasuk identifikasi karakteristik lalu lintas
> jaringan, distribusi kelas serangan, serta potensi permasalahan
> kualitas data. Tahap ini bertujuan memastikan data yang digunakan
> relevan dan layak untuk proses analisis dan pemodelan lebih lanjut
> (Schröer dkk., 2021).

c.  *Data Preparation*

> Tahap *data preparation* mencakup seluruh proses pengolahan data
> mentah hingga siap digunakan dalam pemodelan. Kegiatan pada tahap ini
> meliputi pembersihan data, transformasi fitur, serta pembagian data ke
> dalam subset yang merepresentasikan masing-masing klien dalam skema
> *Federated Learning* (Schröer dkk., 2021).

d.  *Modeling*

> Pada tahap *modeling*, arsitektur model pembelajaran mesin serta
> algoritma *Federated Learning* dipilih dan diterapkan sesuai dengan
> tujuan penelitian. Tahap ini mencakup konfigurasi model lokal pada
> masing-masing klien, penentuan parameter pelatihan, serta mekanisme
> agregasi model global (Schröer dkk., 2021).

e.  Evaluation

> Digunakan untuk menilai performa model global yang dihasilkan
> berdasarkan metrik evaluasi yang telah ditetapkan, seperti akurasi dan
> *F1-score*. Selain performa prediktif, evaluasi juga mempertimbangkan
> aspek efisiensi proses pelatihan dan stabilitas model pada kondisi
> distribusi data yang heterogen (Schröer dkk., 2021).

f.  *Deployment*

> Pada *CRISP-DM* secara umum mencakup penerapan model ke lingkungan
> operasional. Namun, dalam penelitian ini, tahap deployment dibatasi
> pada penyajian hasil eksperimen dan analisis performa sebagai bukti
> konsep, tanpa implementasi langsung pada infrastruktur *smart city*
> yang sebenarnya (Schröer et al., 2021).

### Dataset UNSW: ToN IoT

Dataset ToN-IoT merupakan dataset lalu lintas jaringan heterogen yang
dikembangkan oleh Cyber Range Lab, UNSW Canberra, untuk mendukung
penelitian deteksi intrusi pada lingkungan *Internet of Things* (IoT)
dan Industrial IoT (IIoT) (Moustafa, 2021). Dataset ini dikumpulkan dari
sebuah testbed yang dirancang menyerupai lingkungan jaringan nyata, di
mana layanan IoT/IIoT terintegrasi dengan infrastruktur jaringan
konvensional melalui arsitektur berlapis yang terdiri dari *edge*,
*fog*, dan *cloud*. Pendekatan ini memungkinkan dataset
merepresentasikan karakteristik lalu lintas jaringan yang kompleks
sebagaimana dijumpai pada skenario *smart city*.

Testbed ToN-IoT menghasilkan lalu lintas jaringan normal dan berbahaya
dengan memanfaatkan berbagai skenario serangan siber, sehingga dataset
ini banyak digunakan sebagai benchmark dalam penelitian *Network
Intrusion Detection System* (NIDS). Dataset mencakup sembilan kategori
serangan, yaitu *Distributed Denial of Service* (DDoS), *Denial of
Service* (DoS), *Ransomware*, *Backdoor*, *Injection*, *Cross-Site
Scripting* (XSS), *Password attacks*, *Scanning*, dan
*Man-in-the-Middle* (MITM), serta lalu lintas normal (Moustafa, 2021).

Secara struktural, dataset ToN-IoT terdiri dari 46 atribut yang
dikelompokkan ke dalam tujuh kategori fitur, mencerminkan informasi
koneksi, statistik trafik, serta karakteristik protokol aplikasi.
Pembagian ini memungkinkan analisis lalu lintas jaringan dilakukan dari
berbagai lapisan, mulai dari transport hingga aplikasi.

a.  Connection Features

> []{#_Ref217636046 .anchor}Tabel 2.1 Connection Features

  ------------------------------------------------------------
  **ID**        **Feature**    **Type**      **Description**
  ------------- -------------- ------------- -----------------
  1             ts             Time          Timestamp koneksi
                                             antar flow
                                             identifiers

  2             src_ip         String        Alamat IP sumber

  3             src_port       Number        Port TCP/UDP
                                             sumber

  4             dst_ip         String        Alamat IP tujuan

  5             dst_port       Number        Port TCP/UDP
                                             tujuan

  6             proto          String        Protokol
                                             transport layer

  7             service        String        Protokol yang
                                             terdeteksi
                                             dinamis (DNS,
                                             HTTP, SSL)

  8             duration       Number        Durasi koneksi
                                             paket

  9             src_bytes      Number        Bytes dari source
                                             payload

  10            dst_bytes      Number        Bytes dari
                                             destination
                                             payload

  11            conn_state     String        Status koneksi
                                             (S0, S1, REJ,
                                             dll)

  12            missed_bytes   Number        Bytes yang hilang
                                             dalam content
                                             gaps
  ------------------------------------------------------------

Sumber: (Moustafa, 2021)

> Kelompok fitur ini merepresentasikan informasi dasar koneksi jaringan,
> seperti alamat IP, port, protokol, durasi koneksi, serta status
> koneksi. Fitur-fitur ini memberikan gambaran umum mengenai aliran
> trafik antar *node* jaringan.

b.  Statistical Features

> []{#_Ref475774222 .anchor}Tabel 2.2 Statiscal Features

  ------------------------------------------------------------
  **ID**        **Feature**    **Type**      **Description**
  ------------- -------------- ------------- -----------------
  13            src_pkts       Number        Jumlah paket dari
                                             source

  14            src_ip_bytes   Number        Total IP header
                                             bytes dari source

  15            dst_pkts       Number        Jumlah paket dari
                                             destination

  16            dst_ip_bytes   Number        Total IP header
                                             bytes dari
                                             destination
  ------------------------------------------------------------

Sumber: (Moustafa, 2021)

> Fitur statistik menangkap karakteristik kuantitatif lalu lintas
> jaringan, seperti jumlah paket dan total *byte* yang ditransmisikan,
> yang sering digunakan untuk mengidentifikasi pola anomali berbasis
> volume trafik.

c.  DNS Features[]{#_Hlk217629630 .anchor}

> Tabel 2.3 Statiscal Features

  ------------------------------------------------------------
  **ID**        **Feature**    **Type**      **Description**
  ------------- -------------- ------------- -----------------
  17            dns_query      String        Domain name dari
                                             DNS queries

  18            dns_qclass     Number        DNS query class

  19            dns_qtype      Number        DNS query type

  20            dns_rcode      Number        Response code DNS

  22            dns_RD         Boolean       Recursion desired
                                             (T/F)

  23            dns_RA         Boolean       Recursion
                                             available (T/F)

  24            dns_rejected   Boolean       DNS query
                                             rejected (T/F)
  ------------------------------------------------------------

Sumber: (Moustafa, 2021)

> Kelompok fitur DNS berisi informasi terkait permintaan dan respons
> *domain name system*, yang relevan untuk mendeteksi aktivitas
> mencurigakan seperti tunneling atau penyalahgunaan layanan DNS.

d.  SSL Features

> []{#_Toc217653217 .anchor}Tabel 2.4 SSL Features

  ---------------------------------------------------------------
  **ID**        **Feature**       **Type**      **Description**
  ------------- ----------------- ------------- -----------------
  25            ssl_version       String        Versi SSL yang
                                                ditawarkan server

  26            ssl_cipher        String        SSL cipher suite
                                                yang dipilih

  27            ssl_resumed       Boolean       Session dapat
                                                digunakan untuk
                                                koneksi baru

  28            ssl_established   Boolean       Koneksi SSL
                                                berhasil
                                                established

  29            ssl_subject       String        Subject dari
                                                X.509 certificate

  30            ssl_issuer        String        Certificate
                                                authority
  ---------------------------------------------------------------

Sumber: (Moustafa, 2021)

> Fitur SSL merepresentasikan karakteristik koneksi terenkripsi,
> termasuk versi protokol, *cipher suite*, serta informasi sertifikat,
> yang dapat digunakan untuk menganalisis perilaku koneksi aman yang
> tidak wajar.

e.  HTTP Features

> []{#_Toc217653218 .anchor}Tabel 2.5 HTTP Features

  ----------------------------------------------------------------------
  **ID**        **Feature**              **Type**      **Description**
  ------------- ------------------------ ------------- -----------------
  31            http_trans_depth         Number        Pipelined depth
                                                       koneksi HTTP

  32            http_method              String        HTTP method (GET,
                                                       POST, HEAD)

  33            http_uri                 String        URI dalam request
                                                       HTTP

  34            http_referrer            String        Nilai header
                                                       referer

  35            http_version             String        Versi HTTP (1.1,
                                                       dll)

  36            http_request_body_len    Number        Ukuran content
                                                       dari HTTP client

  37            http_response_body_len   Number        Ukuran content
                                                       dari HTTP server

  38            http_status_code         Number        Status code HTTP

  39            http_user_agent          Number        Nilai header
                                                       User-Agent

  40            http_orig_mime_types     String        MIME types dari
                                                       source

  41            http_resp_mime_types     String        MIME types dari
                                                       destination
  ----------------------------------------------------------------------

Sumber: (Moustafa, 2021)

> Kelompok fitur HTTP merepresentasikan aktivitas pada lapisan aplikasi,
> yang sangat penting untuk mendeteksi serangan berbasis web seperti
> *Injection* atau *Cross-Site Scripting* (XSS). Fitur-fitur ini
> memungkinkan sistem untuk menganalisis isi permintaan klien dan
> respons server guna mengidentifikasi pola akses yang tidak wajar atau
> muatan paket yang mencurigakan.

f.  Violation Features

> []{#_Toc217653219 .anchor}Tabel 2.6 HTTP Features

  ----------------------------------------------------------------
  **ID**        **Feature**        **Type**      **Description**
  ------------- ------------------ ------------- -----------------
  31            http_trans_depth   Number        Pipelined depth
                                                 koneksi HTTP

  32            http_method        String        HTTP method (GET,
                                                 POST, HEAD)

  33            http_uri           String        URI dalam request
                                                 HTTP

  34            http_referrer      String        Nilai header
                                                 referer
  ----------------------------------------------------------------

Sumber: (Moustafa, 2021)

> Kelompok fitur ini mencatat anomali atau pelanggaran protokol yang
> terdeteksi selama sesi komunikasi berlangsung. Fitur-fitur ini sangat
> berguna untuk mengidentifikasi aktivitas yang menyimpang dari standar
> protokol jaringan (RFC) yang sering kali menjadi indikasi awal adanya
> upaya eksploitasi. Atribut ini membantu model dalam menangkap perilaku
> paket yang tidak standar, seperti malformasi paket atau
> ketidaksesuaian struktur protokol, yang sulit dideteksi hanya melalui
> fitur statistik biasa.

g.  Labelling Attributes

> []{#_Toc217653220 .anchor}Tabel 2.7 Labelling Attributes

  ------------------------------------------------------------
  **ID**        **Feature**    **Type**      **Description**
  ------------- -------------- ------------- -----------------
  45            label          Number        Tag normal (0)
                                             dan attack (1)

  46            type           String        Kategori serangan
                                             (normal, DoS,
                                             DDoS, backdoor,
                                             dll)
  ------------------------------------------------------------

Sumber: (Moustafa, 2021)

> Kelompok fitur ini merupakan atribut target yang digunakan untuk
> proses pembelajaran model. Atribut ini memberikan informasi mengenai
> status keamanan dari setiap baris data dalam dataset. Fitur *label*
> digunakan untuk skenario *binary classification*, sedangkan fitur
> *type* digunakan untuk skenario *multi-class classification* guna
> mengidentifikasi jenis serangan secara lebih mendetail.

h.  Distribusi Data dan Karakteristik Kelas

> Penelitian ini menggunakan subset *train network* dari dataset ToN-IoT
> sebagai data referensi dalam proses pemodelan. Distribusi jumlah
> record untuk setiap kategori trafik dan serangan disajikan pada tabel
> berikut.
>
> []{#_Toc217653221 .anchor}Tabel 2.8 Distribusi Data dan Karakteristik
> Kelas

  ----------------------------------------------------------
  **Attack Type**    **Total Record (Full **Train Test
                     Dataset)**           Network Record**
  ------------------ -------------------- ------------------
  backdoor           508,116              20,000

  ddos               6,165,008            20,000

  dos                3,375,328            20,000

  injection          452,659              20,000

  mitm               1,052                1,043

  password           1,718,568            20,000

  ransomware         72,805               20,000

  scanning           7,140,161            20,000

  xss                2,108,944            20,000

  normal             796,380              50,000
  ----------------------------------------------------------

Sumber: (Moustafa, 2021)

> Karakteristik utama yang menonjol dari dataset ini adalah ketimpangan
> distribusi kelas (*class imbalance*). Sebagai contoh, kelas
> *Man-in-the-Middle* (MITM) hanya memiliki 1,043 *record* (0,49%),
> sementara kelas normal mendominasi dengan 50,000 *record* (23,69%).
> Ketimpangan ini sengaja dipertahankan karena merepresentasikan kondisi
> riil di lingkungan jaringan, di mana serangan tertentu memiliki
> frekuensi kemunculan yang jauh lebih rendah dibandingkan aktivitas
> normal atau serangan umum lainnya (Moustafa, 2021).

Secara keseluruhan, dataset ToN-IoT menyediakan representasi lalu lintas
jaringan yang komprehensif untuk lingkungan *smart city* melalui
keragaman fitur aplikasi dan variasi kategori serangan. Karakteristik
dataset yang memiliki ketimpangan distribusi kelas (*class imbalance*)
serta volume data yang besar menjadikannya instrumen yang relevan untuk
menguji ketangguhan model deteksi intrusi. Dalam konteks penelitian ini,
subset data tersebut akan didistribusikan ke beberapa klien guna
mensimulasikan kondisi *Non-Independent and Identically Distributed*
(Non-IID), yang merupakan tantangan utama dalam implementasi *Federated
Learning* di jaringan terdistribusi.

### Teknik Pre-Processing

*Pre-processing* data adalah tahapan pengolahan data mentah untuk
meningkatkan kualitas dan efisiensi proses pembelajaran mesin. Tahapan
ini bertujuan untuk memastikan data memiliki konsistensi dan format yang
sesuai dengan persyaratan algoritma yang digunakan (Qazi dkk., 2022a).
Beberapa konsep utama dalam *pre-processing* meliputi:

a.  Penanganan Data Tidak Lengkap (*Missing Values*)\
    Dalam pengumpulan data berskala besar, sering kali terdapat
    informasi yang hilang atau tidak tercatat. Penanganan data ini dapat
    dilakukan melalui teknik penghapusan (*deletion*) atau pengisian
    nilai pengganti (*imputation*). Pemilihan teknik pengisian harus
    mempertimbangkan karakteristik data agar tidak mengubah distribusi
    asli dari informasi tersebut secara signifikan (Moustafa, 2021).

b.  Transformasi Fitur Kategorikal

> Dalam algoritma pembelajaran mesin, khususnya *deep learning*, bekerja
> atas dasar perhitungan matematis yang memerlukan input numerik. Oleh
> karena itu, fitur yang bertipe kategori harus ditransformasikan ke
> dalam representasi angka. Proses ini memastikan bahwa informasi
> kualitatif dapat diproses oleh model tanpa menghilangkan perbedaan
> antar kategori (Alsaedi dkk., 2020).

c.  Reduksi Dimensi dan Seleksi Fitur

> Seleksi fitur merupakan proses memilih atribut yang dianggap paling
> relevan dan informatif bagi model. Dengan mengurangi jumlah atribut
> yang tidak memberikan kontribusi signifikan, beban komputasi dapat
> dikurangi dan risiko *overfitting* dapat diminimalisir. Hal ini juga
> membantu model untuk lebih fokus pada pola yang benar-benar membedakan
> setiap kelas data (Al-Ghadi dkk., 2025).

d.  Penskalaan Fitur (*Feature Scaling*)

> Penskalaan fitur bertujuan untuk menyamakan rentang nilai antar
> atribut yang berbeda. Tanpa penskalaan, fitur dengan rentang nilai
> yang besar akan mendominasi perhitungan fungsi biaya dan menghambat
> efisiensi pembaruan bobot dalam model. Teknik seperti standardisasi
> memastikan seluruh fitur berada pada skala yang sebanding, sehingga
> proses pelatihan model menjadi lebih stabil (Javeed dkk., 2024).

### Federated Learning

*Federated Learning* (FL) adalah paradigma pembelajaran mesin
terdistribusi yang memungkinkan pelatihan model dilakukan secara
kolaboratif pada perangkat klien yang berbeda tanpa perlu memindahkan
data mentah ke server pusat (McMahan dkk., 2023). Prinsip utama dari
pendekatan ini adalah melakukan proses komputasi di tempat data tersebut
berada, yang secara fundamental berbeda dari pendekatan pembelajaran
mesin tradisional yang bersifat tersentralisasi.

Dalam arsitektur FL, server pusat bertugas untuk mengelola model global
dan mendistribusikannya ke sejumlah klien atau *node*. Setiap klien
melatih model tersebut menggunakan data lokal mereka, kemudian hanya
mengirimkan pembaruan parameter model , seperti bobot atau *gradient*.
Lalu kembali ke server pusat untuk proses agregasi. Mekanisme ini
memberikan keunggulan dalam menjaga privasi data sensitif, mengurangi
kebutuhan akan bandwidth transmisi data besar, serta mematuhi regulasi
perlindungan data (Upreti dkk., 2024).

#### Arsitektur Horizontal Federated Learning

![[]{#_Ref465798961 .anchor}Gambar 2.1 Ilustrasi *Horizontal Federated
Learning*](media/image3.gif){alt="Figure 5" width="3.4770833333333333in"
height="2.1590277777777778in"}

Sumber: (Upreti dkk., 2024).

Penelitian ini menggunakan skenario *Horizontal Federated Learning*
(HFL). Dalam HFL, setiap klien atau *gateway* memiliki struktur fitur
yang identik namun memiliki sampel data yang berbeda. Pendekatan ini
sangat relevan untuk ekosistem *smart city* di mana berbagai *gateway*
IoT mengumpulkan jenis parameter jaringan yang sama tetapi dari lokasi
atau populasi pengguna yang berbeda.

#### Karakteristik Distribusi Data (IID dan Non-IID)

Dalam implementasi FL, distribusi data antar klien dibagi menjadi dua
kategori utama yang sangat menentukan performa model global:

a.  *Independent and Identically Distributed* (IID)

> Independent and Identically Distributed (IID) merupakan kondisi ideal
> dalam *Federated Learning*, di mana setiap klien memiliki distribusi
> data yang serupa dengan distribusi populasi global, baik dari segi
> proporsi kelas maupun karakteristik fitur. Pada skenario ini, data
> pada masing-masing klien dapat dianggap sebagai sampel acak yang
> merepresentasikan keseluruhan dataset.
>
> Dalam kondisi IID, algoritma agregasi standar seperti *Federated
> Averaging* (FedAvg) cenderung mencapai konvergensi dengan cepat dan
> stabil, karena gradien lokal yang dihasilkan oleh setiap klien relatif
> konsisten satu sama lain. Oleh sebab itu, skenario IID sering
> digunakan sebagai baseline untuk mengevaluasi performa Federated
> Learning sebelum diuji pada kondisi yang lebih realistis dan kompleks
> (Zhu dkk., 2021).

b.  *Non-Independent and Identically Distributed* (Non-IID)

> *Non-Independent and Identically Distributed* (Non-IID) menggambarkan
> kondisi di mana distribusi data antar klien berbeda secara signifikan,
> baik dalam hal jumlah sampel, proporsi kelas, maupun pola fitur. Pada
> lingkungan *smart city*, kondisi ini muncul secara alami karena setiap
> *gateway* melayani area dengan karakteristik trafik yang berbeda,
> seperti kawasan residensial, industri, atau fasilitas publik, yang
> menghasilkan pola serangan dan lalu lintas jaringan yang tidak seragam
> (Zhu dkk., 2021).

**Dirichlet**

Untuk memodelkan dan menganalisis kondisi Non-IID secara sistematis,
sejumlah penelitian mengadopsi Distribusi Dirichlet sebagai mekanisme
matematis dalam mensimulasikan ketimpangan distribusi kelas antar klien.
Distribusi ini memungkinkan pengaturan tingkat heterogenitas data
melalui parameter konsentrasi (α), di mana nilai α yang kecil
merepresentasikan kondisi Non-IID ekstrem, sedangkan nilai α yang besar
mendekati distribusi IID. Pendekatan berbasis Dirichlet banyak digunakan
dalam penelitian Federated Learning karena fleksibilitasnya dalam
merepresentasikan berbagai tingkat ketidakseragaman data tanpa mengubah
struktur fitur dasar dataset.

Dengan demikian, penggunaan distribusi Dirichlet menjadi landasan
teoretis yang relevan untuk mengevaluasi ketahanan dan stabilitas
algoritma Federated Learning pada skenario distribusi data yang
menyerupai kondisi nyata *smart city*.

#### Algoritma Agregasi

Algoritma agregasi berperan krusial dalam menggabungkan pembaruan model
dari berbagai klien untuk membentuk satu model global yang
representatif. Penelitian ini membandingkan dua algoritma utama yang
menjadi standar dalam literatur Federated Learning.

**Federated Averaging**

Federated Averaging (FedAvg) adalah algoritma agregasi dasar yang
bekerja dengan prinsip rata-rata tertimbang (*weighted average*). Dalam
algoritma ini, server pusat melakukan inisialisasi model global,
kemudian mengirimkannya ke sejumlah klien untuk dilatih secara lokal
menggunakan data masing-masing selama beberapa *epoch*. Parameter model
global diperbarui berdasarkan rata-rata parameter model lokal yang
dibobotkan dengan jumlah sampel data pada setiap klien (McMahan dkk.,
2023).

Formula agregasi FedAvg dinyatakan sebagai berikut:

+--------------------------------------------------------------+---------------+
| $$w_{t + 1} = \sum_{k = 1}^{K}\frac{n_{k}}{n}w_{t + 1}^{k}$$ | > ( 2.1 )     |
+==============================================================+===============+

Di mana $w_{t + 1}$ adalah parameter model global pada ronde $t + 1$,
$n_{k}$ adalah jumlah sampel pada klien $k$, $n$ adalah total sampel
dari seluruh klien yang berpartisipasi, dan $w_{t + 1}^{k}$ adalah
parameter hasil pelatihan lokal pada klien $k$.

**Federated Proximal**

FedProx merupakan pengembangan dari FedAvg yang dirancang khusus untuk
mengatasi tantangan heterogenitas data (Non-IID). Algoritma ini
memperkenalkan *proximal term* pada fungsi tujuan (*loss function*)
lokal untuk membatasi agar pembaruan model lokal tidak menyimpang
terlalu jauh dari model global. Penambahan suku penalti ini secara
teoretis mampu menekan fenomena *client drift* yang merupakan fenomena
di mana model lokal pada setiap perangkat \"melenceng\" dari tujuan
global karena data yang tidak seragam (non-IID), sehingga memperlambat
konvergensi dan menurunkan akurasi model utama. Dan, sering terjadi pada
dataset heterogen seperti ToN-IoT (Li dkk., 2020).

Formula loss function pada sisi klien dalam FedProx dinyatakan sebagai
berikut:

  --------------------------------------------------------------------------------------------------------------------------------------------
  $$\min_{w}h_{k\left( w;\ w^{t} \right)} = \ F_{k(w)} + \ \left( \frac{\mu}{2} \right)\left\| w\  - \ w^{t} \right\|^{2}$$   (2.2 )
  --------------------------------------------------------------------------------------------------------------------------- ----------------

  --------------------------------------------------------------------------------------------------------------------------------------------

Di mana $F_{k(w)}$ adalah fungsi *loss* tradisional, sedangkan
$\left( \frac{\mu}{2} \right)\left\| w\  - \ w^{t} \right\|^{2}$ adalah
*proximal term* dengan *hypermarameter* $\mu$ yang mengatur kekuatan
penalti terhadap penyimpangan model lokal $w$ dari model global $w^{t}$

Tabel 2.9 Perbedaan FedAvg dengan FedProx

  ----------------------------------------------------------
           **Aspek**           **FedAvg**        **FedProx**
  ------------------ -------------------- ------------------
         Fungsi Loss      Standar (misal:     Standar dengan
                           Cross-Entropy) tambahan *Proximal
                                                       Term*

  Mekanisme Agregasi   *Weighted Average* *Weighted Average*

  Stabilitas Non-IID      Rentan terhadap   Lebih stabil dan
                             client drift          konsisten

      Hyperparameter       Learning Rate, Tambahan Koefisien
                        Epoch, Batch Size                *µ*

         Konvergensi  Cepat pada data IID Lebih lambat namun
                                                 stabil pada
                                                     Non-IID
  ----------------------------------------------------------

Perbedaan di atas menunjukkan bahwa perbedaan fundamental antara FedAvg
dan FedProx terletak pada modifikasi fungsi tujuan di sisi klien.
Sementara FedAvg mengasumsikan bahwa setiap model lokal dapat
berkontribusi secara langsung melalui rata-rata tertimbang, FedProx
mengakui adanya risiko ketidakstabilan pada data yang heterogen
(Non-IID).

Penggunaan proximal term (parameter *µ*) pada FedProx menjadi fitur
kunci yang memberikan fleksibilitas bagi model untuk beradaptasi dengan
variasi data lokal tanpa mengorbankan stabilitas model global. Meskipun
FedAvg menawarkan kecepatan konvergensi yang lebih tinggi pada kondisi
data yang seragam (IID), FedProx secara teoretis lebih stabil dalam
memitigasi dampak *client drift* yang sering terjadi pada jaringan
*smart city* yang kompleks.

### Deep Learning

*Deep Learning* merupakan sub-bidang dari *Machine Learning* yang
didasarkan pada konsep jaringan saraf tiruan (*Artificial Neural
Networks*). Perbedaan utama *Deep Learning* terletak pada penggunaan
struktur lapisan *(layer)* yang dalam dan hierarkis untuk mengekstraksi
representasi data secara otomatis. Tidak seperti algoritma tradisional
yang memerlukan rekayasa fitur manual secara intensif, *Deep Learning*
mampu mempelajari pola-pola kompleks langsung dari data mentah melalui
proses komputasi yang berlapis-lapis (LeCun dkk., 2015).

Dalam konteks keamanan jaringan, *Deep Learning* menawarkan keunggulan
dalam menangani volume data trafik yang sangat besar dan mendeteksi
anomali yang halus yang mungkin terlewatkan oleh metode berbasis
statistik konvensional. Kemampuannya untuk melakukan generalisasi
terhadap pola serangan baru menjadikan teknologi ini sangat relevan
untuk diimplementasikan dalam sistem deteksi intrusi yang dinamis (Ahmad
dkk., 2021).

Penelitian ini secara spesifik mengkaji dua arsitektur Deep Learning
sebagai model lokal dalam skema Federated Learning yaitu *Multi-Layer
Perceptron* (MLP) dan *Convolutional Neural Network* *1 Dimensional
(CNN-1D).*

#### Multi-Layer Perceptron

*Multi-Layer Perceptron* (MLP) adalah varian jaringan saraf
*feedforward* yang terdiri dari lapisan input, satu atau lebih lapisan
tersembunyi (*hidden layers*), dan lapisan output yang terhubung secara
penuh (*fully-connected*). Prinsip kerja MLP didasarkan pada kemampuan
unit perseptron untuk mempelajari pemetaan non-linear antara input dan
output melalui proses *backpropagation* (Ali dkk., 2024)

Secara matematis, operasi pada setiap lapisan MLP melibatkan perkalian
matriks bobot ($W$), penambahan bias ($b$), dan penerapan fungsi
aktivasi non-linear ($f$) untuk menghasilkan representasi fitur yang
lebih abstrak:

  ------------------------------------------------------------------------------------
  $$h^{(l)} = f\left( W^{(l)} \cdot h^{(l - 1)} + b^{(l)} \right)$$   (2.3)
  ------------------------------------------------------------------- ----------------

  ------------------------------------------------------------------------------------

Dalam konteks NIDS, MLP efektif untuk memproses data tabular seperti
statistik paket karena kemampuannya dalam menangkap hubungan kompleks
antar fitur yang telah diekstraksi. Penggunaan fungsi aktivasi seperti
*Rectified Linear Unit* (ReLU) membantu mempercepat konvergensi,
sementara *Sigmoid* atau *Softmax* digunakan pada lapisan akhir untuk
menghasilkan probabilitas prediksi serangan*.*

#### Convolutional Neural Network 1 Dimensional (CNN-1D)

*Convolutional Neural Network 1 Dimensional* (CNN-1D) merupakan adaptasi
dari arsitektur CNN yang umumnya digunakan pada data citra, namun
dioptimalkan untuk data sekuensial atau satu dimensi. Dalam deteksi
intrusi jaringan, CNN 1D bekerja dengan menggeser filter (kernel)
sepanjang urutan fitur untuk mengekstraksi pola lokal pada urutan atau
hubungan antar fitur yang berdekatan (Ahmad dkk., 2021).

Secara matematis, operasi pada lapisan konvolusi melibatkan pergeseran
filter (kernel) di atas data input, di mana setiap elemen filter
dikalikan dengan nilai input yang sesuai dan dijumlahkan untuk
menghasilkan feature map. Operasi konvolusi 1D didefinisikan sebagai
berikut:

  --------------------------------------------------------------------------------------------------------------------------------
  $$(x\  \cdot \ k)\lbrack i\rbrack = \ \Sigma_{m = 0}^{M - 1}x\lbrack i + m\rbrack \cdot \ k\lbrack m\rbrack$$   (2.4 )
  --------------------------------------------------------------------------------------------------------------- ----------------

  --------------------------------------------------------------------------------------------------------------------------------

Dalam formula tersebut, $x$ merepresentasikan sinyal input (fitur
jaringan), $k$ adalah filter atau kernel dengan panjang $M$, dan $i$
adalah indeks posisi pada feature map yang dihasilkan.

### Hyperparameter: Grid Search

Optimasi *hyperparameter* merupakan tahapan penting dalam pengembangan
model pembelajaran mesin dan deep learning, yang bertujuan untuk
menentukan konfigurasi parameter eksternal model yang tidak dipelajari
secara otomatis selama proses pelatihan. Pemilihan *hyperparameter* yang
tepat dapat mempengaruhi kecepatan konvergensi serta performa akhir
model dalam mendeteksi ancaman jaringan (Kunang dkk., 2021a).

#### Mekanisme Grid Search

*Grid search* merupakan salah satu metode optimasi hyperparameter yang
paling umum digunakan, dengan mekanisme pencarian sistematis melalui
seluruh kombinasi nilai kandidat yang telah ditentukan dalam ruang
pencarian (search space). Pendekatan ini bersifat exhaustive, sehingga
setiap konfigurasi hyperparameter diuji secara menyeluruh (Kunang dkk.,
2021a).

#### Parameter Kunci dalam Pembelajaran Terdistribusi

Dalam lingkungan Federated Learning, optimasi hyperparameter tidak hanya
berfokus pada peningkatan akurasi model, tetapi juga pada keseimbangan
antara beban komputasi lokal dan performa global model (McMahan dkk.,
2023). Beberapa hyperparameter yang umum dioptimalkan dalam studi
Federated Learning meliputi:

a.  *Learning Rate*, merupakan kontrol besaran pembaruan bobot model dan
    berpengaruh langsung terhadap stabilitas konvergensi.

b.  *Batch Size*, merupakan pentukan jumlah sampel yang diproses sebelum
    pembaruan gradien dan memengaruhi efisiensi pelatihan di sisi klien.

c.  *Epoch* Lokal, merupakan pengatur jumlah iterasi pelatihan lokal
    sebelum proses agregasi model global, serta mempengaruhi tingkat
    kontribusi pembelajaran lokal (Li dkk., 2020).

#### Strategi Pemilihan Hyperparameter Berbasis Multi-Kriteria

Beberapa penelitian mengusulkan pemilihan konfigurasi hyperparameter
berdasarkan pendekatan multi-kriteria, dengan mempertimbangkan lebih
dari satu metrik evaluasi, seperti Akurasi, *F1-Score*, dan *AUC-ROC*.
Pendekatan ini bertujuan untuk memperoleh konfigurasi yang tidak hanya
unggul pada satu metrik tertentu, tetapi juga stabil secara keseluruhan
dan efisien dari sisi komputasi.

Dalam literatur, pendekatan ini sering dikaitkan dengan konsep
*trade-off* performa dan efisiensi, serta dapat dianalisis menggunakan
prinsip Pareto Optimal untuk menghindari konfigurasi yang dominan pada
satu aspek namun lemah pada aspek lainnya (Deb dkk., 2002).

### Teknik Evaluasi

Evaluasi kinerja sistem deteksi intrusi berbasis Federated Learning
umumnya dilakukan melalui dua aspek utama, yaitu kualitas prediksi model
dan efisiensi operasional pada lingkungan terdistribusi. Pada konteks
keamanan jaringan *smart city*, kedua aspek ini sama-sama penting karena
sistem tidak hanya dituntut akurat, tetapi juga stabil dan efisien
ketika diimplementasikan pada banyak *gateway* dengan karakteristik data
yang heterogen.

#### Confuse Matrix

Confusion Matrix merupakan alat evaluasi fundamental yang digunakan
untuk merepresentasikan performa algoritma klasifikasi dengan
membandingkan label aktual dan hasil prediksi model. Matriks ini
memberikan informasi rinci mengenai kemampuan model dalam
mengidentifikasi kelas positif (serangan) dan kelas negatif (lalu lintas
normal), serta jenis kesalahan yang dihasilkan selama proses prediksi
(Tiwari, 2022).

Struktur Confusion Matrix pada klasifikasi biner terdiri dari empat
komponen utama:

a.  *True Positive* (TP): Serangan yang diprediksi benar sebagai
    serangan

b.  *True Negative* (TN): Aktivitas normal yang diprediksi benar sebagai
    normal

c.  *False Positive* (FP): Aktivitas normal yang salah diprediksi
    sebagai serangan (false alarm)

d.  *False Negative* (FN): Serangan yang salah diprediksi sebagai
    aktivitas normal, yang berpotensi menyebabkan kebocoran keamanan

Pada skenario klasifikasi *multi-class*, Confusion Matrix diperluas
menjadi matriks berdimensi $C\  \times C$, dengan $C$merepresentasikan
jumlah kelas serangan, sehingga distribusi kesalahan prediksi antar
kelas dapat dianalisis secara lebih spesifik.

![Fig. 4](media/image4.jpeg){width="2.247916666666667in"
height="1.68125in"}
$$

[]{#_Toc217653244 .anchor}Gambar 2.2 Ilustrasi *Horizontal Federated
Learning*

Sumber: (Tiwari, 2022)

dengan definisi sebagai berikut:

a.  *True Positive* (TP): Model memprediksi kelas positif secara benar.

b.  *True Negative* (TN): Model memprediksi kelas negatif secara benar.

c.  *False Positive* (FP): Model memprediksi kelas negatif sebagai
    positif (false alarm).

d.  *False Negative* (FN): Model gagal mendeteksi kelas positif (missed
    detection).

Pada permasalahan klasifikasi *multi-class*, Confusion Matrix dapat
diperluas menjadi matriks berdimensi $n \times n$, di mana elemen
diagonal utama merepresentasikan prediksi yang benar, sedangkan elemen
di luar diagonal menunjukkan pola misklasifikasi antar kelas.

#### Metrik Kinerja Klasifikasi

Berdasarkan nilai-nilai pada Confusion Matrix, performa model
klasifikasi umumnya diukur menggunakan beberapa metrik standar sebagai
berikut:

a.  Akurasi (Accuracy)

  -----------------------------------------------------------------------
  $$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$       (2.5)
  ------------------------------------------------------ ----------------

  -----------------------------------------------------------------------

> Mengukur proporsi prediksi yang benar terhadap seluruh sampel data.

b.  Presisi (Precision)

  -----------------------------------------------------------------------
  $$Precision = \frac{TP}{TP + FP}$$                     (2.6)
  ------------------------------------------------------ ----------------

  -----------------------------------------------------------------------

> Menunjukkan tingkat keandalan model ketika memprediksi suatu aktivitas
> sebagai serangan.

c.  *Recall*

  -----------------------------------------------------------------------
  $$Recall = \frac{TP}{TP + FN}$$                        (2.7)
  ------------------------------------------------------ ----------------

  -----------------------------------------------------------------------

> Mengukur kemampuan model dalam mendeteksi seluruh serangan yang
> terjadi. Dalam konteks keamanan jaringan, metrik ini sangat krusial
> karena berkaitan langsung dengan minimisasi *false negative*.

d.  *F1-Score*

  -------------------------------------------------------------------------------------------------
  $$F1 - Score = 2 \times \frac{Precision\  \times Recall}{Precision + Recall}$$   (2.8)
  -------------------------------------------------------------------------------- ----------------

  -------------------------------------------------------------------------------------------------

> Merupakan rata-rata harmonik antara Presisi dan Recall, yang
> memberikan evaluasi performa lebih seimbang, terutama pada dataset
> dengan ketimpangan kelas.

e.  *ROC-AUC* (Receiver Operating Characteristic -- Area Under Curve)

> Digunakan untuk mengukur kemampuan model dalam membedakan antar kelas
> pada berbagai ambang batas keputusan. Nilai *AUC* yang mendekati 1
> menunjukkan kemampuan separabilitas yang sangat baik.

#### Metrik Kinerja Klasifikasi

Selain kualitas prediksi, evaluasi sistem Federated Learning juga
mencakup aspek efisiensi dan stabilitas pelatihan dalam lingkungan
terdistribusi. Beberapa indikator yang umum digunakan meliputi:

a.  Waktu Pelatihan (Training Latency)

> Menggambarkan durasi yang dibutuhkan untuk menyelesaikan satu ronde
> pelatihan federated, yang mencakup pelatihan lokal di sisi klien serta
> proses agregasi model di server pusat.

b.  Dampak Heterogenitas Data (Parameter Dirichlet $\alpha$)

> Distribusi data Non-IID antar klien sering dimodelkan menggunakan
> distribusi Dirichlet dengan parameter konsentrasi 𝛼. Nilai $\alpha$
> yang kecil merepresentasikan heterogenitas data yang tinggi, sedangkan
> nilai yang lebih besar mendekati kondisi IID. Evaluasi terhadap
> parameter ini penting untuk mengukur ketangguhan algoritma *Federated
> Learning* terhadap ketidakseimbangan distribusi data.

c.  Stabilitas Parameter Proksimal $(\mu)$

> Pada algoritma FedProx, parameter proksimal 𝜇 berperan dalam
> mengendalikan deviasi pembaruan model lokal terhadap model global.
> Evaluasi terhadap parameter ini digunakan untuk memahami keseimbangan
> antara akurasi model dan stabilitas konvergensi pada kondisi data
> heterogen.

### Penelitian Terkait

*Federated Learning* (FL) telah banyak diteliti sebagai pendekatan
pembelajaran terdistribusi yang berfokus pada perlindungan privasi data,
khususnya pada lingkungan dengan keterbatasan regulasi dan sensitivitas
data tinggi. Dalam konteks keamanan jaringan dan sistem terdistribusi,
FL menjadi relevan karena memungkinkan proses pelatihan model tanpa
memusatkan data mentah dari berbagai *node*. Namun, tantangan utama
dalam penerapan FL adalah heterogenitas data antar klien (Non-IID),
keterbatasan komunikasi, serta variasi kemampuan komputasi perangkat.
Oleh karena itu, berbagai penelitian terdahulu berupaya mengembangkan
dan mengevaluasi algoritma FL yang lebih stabil dan robust terhadap
kondisi tersebut.

> []{#_Toc217653222 .anchor}Tabel 2.9 Penelitian Terkait

+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| Penulis            | Pengaplikasian | Metode FL &     | Dataset          | Temuan           | Kinerja Utama   | Tantangan & Solusi  |
|                    | dalam Bidang   | Model ML        |                  |                  |                 |                     |
|                    | Keamanan       |                 |                  |                  |                 |                     |
+====================+================+=================+==================+==================+=================+=====================+
| (McMahan dkk.,     | Fokus pada     | Federated       | MNIST (digit     | FedAvg robust    | MNIST CNN:      | Tantangan: data     |
| 2023)              | privasi &      | Learning dengan | recognition),    | terhadap data    | akurasi 99%     | non-IID,            |
|                    | keamanan data  | algoritma       | CIFAR-10 (image  | non-IID dan      | dengan          | unbalanced,         |
|                    | pengguna:      | Federated       | classification), | unbalanced.      | komunikasi jauh | komunikasi          |
|                    | federated      | Averaging       | Shakespeare      |                  | lebih sedikit.  | terbatas, device    |
|                    | learning       | (FedAvg); model | (language        | Komunikasi       |                 | availability.       |
|                    | mengurangi     | ML: MLP (2NN),  | modeling),       | berkurang hingga | Shakespeare     |                     |
|                    | risiko         | CNN, LSTM       | dataset besar    | 10--100×         | LSTM: speedup   | Solusi: FedAvg      |
|                    | kebocoran      | (bahasa),       | dari 10 juta     | dibandingkan     | hingga 95× pada | menambah komputasi  |
|                    | karena data    | word-level      | posting media    | FedSGD.          | data non-IID.   | lokal (epoch lebih  |
|                    | tetap di       | LSTM.           | sosial.          |                  |                 | banyak, batch       |
|                    | perangkat,     |                 |                  | Model tetap      | CIFAR-10:       | kecil), secure      |
|                    | hanya update   |                 |                  | mencapai akurasi | akurasi 85%     | aggregation,        |
|                    | model yang     |                 |                  | tinggi meski     | dengan hanya    | differential        |
|                    | dikirim.       |                 |                  | data tersebar.   | 2.000           | privacy, multiparty |
|                    |                |                 |                  |                  | komunikasi      | computation.        |
|                    |                |                 |                  |                  | round (vs       |                     |
|                    |                |                 |                  |                  | 197.500 pada    |                     |
|                    |                |                 |                  |                  | SGD).           |                     |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| (Li dkk., 2020)    | Tidak secara   | Federated       | Synthetic        | FedProx lebih    | Peningkatan     | Tantangan:          |
|                    | langsung       | Learning dengan | datasets (dengan | stabil dibanding | absolute test   | Heterogenitas       |
|                    | membahas       | algoritma       | variasi          | FedAvg pada      | accuracy        | sistem (perbedaan   |
|                    | keamanan,      | FedProx         | heterogenitas α, | kondisi          | rata-rata 22%   | hardware, koneksi,  |
|                    | namun relevan  | (generalization | β), MNIST,       | heterogen.       | pada kondisi    | daya) dan           |
|                    | karena         | dari FedAvg).   | FEMNIST,         | Memberikan       | sangat          | heterogenitas       |
|                    | federated      | Model ML:       | Sentiment140     | konvergensi      | heterogen       | statistik (data     |
|                    | learning       | Logistic        | (tweet           | lebih robust dan | dibanding       | non-IID).           |
|                    | menjaga        | Regression,     | sentiment),      | akurasi lebih    | FedAvg.         |                     |
|                    | privasi data   | LSTM, dan model | Shakespeare      | tinggi.          |                 | Solusi: FedProx     |
|                    | (data tetap di | klasifikasi     | (next-character  |                  |                 | menambahkan         |
|                    | perangkat,     | lainnya.        | prediction).     |                  |                 | proximal term untuk |
|                    | tidak dikirim  |                 |                  |                  |                 | membatasi drift     |
|                    | ke server).    |                 |                  |                  |                 | model lokal, serta  |
|                    |                |                 |                  |                  |                 | mengakomodasi       |
|                    |                |                 |                  |                  |                 | jumlah pekerjaan    |
|                    |                |                 |                  |                  |                 | lokal yang          |
|                    |                |                 |                  |                  |                 | bervariasi          |
|                    |                |                 |                  |                  |                 | (stragglers tidak   |
|                    |                |                 |                  |                  |                 | di-drop).           |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| (Bodagala &        | Deteksi        | Metode:         | Bot-IoT (utama), | Algoritma FL \>  | F-Score 95%-99% | Tantangan: Risiko   |
| Priyanka, 2022)    | ancaman siber  | Federated       | TON_IoT,         | ML terpusat      | (DDoS, DoS,     | keamanan, privasi,  |
|                    | di lingkungan  | Learning (FL).  | MQTTset.         | untuk keamanan & | Reconnaissance) | & latensi pada      |
|                    | IoT (spoofing, | Model: DNN,     |                  | kerahasiaan IoT. | pada Bot-IoT.   | pembelajaran        |
|                    | breach, DoS).  | CNN, RNN.       |                  |                  |                 | terpusat. Solusi:   |
|                    |                |                 |                  |                  |                 | FL melatih model    |
|                    |                |                 |                  |                  |                 | secara lokal di     |
|                    |                |                 |                  |                  |                 | klien.              |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| (Hijazi dkk.,      |                | Metode: FL +    | N-BaIoT (utama), | Kombinasi FL +   | Akurasi,        | Tantangan: FL       |
| 2024)              |                | Fully           | WUSTL-EHMS-2020  | FHE (khususnya   | recall,         | standar rentan      |
|                    |                | Homomorphic     | (studi kasus).   | berbasis         | presisi, F1 \>  | (saluran tidak      |
|                    |                | Encryption      |                  | klaster) efektif | 99.7% (OECM,    | aman). Overhead &   |
|                    |                | (FHE); 4        |                  | mengurangi       | MUCM, MECM)     | latensi tinggi pada |
|                    |                | pendekatan      |                  | overhead (hingga | pada N-BaIoT.   | FL yang aman.       |
|                    |                | berbasis        |                  | 89.98%) &        | MUCM latensi    | Solusi: Enkripsi    |
|                    |                | klaster (OUCM,  |                  | latensi (hingga  | terendah.       | parameter model     |
|                    |                | OECM, MUCM,     |                  | 70.38%) sambil   |                 | (FHE); Klasterisasi |
|                    |                | MECM). Model:   |                  | menjaga akurasi. |                 | untuk mengurangi    |
|                    |                | CNN.            |                  |                  |                 | komunikasi.         |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| (Ahmadi & Javidan, | Deteksi        | Metode:         | Dataset          | Model FL         | Akurasi 0.953,  | Tantangan: Model    |
| 2023)              | serangan DDoS  | Federated Deep  | aktivitas IoT    | mencapai         | Loss 0.0369     | terpusat butuh      |
|                    | pada           | Learning        | perkotaan nyata  | performa         | (FL) vs Akurasi | konsentrasi data    |
|                    | lingkungan IoT | (antara fog &   | (4060 node) +    | sebanding dengan | 0.9575, Loss    | (kompleksitas       |
|                    | perkotaan      | cloud). Model:  | simulasi DDoS.   | model terpusat,  | 0.038           | komputasi tinggi,   |
|                    | nyata.         | LSTM (RNN).     |                  | sambil menjaga   | (Terpusat).     | masalah privasi).   |
|                    |                |                 |                  | privasi data &   |                 | Solusi: Menerapkan  |
|                    |                |                 |                  | mendistribusikan |                 | FL untuk            |
|                    |                |                 |                  | beban komputasi. |                 | mendistribusikan    |
|                    |                |                 |                  |                  |                 | beban komputasi ke  |
|                    |                |                 |                  |                  |                 | perangkat fog &     |
|                    |                |                 |                  |                  |                 | menjaga privasi     |
|                    |                |                 |                  |                  |                 | data.               |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| (Thantharate & T,  | Deteksi        | Metode:         | Bot-IoT.         | Kerangka kerja   | Akurasi 89.6%   | Tantangan: 1)       |
| 2023)              | ancaman siber  | Horizontal      |                  | FL (Cybria)      | (FL) vs 81.4%   | Pendekatan terpusat |
|                    | kolaboratif    | Federated       |                  | mencapai akurasi | (Terpusat).     | memiliki risiko     |
|                    | (Cybria) yang  | Learning        |                  | lebih tinggi     |                 | privasi & keamanan. |
|                    | menjaga        | (TensorFlow     |                  | (\~10%) &        |                 | 2) Penerapan FL     |
|                    | privasi.       | Federated,      |                  | konvergensi      |                 | menghadapi          |
|                    |                | Flower). Model: |                  | lebih cepat      |                 | heterogenitas       |
|                    |                | Deep Neural     |                  | dibandingkan     |                 | statistik &         |
|                    |                | Network (DNN).  |                  | model DNN        |                 | serangan poisoning. |
|                    |                |                 |                  | terpusat.        |                 | Solusi: 1)          |
|                    |                |                 |                  |                  |                 | Arsitektur FL       |
|                    |                |                 |                  |                  |                 | (Cybria) untuk      |
|                    |                |                 |                  |                  |                 | pelatihan           |
|                    |                |                 |                  |                  |                 | terdesentralisasi.  |
|                    |                |                 |                  |                  |                 | 2) Perlu agregasi   |
|                    |                |                 |                  |                  |                 | aman & DP.          |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| (Olanrewaju-George | IDS untuk IoT  | Metode:         | N-BaIoT (9       | Model            | FL-AE           | Tantangan: 1)       |
| & Pranggono, 2025) | (keamanan &    | Federated       | perangkat IoT,   | unsupervised AE  | menunjukkan FPR | Masalah keamanan &  |
|                    | privasi data). | Learning        | botnet Mirai &   | yang dilatih via | terendah        | privasi IoT. 2)     |
|                    |                | (FedAvgM).      | BASHLITE).       | FL adalah yang   | dibandingkan    | Keterbatasan sumber |
|                    |                | Model:          |                  | terbaik secara   | FL-DNN dan      | daya perangkat IoT. |
|                    |                | Unsupervised    |                  | keseluruhan,     | model non-FL.   | 3) Sulit memproses  |
|                    |                | AutoEncoder     |                  | terutama unggul  |                 | data tidak berlabel |
|                    |                | (AE) &          |                  | dalam metrik     |                 | di edge. Solusi: 1) |
|                    |                | Supervised Deep |                  | False Positive   |                 | FL untuk pelatihan  |
|                    |                | Neural Network  |                  | Rate (FPR) /     |                 | terdesentralisasi & |
|                    |                | (DNN).          |                  | mengurangi alarm |                 | privasi. 2) Model   |
|                    |                |                 |                  | palsu.           |                 | AE unsupervised     |
|                    |                |                 |                  |                  |                 | untuk belajar dari  |
|                    |                |                 |                  |                  |                 | data tidak berlabel |
|                    |                |                 |                  |                  |                 | di edge.            |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| (Thakur dkk.,      | Deteksi        | Metode:         | Tidak disebutkan | Pendekatan FL    | Akurasi 95%     | Tantangan: 1)       |
| 2024)              | serangan       | Federated       | (Implementasi    | secara           | (FL) vs 91%     | Privasi &           |
|                    | jaringan (IDS) | Learning        | umum pada data   | signifikan       | (Non-FL). Data  | skalabilitas pada   |
|                    | di lingkungan  | (FedAvg).       | IoT).            | mengungguli      | loss \~2% (FL). | pendekatan          |
|                    | IoT.           | Model: CNN      |                  | model non-FL     | Waktu respons   | terpusat. 2)        |
|                    |                | (ekstraksi      |                  | (terpusat) dalam | rata-rata 6.81  | Mengelola data      |
|                    |                | fitur), KNN     |                  | akurasi & data   | detik.          | heterogen           |
|                    |                | (deteksi        |                  | loss.            |                 | (Non-IID).          |
|                    |                | anomali).       |                  |                  |                 | Solusi: 1) FL untuk |
|                    |                |                 |                  |                  |                 | melatih di edge &   |
|                    |                |                 |                  |                  |                 | mengurangi risiko   |
|                    |                |                 |                  |                  |                 | kebocoran data. 2)  |
|                    |                |                 |                  |                  |                 | Agregasi model      |
|                    |                |                 |                  |                  |                 | (FedAvg) untuk      |
|                    |                |                 |                  |                  |                 | membangun model     |
|                    |                |                 |                  |                  |                 | global.             |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| (Abdel-Basset      | Perlindungan   | Metode: PP-FDL  | MNIST, CIFAR-10. | PP-FDL efektif   | Peningkatan     | Tantangan: 1)       |
| dkk., 2024)        | privasi data   | (FL +           |                  | melindungi data  | akurasi 3%-8%   | Privasi (rentan     |
|                    | terhadap       | arsitektur      |                  | dari serangan    | vs SOTA.        | serangan GAN). 2)   |
|                    | serangan GAN   | GAN).           |                  | GAN pada data    | Akurasi 93.07%  | Heterogenitas Data  |
|                    | pada data      | Menggunakan     |                  | Non-IID tanpa    | (MNIST), 84.21% | (Non-IID). 3)       |
|                    | Non-IID di     | \'private       |                  | penurunan        | (CIFAR-10).     | Efisiensi (solusi   |
|                    | IoT.           | identifier\'    |                  | kinerja          |                 | privasi sering      |
|                    |                | unik per kelas. |                  | signifikan       |                 | mengorbankan        |
|                    |                | Agregasi via    |                  | (seperti DP)     |                 | akurasi/komputasi). |
|                    |                | FedProx. Model: |                  | atau overhead    |                 | Solusi: 1)          |
|                    |                | CNN.            |                  | tinggi (seperti  |                 | Menggunakan         |
|                    |                |                 |                  | enkripsi).       |                 | \'private           |
|                    |                |                 |                  |                  |                 | identifier\' per    |
|                    |                |                 |                  |                  |                 | kelas agar          |
|                    |                |                 |                  |                  |                 | penyerang tidak     |
|                    |                |                 |                  |                  |                 | bisa menargetkan    |
|                    |                |                 |                  |                  |                 | kelas data. 2)      |
|                    |                |                 |                  |                  |                 | Dirancang untuk     |
|                    |                |                 |                  |                  |                 | data Non-IID. 3)    |
|                    |                |                 |                  |                  |                 | Menghindari         |
|                    |                |                 |                  |                  |                 | noise/enkripsi      |
|                    |                |                 |                  |                  |                 | berat.              |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+
| Penelitian ini     | ToN-IoT        | HFL+FedAVG      | Basic MLP        | Temuan dibahas   | Temuan dibahas  | Tantangan\          |
|                    |                |                 |                  | di Bab IV        | di Bab IV       | dibahas di Bab IV   |
|                    |                | HFL+FedProx     | Basic CNN        |                  |                 |                     |
+--------------------+----------------+-----------------+------------------+------------------+-----------------+---------------------+

## BAB III METODOLOGI PENELITIAN

Penelitian ini mengadopsi kerangka *CRISP-DM* (Cross-Industry Standard
Process for Data Mining) sebagai fondasi metodologi, dengan penyesuaian
pada konteks *Federated Learning* untuk *Network Intrusion Detection
System* (NIDS) di lingkungan *smart city*. Pemilihan *CRISP-DM*
didasarkan pada kemampuannya dalam menyediakan alur kerja yang
sistematis dan iteratif, sekaligus fleksibel untuk diterapkan pada
skenario pembelajaran mesin terdistribusi.

### Alur Pengerjaan

Berbeda dengan pendekatan data mining terpusat, penelitian ini dirancang
untuk mempertahankan desentralisasi data guna menjamin privasi lalu
lintas jaringan pada level *gateway*. Oleh karena itu, setiap tahapan
*CRISP-DM* diadaptasi agar selaras dengan skema *Horizontal Federated
Learning*, di mana data tetap berada pada klien lokal dan hanya
parameter model yang dipertukarkan dengan server pusat.

Secara umum, alur penelitian diawali dengan pemetaan kebutuhan keamanan
dan privasi *smart city* (*Business Understanding*), dilanjutkan dengan
verifikasi karakteristik statistik dan kualitas dataset ToN-IoT (*Data
Understanding*). Data kemudian ditransformasikan agar sesuai dengan
kebutuhan pelatihan model terdistribusi (*Data Preparation*), sebelum
masuk ke tahap perancangan arsitektur model dan mekanisme agregasi
Federated Learning (*Modeling*). Tahap akhir mencakup evaluasi performa
model global pada berbagai skenario distribusi data, baik IID maupun
Non-IID (*Evaluation*).

Untuk memastikan reprodusibilitas dan konsistensi hasil eksperimen,
seluruh proses penelitian diimplementasikan dalam lingkungan komputasi
yang terkontrol, mencakup spesifikasi perangkat keras, perangkat lunak,
serta pustaka pendukung yang digunakan selama simulasi Federated
Learning.

Alur metodologi penelitian secara keseluruhan dirangkum pada Gambar 3.1
dalam bentuk diagram alur kerja.

![[]{#_Ref217646411 .anchor}Gambar 3.1 Alur kerja
penelitian](media/image5.png){width="5.350445100612424in"
height="4.527163167104112in"}

Gambar 3.1 Alur kerja penelitian menunjukkan alur kerja penelitian
berbasis CRISP-DM yang diadaptasi untuk Horizontal Federated Learning,
dimulai dari perumusan masalah dan tujuan penelitian, dilanjutkan dengan
tahapan pemahaman bisnis, pemahaman data, persiapan data, pemodelan, dan
evaluasi. Tahap evaluasi memungkinkan terjadinya iterasi kembali ke
pemahaman bisnis apabila hasil yang diperoleh belum memenuhi tujuan
penelitian, sebelum diakhiri dengan analisis hasil dan kesimpulan.

### Lingkungan Penelitian

Lingkungan penelitian pada studi ini dirancang untuk mendukung
pelaksanaan seluruh tahapan alur kerja yang telah dijelaskan pada
Sub-bab 3.1, khususnya dalam simulasi Horizontal Federated Learning dan
pelatihan model pembelajaran mesin. Seluruh eksperimen dijalankan pada
satu mesin komputasi lokal dengan konfigurasi perangkat keras dan
perangkat lunak yang terdefinisi secara eksplisit guna memastikan
konsistensi serta kemudahan replikasi hasil penelitian. Pengelolaan
dependensi dilakukan menggunakan *Python virtual environment* tanpa
menggunakan Conda, sementara akselerasi komputasi model *deep learning*
memanfaatkan GPU melalui dukungan CUDA pada TensorFlow.

> []{#_Toc217653223 .anchor}Tabel 3.1 Hardware

  -----------------------------------------------------------------------
  **Komponen**     **Spesifikasi**
  ---------------- ------------------------------------------------------
  Motherboard      Gigabyte B450 Aorus M

  Prosesor         AMD Ryzen 5 3500 (hingga 4.1 GHz)

  Memory           2×8 GB Single Rank + 2×16 GB Dual Rank DDR4 3200 MHz
                   CL18 (48 GB total)

  *Storage*        Adata SU650 240 GB SATA III

  GPU              Zotac GTX 1650 Super

  Operating System Arch Linux (rolling release)

  Kernel           Linux 6.17.9-zen (freezed)

  Driver NVIDIA    580.105.08

  CUDA Version     13.0
  -----------------------------------------------------------------------

> []{#_Toc217653224 .anchor}Tabel 3.2 Perangkat Lunak dan Pustaka
> Pendukung

  ------------------------------------------------------------------------------------
  **Kategori**     **Library**              **Versi**   **Fungsi**
  ---------------- ------------------------ ----------- ------------------------------
  Data Processing  pandas                   2.3.3       Manipulasi dan analisis data

                   numpy                    2.3.5       Operasi numerik

                   scipy                    1.16.3      Komputasi ilmiah

                   scikit-learn             1.7.2       Pra-pemrosesan dan evaluasi
                                                        model

  Deep learning    tensorflow               2.20.0      Framework deep learning
                                                        berbasis CUDA

                   keras                    3.12.0      Abstraksi arsitektur model

  Federated        flwr                     1.24.0      Orkestrasi dan agregasi FL
  Learning                                              

                   grpcio                   1.76.0      Komunikasi client--server

                   grpcio-health-checking   1.76.0      Monitoring koneksi FL

  Imbalance        imbalanced-learn         0.14.0      Teknik penanganan
  Handler                                               ketidakseimbangan kelas

  GPU Accelerated  cupy                     13.6.0      Operasi numerik berbasis CUDA
  for                                                   
  Pre-processing                                        
  (opsional)                                            

  Visualization    matplotlib               3.10.7      Visualisasi data
  and EDA                                               

                   seaborn                  0.13.2      Visualisasi statistik

  UI/UX Enviroment jupyter                  1.0.0       Notebook interface

                   jupyterlab               4.5.0       Pengembangan interaktif

                   notebook                 7.5.0       Eksekusi notebook

                   ipykernel                7.1.0       Kernel Python

                   ipython                  9.7.0       Interactive shell

                   ipywidgets               8.1.8       Komponen interaktif

  Utils            pickle                   built-in    Serialisasi objek

                   pathlib                  built-in    Operasi berkas

                   rich                     13.9.4      Logging dan output terminal

                   tabulate                 0.9.0       Penyajian tabel

  Distributed      ray                      2.51.1      Eksekusi terdistribusi
  computing                                             
  ------------------------------------------------------------------------------------

### Businisse Understanding

Dalam konteks penelitian ini, lingkungan *smart city* dipandang sebagai
sistem jaringan terdistribusi yang terdiri dari berbagai *gateway* IoT
dengan karakteristik lalu lintas yang heterogen. Masing-masing *gateway*
tersebut berperan sebagai titik akses utama bagi layanan publik penting,
seperti transportasi cerdas, manajemen energi, dan sistem kesehatan.
Gangguan pada lapisan jaringan, khususnya akibat serangan siber,
berpotensi berdampak langsung terhadap kontinuitas layanan dan keandalan
operasional kota.

Permasalahan keamanan jaringan pada *smart city* tidak hanya berkaitan
dengan kemampuan mendeteksi serangan, tetapi juga dengan cara
pengelolaan data lalu lintas jaringan. Pendekatan keamanan konvensional
yang mengandalkan pemusatan data pada server terpusat menghadapi kendala
serius terkait risiko kebocoran data dan kepatuhan terhadap regulasi
privasi. Lalu lintas jaringan yang dianalisis sering kali memuat
informasi sensitif yang merepresentasikan aktivitas pengguna dan
infrastruktur kota.

Kondisi tersebut mendorong kebutuhan akan mekanisme deteksi intrusi yang
mampu beroperasi secara terdistribusi pada tingkat *gateway*, tanpa
memindahkan data mentah ke pusat, namun tetap mempertahankan kemampuan
deteksi yang andal pada skala kota. Kerangka inilah yang menjadi dasar
dalam perumusan tujuan bisnis dan kriteria keberhasilan sistem pada
tahap *business understanding*.

#### Tujuan Bisnis (Business Objectives)

Berdasarkan konteks permasalahan tersebut, tujuan bisnis dari penelitian
ini adalah merancang mekanisme pertahanan siber yang mampu
menyeimbangkan kebutuhan keamanan operasional dan perlindungan privasi
data dalam lingkungan *smart city*. Sistem yang diusulkan diharapkan
dapat memenuhi tujuan-tujuan berikut:

a.  Menjamin Kontinuitas Layanan Publik

> Sistem harus mampu mendeteksi serangan jaringan, seperti Distributed
> Denial of Service, Injection, dan sebagainya secara dini pada tingkat
> *gateway* untuk mencegah gangguan terhadap layanan publik yang
> bersifat kritis.

b.  Menjaga Privasi Data Lalu Lintas Jaringan

> Sistem harus memastikan bahwa data mentah lalu lintas jaringan tetap
> berada di lingkungan lokal masing-masing *gateway*, sehingga risiko
> kebocoran data dan pelanggaran privasi dapat diminimalkan.

c.  Mendukung Operasi Terdistribusi Skala Kota

> Mekanisme yang dirancang harus memungkinkan pembaruan dan peningkatan
> kemampuan deteksi dilakukan secara terkoordinasi tanpa memerlukan
> sentralisasi data.

#### Kriteria Keberhasilan (Success Criteria)

Keberhasilan sistem yang diusulkan dievaluasi berdasarkan indikator
teknis yang memiliki implikasi langsung terhadap operasional *smart
city*, sebagai berikut:

a.  Efektivitas Deteksi pada Data Heterogen (Non-IID)

> Model deteksi intrusi harus mampu mempertahankan performa yang
> konsisten meskipun setiap *gateway* memiliki distribusi lalu lintas
> jaringan yang berbeda. Ketidakmampuan menangani heterogenitas data
> berpotensi meningkatkan tingkat false alarm dan menurunkan keandalan
> sistem.

b.  Stabilitas Pelatihan dalam Lingkungan Terdistribusi

> Proses pelatihan menggunakan Federated Learning harus menghasilkan
> konvergensi model global yang stabil meskipun pelatihan dilakukan
> secara terfragmentasi pada banyak klien.

c.  Efisiensi Komputasi pada Perangkat *Gateway*

> Model yang dikembangkan harus memiliki kompleksitas komputasi yang
> sesuai dengan keterbatasan sumber daya *gateway* IoT, sehingga tidak
> menimbulkan beban berlebih terhadap kinerja jaringan maupun perangkat.

Indikator-indikator tersebut digunakan sebagai dasar dalam perancangan
eksperimen dan evaluasi performa sistem pada tahap selanjutnya.

### Data Understanding

Tahap *data understanding* dalam kerangka *CRISP-DM* bertujuan untuk
memastikan bahwa dataset yang digunakan memiliki kualitas, karakteristik
statistik, dan struktur distribusi yang sesuai dengan tujuan penelitian
sebelum dilakukan pemrosesan lebih lanjut. Dataset ToN-IoT yang
digunakan dalam penelitian ini telah dijelaskan secara komprehensif pada
Bab II Sub Bab 2.3, mencakup arsitektur *testbed*, jenis serangan, serta
deskripsi fitur. Oleh karena itu, tahap ini tidak mengulang pemaparan
struktur data, melainkan berfokus pada evaluasi karakteristik data dari
perspektif eksperimental.

Secara khusus, tahap *data understanding* diarahkan untuk memverifikasi
kesesuaian dataset ToN-IoT dalam mensimulasikan skenario *Federated
Learning* (FL) pada lingkungan *smart city*, di mana data bersifat
terdistribusi, heterogen, dan tidak seimbang. Analisis eksploratori
dilakukan untuk mengidentifikasi potensi permasalahan data yang dapat
memengaruhi stabilitas pelatihan model dan validitas hasil eksperimen.
Investigasi data difokuskan pada tiga aspek utama berikut.

#### Analisis Distribusi Kelas

Analisis distribusi kelas dilakukan untuk memetakan proporsi
masing-masing kategori serangan dan lalu lintas normal dalam dataset.
Dataset ToN-IoT secara inheren memiliki karakteristik *class imbalance*,
di mana beberapa jenis serangan muncul dalam jumlah yang sangat terbatas
dibandingkan kelas lainnya. Kondisi ini merepresentasikan situasi nyata
pada jaringan *smart city*, di mana sebagian besar waktu jaringan berada
dalam kondisi normal dan hanya sebagian kecil serangan tertentu yang
terjadi secara sporadis.

Pemahaman terhadap distribusi kelas ini menjadi faktor kunci dalam
perancangan eksperimen *Federated Learning*. Informasi mengenai
ketimpangan kelas digunakan sebagai dasar untuk merancang skema
pembagian data ke setiap klien agar mencerminkan kondisi Non-IID, di
mana setiap *gateway* memiliki pola lalu lintas dan profil ancaman yang
berbeda. Tanpa analisis ini, simulasi *Federated Learning* berisiko
menghasilkan model yang bias terhadap kelas mayoritas atau tidak stabil
pada kelas minoritas.

#### Analisis Integritas dan Kualitas Data

Analisis integritas data dilakukan untuk memastikan bahwa dataset bebas
dari permasalahan mendasar yang dapat menurunkan kualitas proses
pelatihan model. Pemeriksaan difokuskan pada dua aspek utama, yaitu
keberadaan *missing values* dan duplikasi data.

Pemeriksaan missing values dilakukan untuk mengidentifikasi atribut yang
tidak memiliki nilai, khususnya pada fitur yang bergantung pada protokol
tertentu pada Sub Bab 2.3 Ketidakhadiran nilai pada fitur-fitur tersebut
dianalisis secara kontekstual untuk membedakan antara kondisi yang
muncul secara alami akibat ketiadaan protokol pada suatu koneksi dan
indikasi kesalahan pencatatan data. Pendekatan ini penting agar
penanganan data hilang tidak menghilangkan informasi yang secara
semantik masih valid.

Selain itu, analisis duplikasi dilakukan untuk mendeteksi adanya
pengulangan baris data yang identik. Keberadaan data duplikat berpotensi
menyebabkan bias pada model karena pola yang sama dipelajari secara
berulang. Oleh karena itu, identifikasi redundansi data menjadi langkah
awal untuk menjaga objektivitas dan generalisasi model yang dilatih.

#### Analisis Korelasi Fitur

Analisis korelasi fitur dilakukan untuk mengevaluasi hubungan antar
atribut numerik dalam dataset. Matriks korelasi membantu kita melihat
apakah ada data yang kembar atau saling tumpang tindih. Keberadaan fitur
yang sangat berkorelasi dapat meningkatkan kompleksitas model tanpa
memberikan informasi tambahan yang signifikan.

Hasil analisis korelasi ini digunakan sebagai landasan dalam tahap
seleksi dan transformasi fitur pada fase Data Preparation. Dengan
mengurangi redundansi fitur, model Federated Learning yang dibangun
diharapkan lebih efisien dari sisi komputasi serta mengurangi beban
komunikasi antar klien dan server agregasi.

Melalui tahap *data understanding* ini, dataset ToN-IoT divalidasi
kelayakannya sebagai representasi lalu lintas jaringan *smart city* yang
kompleks dan terdistribusi. Analisis distribusi kelas, integritas data,
dan korelasi fitur memberikan dasar empiris bagi perancangan strategi
pemrosesan data dan pembagian data antar klien pada tahap *data
preparation*, sehingga eksperimen *Federated Learning* yang dilakukan
memiliki fondasi data yang kuat dan realistis.

### Data Preparation

Tahap *data preparation* bertujuan untuk mentransformasikan data mentah
menjadi representasi numerik yang konsisten, efisien, dan sesuai untuk
pelatihan model *Federated Learning* berbasis jaringan saraf tiruan.
Mengingat model *deep learning* sangat sensitif terhadap skala, format,
dan distribusi input, proses persiapan data dirancang secara sistematis
dengan mempertimbangkan karakteristik spesifik dataset ToN-IoT serta
keterbatasan lingkungan terdistribusi pada skenario *smart city*.

Berbeda dengan pendekatan generik, tahapan persiapan data pada
penelitian ini disusun untuk menjaga integritas semantik lalu lintas
jaringan, mempertahankan karakteristik Non-IID, serta meminimalkan
risiko bias akibat kebocoran data. Proses ini terdiri atas enam tahapan
utama sebagai berikut.

#### Pembersihan Data

Pembersihan data dilakukan dengan pendekatan protocol-aware yang
kontekstual. Missing values pada fitur spesifik protokol *DNS*, *HTTP*,
*SSL* diisi berdasarkan keberadaan trafik protokol terkait, misalnya
dengan mode, 0, atau *none*. Kolom numerik lainnya diisi dengan median,
dan kolom kategorikal dengan mode atau *unknown*. Pendekatan ini tetap
mempertahankan makna semantik sebanyak mungkin sambil memastikan tidak
ada nilai NaN yang mengganggu proses pelatihan model (Alsaedi dkk.,
2020).

Ketiadaan nilai pada fitur-fitur tersebut tidak merepresentasikan
kesalahan pencatatan data, melainkan menunjukkan bahwa suatu koneksi
tidak menggunakan protokol terkait. Oleh karena itu, nilai kosong
dipertahankan dan diperlakukan sebagai informasi implisit mengenai
absennya protokol tertentu. Pendekatan ini memungkinkan model
mempelajari perbedaan karakteristik lalu lintas berdasarkan jenis
protokol yang aktif tanpa kehilangan makna semantik data (Alsaedi dkk.,
2020).

#### Transformasi Variabel Kategorikal (Encoding)

Untuk mendukung komputasi berbasis matriks pada model *deep learning*,
seluruh atribut non-numerik ditransformasikan ke dalam representasi
numerik yang sesuai (Alsaedi dkk., 2020).

Variabel target untuk klasifikasi *multi-class*, yang mencakup sepuluh
kategori lalu lintas (sembilan jenis serangan dan satu kelas normal),
dikonversi menggunakan *label encoding*. Pendekatan ini dipilih karena
label hanya berfungsi sebagai penanda kelas dan tidak mengandung
hubungan ordinal (Alsaedi dkk., 2020).

Sementara itu, fitur kategorikal nominal seperti jenis layanan, status
koneksi, dan atribut protokol ditransformasikan menggunakan teknik
*one-hot encoding*. Metode ini digunakan untuk mencegah model
mengasumsikan adanya hubungan hierarkis yang tidak relevan antar
kategori, sehingga pola lalu lintas jaringan dapat dipelajari secara
lebih representatif (Alsaedi dkk., 2020).

#### Seleksi Fitur Berbasis Variansi

Untuk meningkatkan efisiensi komputasi dan mengurangi kompleksitas
model, dilakukan seleksi fitur menggunakan metode *variance
thresholding*. Fitur-fitur dengan variansi sangat rendah, yaitu di bawah
ambang batas 0.01, dieliminasi dari dataset (Alsaedi dkk., 2020).

Fitur dengan variansi mendekati nol cenderung memiliki nilai yang hampir
konstan pada seluruh sampel, sehingga tidak memberikan kontribusi
signifikan terhadap kemampuan model dalam membedakan antara lalu lintas
normal dan aktivitas serangan. Penghapusan fitur-fitur ini membantu
mengurangi risiko *overfitting* serta menurunkan beban komputasi dan
komunikasi dalam skema *Federated Learning (Li dkk., 2020)* .

#### Standardisasi Fitur (Feature Scaling)

Dataset ToN-IoT memiliki fitur numerik dengan rentang nilai yang sangat
bervariasi, seperti durasi koneksi dalam satuan detik dan volume lalu
lintas dalam satuan *byte* yang dapat mencapai jutaan. Untuk memastikan
setiap fitur memberikan kontribusi yang seimbang selama proses
pelatihan, dilakukan standardisasi menggunakan teknik *standard scaling
(Alsaedi dkk., 2020)*.

Teknik ini mentransformasi fitur numerik sehingga memiliki nilai
rata-rata nol dan deviasi standar satu. Proses fitting scaler dilakukan
secara eksklusif pada data latih dan kemudian diterapkan pada data uji.
Pemisahan ini dilakukan secara ketat untuk mencegah terjadinya kebocoran
data (data leakage) yang dapat menyebabkan hasil evaluasi menjadi bias
dan terlalu optimis (Alsaedi dkk., 2020).

#### Pembagian Data Terstratifikasi

Data yang telah diproses dibagi menjadi himpunan pelatihan dan pengujian
dengan rasio 80% untuk data latih dan 20% untuk data uji. Pembagian
dilakukan menggunakan metode stratified splitting untuk memastikan
proporsi setiap kelas serangan pada kedua himpunan tetap konsisten
dengan distribusi data asli (Alsaedi dkk., 2020).

Pendekatan ini sangat penting mengingat dataset ToN-IoT memiliki tingkat
ketimpangan kelas yang tinggi. Dengan menjaga konsistensi distribusi
kelas, evaluasi performa model terhadap kelas minoritas, seperti
serangan *Man-in-the-Middle* (MITM), dapat dilakukan secara lebih adil
dan representative (Alsaedi dkk., 2020).

#### Pembersihan Data

Penelitian ini secara sengaja tidak menerapkan teknik oversampling
sintetis seperti *SMOTE* (Synthetic Minority Over-sampling Technique)
yang umum digunakan pada sistem deteksi intrusi konvensional. Keputusan
metodologis ini didasarkan pada pertimbangan validitas eksperimen
*Federated Learning*.

Pertama, penerapan *SMOTE* akan mengubah distribusi alami data, sehingga
mengaburkan karakteristik Non-IID yang menjadi fokus utama penelitian
ini. Kedua, pada lingkungan terdistribusi, pembuatan data sintetis
secara independen di setiap klien berpotensi menghasilkan pola pelatihan
yang tidak konsisten dan menghambat proses konvergensi model global.
Ketiga, penanganan ketimpangan kelas diserahkan pada mekanisme
algoritmik *Federated Learning*, khususnya melalui penggunaan algoritma
FedProx yang memiliki *proximal regularization* term untuk menjaga
stabilitas pelatihan meskipun terdapat dominasi kelas tertentu pada
masing-masing klien (Li dkk., 2020).

### Modeling

Tahap Modeling merupakan inti dari penelitian ini, di mana arsitektur
jaringan saraf tiruan dan algoritma agregasi Federated Learning
dikonfigurasi untuk membangun sistem deteksi intrusi pada lingkungan
*smart city* yang terdistribusi. Pada tahap ini, fokus diarahkan pada
pemilihan arsitektur model, skema pelatihan federated, strategi
penanganan heterogenitas data, serta konfigurasi hyperparameter yang
sesuai dengan keterbatasan sumber daya *gateway* IoT.

Implementasi pemodelan dilakukan menggunakan kerangka kerja simulasi
Federated Learning berbasis Python dengan Flower framework, yang banyak
digunakan dalam penelitian akademik untuk mengevaluasi algoritma FL pada
skenario terkontrol.

#### Strategi Horizontal Federated Learning

Penelitian ini menerapkan skema *Horizontal Federated Learning* (HFL),
di mana setiap klien memiliki ruang fitur yang identik namun distribusi
sampel yang berbeda. Skema ini dipilih karena secara realistis
merepresentasikan kondisi *smart city*, di mana setiap *gateway*
jaringan mengamati jenis protokol yang sama tetapi dengan pola lalu
lintas lokal yang berbeda.

Dalam HFL, pelatihan model dilakukan secara lokal pada masing-masing
klien, sementara hanya parameter model yang dikirimkan ke server pusat
untuk proses agregasi. Pendekatan ini terbukti efektif dalam menjaga
privasi data mentah sekaligus memungkinkan pembelajaran kolaboratif
lintas *node* terdistribusi, sebagaimana ditunjukkan dalam berbagai
studi Federated Learning pada sistem IoT dan keamanan jaringan (Li dkk.,
2020; McMahan dkk., 2023).

#### Arsitektur Deep Learning

Berdasarkan pertimbangan kompleksitas komputasi dan kemampuan
generalisasi, penelitian ini mengevaluasi dua arsitektur jaringan saraf
tiruan yang umum digunakan dalam deteksi intrusi berbasis lalu lintas
jaringan, yaitu Multi-Layer Perceptron (MLP) dan Convolutional Neural
Network satu dimensi (CNN-1D). Kedua arsitektur diadaptasi untuk dua
skenario klasifikasi, yaitu klasifikasi *binary* dan klasifikasi
*multi-class*.

**Multi-Layer Perceptron (MLP)**

MLP digunakan sebagai model dasar (baseline) untuk mempelajari hubungan
non-linear antar fitur statistik jaringan. Arsitektur ini banyak
digunakan dalam penelitian NIDS karena kesederhanaannya serta efisiensi
komputasi pada lingkungan dengan keterbatasan sumber daya. Untuk
stateginya sebagai berikut:

a.  Konfigurasi *Binary*:

> Arsitektur terdiri dari lima lapisan tersembunyi (Input → 256 → 128 →
> 64 → 32 → Output). Lapisan keluaran menggunakan fungsi aktivasi
> sigmoid untuk memodelkan probabilitas serangan (Kunang dkk., 2021b;
> Qazi dkk., 2022b).

b.  Konfigurasi *Multi-class*:

> Untuk menangkap kompleksitas pola serangan yang lebih beragam,
> digunakan arsitektur yang lebih dalam (Input → 512 → 256 → 128 → 64 →
> Output), dengan fungsi aktivasi *softmax* pada lapisan keluaran untuk
> memprediksi sepuluh kelas lalu lintas (Kunang dkk., 2021b).

c.  Regularisasi:

> Untuk mengurangi risiko *overfitting*, diterapkan dropout dengan rasio
> 0.2--0.4 serta regularisasi L2 dengan koefisien $\lambda\  = \ 0.001$.
> Kombinasi ini terbukti efektif dalam meningkatkan generalisasi model
> pada data jaringan yang kompleks dan tidak seimbang (Ferrag dkk.,
> 2020; Kunang dkk., 2021b).

**Convolutional Neural Network 1D (CNN-1D)**

*CNN-1D* digunakan untuk mengekstraksi pola lokal dari vektor fitur lalu
lintas jaringan. Pendekatan ini telah banyak digunakan dalam literatur
NIDS karena kemampuannya menangkap dependensi lokal antar fitur tanpa
memerlukan rekonstruksi data menjadi format citra. Untuk stateginya
sebagai berikut:

a.  Struktur Ekstraksi Fitur:

> Model terdiri dari tiga lapisan konvolusi bertingkat. Untuk
> klasifikasi *binary* digunakan konfigurasi filter (64 → 32 → 16),
> sedangkan untuk klasifikasi *multi-class* digunakan konfigurasi yang
> lebih lebar (128 → 64 → 32). Setiap lapisan konvolusi diikuti oleh
> batch normalization untuk mempercepat konvergensi dan meningkatkan
> stabilitas pelatihan (Ferrag dkk., 2020).

b.  Klasifikasi:

> Fitur hasil konvolusi diratakan (flatten) dan diproses melalui dua
> lapisan fully connected (128 → 64) sebelum masuk ke lapisan keluaran
> (Ferrag dkk., 2020).

Arsitektur *CNN-1D* dipilih karena telah terbukti memberikan performa
yang kompetitif dalam deteksi intrusi berbasis trafik jaringan,
khususnya pada dataset dengan dimensi fitur tinggi seperti ToN-IoT
(Moustafa, 2021).

#### Strategi Distribusi Data Antar Klien (Non-IID Simulation)

Dalam *Federated Learning*, performa model global sangat dipengaruhi
oleh karakteristik distribusi data pada masing-masing klien (Li dkk.,
2020). Untuk mensimulasikan kondisi heterogenitas data yang
merepresentasikan lingkungan *smart city*, penelitian ini menerapkan
Distribusi *dirichlet* sebagai mekanisme pembagian data antar klien (Zhu
dkk., 2021).

Distribusi *dirichlet* digunakan untuk mengatur proporsi kelas serangan
yang dimiliki oleh setiap klien tanpa mengubah struktur fitur dataset.
Pendekatan ini memungkinkan simulasi berbagai tingkat ketidakseragaman
data (Non-IID) secara terkontrol melalui parameter konsentrasi
$(\alpha)$. Nilai $\alpha$ yang kecil menghasilkan distribusi data yang
sangat timpang, di mana klien cenderung didominasi oleh kelas tertentu,
sedangkan nilai $\alpha$ yang lebih besar menghasilkan distribusi yang
lebih mendekati kondisi IID (Zhu dkk., 2021).

Dalam konteks penelitian ini, penggunaan distribusi *dirichlet* dipilih
karena dua alasan utama. Pertama, pendekatan ini banyak digunakan dalam
penelitian *Federated Learning* untuk mengevaluasi ketahanan algoritma
agregasi terhadap heterogenitas data (Li dkk., 2020). Kedua, Dirichlet
mampu merepresentasikan kondisi realistis *smart city*, di mana setiap
*gateway* mengamati pola lalu lintas jaringan yang berbeda sesuai dengan
karakteristik wilayah operasionalnya (Al-Huthaifi dkk., 2023).

Simulasi lingkungan *smart city* dilakukan dengan membagi dataset ke
lima klien menggunakan distribusi *dirichlet*. Parameter konsentrasi
$\alpha$ digunakan untuk mengendalikan tingkat heterogenitas data antar
klien. Dengan konfigurasi nilai sebagai berikut:

a.  Non-IID Ekstrem (α = 0.3)

> Mewakili kondisi di mana setiap *gateway* didominasi oleh jenis lalu
> lintas atau serangan tertentu.

b.  IID-like (α = 5.0)

> Mewakili kondisi distribusi data yang relatif seimbang antar klien.

Simulasi Non-IID yang dihasilkan melalui distribusi *dirichlet* menjadi
dasar untuk mengevaluasi perbedaan performa antara algoritma *Federated
Averaging* (FedAvg) dan *Federated Proximal* (FedProx), khususnya dalam
hal stabilitas konvergensi dan kemampuan generalisasi model global.

#### Optimasi Hyperparameter dan Reprodusibilitas

Optimasi hyperparameter pada penelitian ini dilakukan menggunakan
pendekatan limited *grid search* untuk menyeimbangkan antara performa
model dan efisiensi komputasi. Strategi ini dipilih karena pelatihan
*Federated Learning* melibatkan biaya komunikasi dan komputasi yang
lebih tinggi dibandingkan pelatihan terpusat. Oleh karena itu, ruang
pencarian hyperparameter dibatasi berdasarkan praktik umum dan
rekomendasi pada literatur *Federated Learnin*g dan *Network Intrusion
Detection System* (NIDS).

Kombinasi *hyperparameter* yang dievaluasi meliputi:

a.  Local Epochs: 1 dan 2

> Jumlah *epoch* pelatihan lokal dibatasi pada nilai kecil untuk
> mengurangi risiko *client drift*, khususnya pada skenario distribusi
> data Non-IID. Pelatihan lokal yang terlalu lama dapat menyebabkan
> pembaruan model klien menyimpang signifikan dari model global,
> sehingga menghambat konvergensi federated (Li dkk., 2020; McMahan
> dkk., 2023).

b.  Batch Size: 256, 512, dan 1024

> Variasi ukuran *batch* digunakan untuk mengevaluasi *trade-off* antara
> stabilitas gradien dan efisiensi komputasi pada dataset lalu lintas
> jaringan berskala besar. Ukuran *batch* yang lebih besar cenderung
> menghasilkan gradien yang lebih stabil, namun meningkatkan kebutuhan
> memori dan waktu komputasi pada perangkat *gateway*.

c.  Learning Rate: 0.001 dan 0.0005

> Rentang learning rate dipilih berdasarkan praktik umum pada pelatihan
> model deep learning menggunakan *Adam optimizer*. Nilai ini bertujuan
> menjaga proses konvergensi yang stabil serta menghindari osilasi atau
> divergensi selama pelatihan terdistribusi (APA HERE).

d.  Nilai $(\mu)$ : 0.01 dan 0.001 pada FedProx

> Evaluasi parameter proksimal $(\mu)$ dilakukan pada tahap lanjutan
> setelah konfigurasi terbaik FedAvg diperoleh melalui grid search.
> Nilai $\mu$ yang lebih kecil memberikan fleksibilitas pada pembaruan
> model lokal, sedangkan nilai yang lebih besar memperkuat regularisasi
> untuk menekan dampak heterogenitas data antar klien. Pendekatan ini
> memungkinkan analisis terfokus terhadap pengaruh mekanisme FedProx
> tanpa memperluas ruang pencarian hyperparameter secara berlebihan (Li
> dkk., 2020).

Untuk menjamin reprodusibilitas eksperimen, seluruh proses pelatihan
dikendalikan dengan penetapan random seed 42 dan python hash seed 42
yang konsisten pada seluruh pustaka utama yang digunakan, termasuk
*NumPy*, *TensorFlow*, dan lingkungan sistem. Pendekatan ini bertujuan
memastikan bahwa perbedaan hasil eksperimen semata-mata disebabkan oleh
variasi konfigurasi *hyperparameter* dan algoritma *federated*, bukan
oleh faktor acak yang tidak terkontrol (Frightera, 2023).

### Evaluation

Tahap evaluasi dalam penelitian ini bertujuan untuk menetapkan kerangka
penilaian kinerja sistem deteksi intrusi berbasis *Federated Learning*
yang diusulkan. Evaluasi dirancang untuk menilai dua aspek utama, yaitu
kualitas deteksi serangan dan karakteristik operasional pelatihan
terdistribusi, dengan mengacu pada landasan teori evaluasi yang telah
dijabarkan pada Bab II Bagian 2.8.

Kerangka evaluasi ini digunakan sebagai acuan dalam pelaporan dan
analisis hasil eksperimen pada Bab IV.

#### Evaluasi Kinerja Klasifikasi

Evaluasi performa klasifikasi dilakukan menggunakan Confusion Matrix
sebagai dasar pengukuran, sebagaimana dijelaskan pada Subbab 2.8.1.
Untuk skenario klasifikasi *binary*, confusion matrix digunakan untuk
merepresentasikan kemampuan model dalam membedakan antara lalu lintas
normal dan lalu lintas serangan. Pada skenario klasifikasi
*multi-class*, confusion matrix diperluas menjadi matriks berdimensi
$C \times C$ untuk memetakan distribusi prediksi pada setiap kategori
serangan.

a.  Berdasarkan confusion matrix tersebut, kinerja model dievaluasi
    menggunakan metrik-metrik berikut:

b.  Accuracy, untuk mengukur tingkat ketepatan prediksi secara
    keseluruhan.

c.  Precision, untuk mengevaluasi keandalan model dalam menghasilkan
    peringatan serangan.

d.  Recall, untuk mengukur kemampuan model dalam mendeteksi seluruh
    serangan yang terjadi.

e.  F1-Score, sebagai ukuran keseimbangan antara precision dan recall
    pada kondisi ketimpangan kelas.

f.  ROC-AUC, untuk menilai kemampuan model dalam membedakan kelas pada
    berbagai nilai ambang Keputusan.

Seluruh metrik dihitung pada data uji yang terpisah dari data pelatihan
guna menjaga objektivitas evaluasi.

#### Evaluasi pada Lingkungan Federated Learning

Selain performa klasifikasi, evaluasi juga difokuskan pada karakteristik
pelatihan dalam lingkungan Federated Learning yang bersifat
terdistribusi.

**Evaluasi Distribusi Data Antar Klien**

Evaluasi dilakukan pada skenario distribusi data IID dan Non-IID.
Kondisi Non-IID disimulasikan menggunakan pendekatan partisi data
berbasis Distribusi Dirichlet, di mana parameter konsentrasi $\alpha$
digunakan untuk mengontrol tingkat heterogenitas data antar klien.
Pendekatan ini memungkinkan pengujian sistem pada berbagai tingkat
ketimpangan distribusi data yang merepresentasikan kondisi nyata
lingkungan Smart City.

**Evaluasi Stabilitas Pelatihan Terdistribusi**

Stabilitas pelatihan dievaluasi dengan mengamati konsistensi pembaruan
model global pada setiap ronde komunikasi. Evaluasi ini dilakukan untuk
menilai kemampuan algoritma Federated Learning dalam mempertahankan
proses pelatihan yang stabil pada kondisi distribusi data yang tidak
seragam.

**Evaluasi Efisiensi Operasional**

Efisiensi sistem Federated Learning dievaluasi dari aspek operasional,
meliputi:

a.  Waktu pelatihan per ronde komunikasi, yang mencerminkan beban
    komputasi dan agregasi model.

b.  Jumlah ronde komunikasi, sebagai indikator efisiensi proses
    pembelajaran terdistribusi.

Evaluasi efisiensi ini bertujuan untuk memastikan bahwa sistem yang
diusulkan tetap sesuai dengan keterbatasan sumber daya pada perangkat
*gateway* IoT.

#### Keterkaitan Evaluasi dengan Tujuan Penelitian

Kerangka evaluasi yang diterapkan dalam penelitian ini dirancang untuk
secara langsung mendukung pencapaian tujuan penelitian, khususnya dalam:

a.  Menilai efektivitas Federated Learning untuk deteksi dan klasifikasi
    serangan jaringan.

b.  Menganalisis dampak heterogenitas data antar klien terhadap performa
    sistem.

c.  Mengevaluasi kesesuaian pendekatan yang diusulkan untuk diterapkan
    pada lingkungan *smart city* yang bersifat terdistribusi dan
    sensitif terhadap privasi data.

## BAB IV HASIL EKSPERIMEN

Bab ini menyajikan hasil eksperimen dan analisis kinerja sistem deteksi
intrusi berbasis *Federated Learning* yang telah dirancang pada bagian
BAB III Metodologi. Evaluasi dilakukan untuk menilai kemampuan model
dalam mendeteksi dan mengklasifikasikan serangan jaringan pada
lingkungan *smart city* yang bersifat terdistribusi dan heterogen.

Seluruh eksperimen dilaksanakan berdasarkan skenario pemodelan,
pembagian data, serta konfigurasi *hyperparameter* yang telah dijelaskan
pada tahap pemodelan dan persiapan data. Evaluasi difokuskan pada dua
aspek utama, yaitu kualitas prediksi model deteksi intrusi dan
stabilitas pelatihan dalam skema *Federated Learning*.

Kinerja sistem dianalisis menggunakan metrik evaluasi klasifikasi yang
telah dibahas pada Bab II, termasuk *Accuracy*, *Precision*, *Recall*,
*F1-Score*, dan *ROC-AUC*, serta metrik operasional *Federated Learning*
seperti stabilitas konvergensi dan sensitivitas terhadap heterogenitas
data. Hasil yang diperoleh kemudian dibahas secara komparatif untuk
menjawab rumusan masalah penelitian.

### Hasil Data Understanding

Tahap *data understanding* dalam kerangka *CRISP-DM* bertujuan untuk
memverifikasi kesesuaian dataset terhadap skenario eksperimen yang
dirancang. Dataset ToN-IoT Network yang digunakan dalam penelitian ini
telah dijelaskan secara rinci pada Bab II, meliputi arsitektur testbed,
jenis serangan, dan struktur fitur. Oleh karena itu, pada tahap ini
analisis difokuskan pada karakteristik data yang relevan secara langsung
terhadap implementasi *Federated Learning* (FL) dalam lingkungan *smart
city*.

Secara khusus, analisis data diarahkan untuk mengevaluasi distribusi
kelas, kualitas data, serta karakteristik statistik fitur guna
memastikan bahwa dataset mampu merepresentasikan kondisi data
*heterogeneity* dan *class imbalance* yang lazim terjadi pada sistem
jaringan terdistribusi.

#### Distribusi Kelas dan Implikasi Non-IID

Analisis distribusi kelas dilakukan untuk mengidentifikasi proporsi
masing-masing kategori serangan dan lalu lintas normal dalam dataset.
Hasil analisis menunjukkan bahwa dataset ToN-IoT memiliki karakteristik
class imbalance yang signifikan, di mana kelas lalu lintas normal
mendominasi keseluruhan data, sementara beberapa kategori serangan
memiliki jumlah sampel yang jauh lebih terbatas.

Distribusi ini ditunjukkan pada Table 2.3.6 dan Gambar 4.1, di mana
sebagian besar kategori serangan memiliki proporsi relatif seimbang,
namun terdapat ketimpangan ekstrem pada kelas *Man-in-the-Middle* (MITM)
yang hanya mencakup sebagian kecil dari total sampel. Kondisi ini
mencerminkan skenario realistis pada lingkungan *smart city*, di mana
kemunculan serangan tertentu bersifat jarang namun berdampak tinggi.

Ketimpangan distribusi kelas ini menjadi dasar dalam perancangan skema
pembagian data antar klien menggunakan distribusi *dirichlet*.
Pendekatan ini digunakan untuk mensimulasikan kondisi Non-IID pada
Federated Learning, sehingga setiap klien memiliki karakteristik data
lokal yang berbeda, baik dari sisi proporsi kelas maupun jumlah sampel.

![](media/image6.png){width="3.2566371391076117in"
height="2.344771434820647in"}

[]{#_Toc217653246 .anchor}Gambar 4.1 Distribusi kategori serangan pada
dataset ToN-IoT Network

#### Kualitas dan Integritas Data

Evaluasi kualitas data dilakukan untuk memastikan bahwa dataset bebas
dari permasalahan mendasar yang dapat memengaruhi proses pelatihan
model.

Pemeriksaan missing values menunjukkan bahwa sejumlah fitur memiliki
nilai kosong dalam proporsi tinggi, sebagaimana terlihat pada Gambar
4.1.2 Kondisi ini tidak disebabkan oleh kesalahan pencatatan data,
melainkan merupakan konsekuensi alami dari karakteristik lalu lintas
jaringan. Fitur-fitur tersebut hanya relevan pada protokol tertentu
seperti *HTTP*, *DNS*, atau *SSL*, sehingga nilai kosong mengindikasikan
bahwa koneksi jaringan tidak menggunakan protokol yang bersangkutan.

![](media/image7.png){width="5.035398075240595in"
height="2.8588035870516184in"}

[]{#_Toc217653247 .anchor}Gambar 4.2 Persentase Missing Values pada
Fitur Spesifik Protokol

Oleh karena itu, nilai hilang ini dipertahankan sebagai informasi
semantik dan ditangani secara protocol-aware pada tahap data
preparation.

#### Karakteristik statistic dan Relevansi Fitur

Analisis statistik dilakukan terhadap fitur numerik utama untuk memahami
pola lalu lintas jaringan yang membedakan antara aktivitas normal dan
berbagai jenis serangan. Hasil analisis pada Gambar 4.3 menunjukkan
bahwa sebagian besar fitur numerik memiliki distribusi yang skewed,
dengan konsentrasi nilai pada rentang rendah dan keberadaan outlier
ekstrem pada koneksi tertentu.

![](media/image8.png){width="4.548672353455818in"
height="3.0203543307086615in"}

[]{#_Toc217653248 .anchor}Gambar 4.3 Distribusi Fitur Numerik Utama

![](media/image9.png){width="5.034884076990376in"
height="4.392904636920385in"}

[]{#_Toc217653249 .anchor}Gambar 4.4 Distribusi Fitur Numerik Utama

Pola ini mengindikasikan bahwa sebagian besar lalu lintas jaringan
bersifat ringan dan berdurasi singkat. Namun, seperti terlihat pada
scatter plot di Gambar 4.4, serangan tertentu seperti *Denial of
Service* (DoS) dan *Distributed Denial of Service* (DDoS) menghasilkan
volume data yang jauh lebih besar (klaster di kanan atas). Sebaliknya,
serangan *Man-in-the-Middle* (MITM) cenderung memiliki durasi koneksi
yang lebih panjang dibandingkan kategori lainnya. Hal ini dikonfirmasi
oleh statistik pada Tabel 4.3.

[]{#_Toc217653225 .anchor}Tabel 4.1 Statistik Deskriptif Fitur Utama per
Tipe Serangan

  --------------------------------------------------------------------------------------
    **Attack    **Sample    **src_bytes_mean**   **dst_bytes_mean**   **duration_mean**
     Type**      Size**                                              
  ------------ ----------- -------------------- -------------------- -------------------
    backdoor      20000           173.17               794.41               37.02

      ddos        20000        2.38395e+06          2.49887e+06             17.08

      dos         20000           21.19               4613.17               0.49

   injection      20000           194818               200242               1.45

      mitm        1043           14528.9              4657.85               28.05

     normal       50000          2127.62              9767.99               3.99

    password      20000           127.49              1222.27               0.71

   ransomware     20000             0                    0                    0

    scanning      20000            4.05                27.53                0.31

      xss         20000           138478               510.22               12.76
  --------------------------------------------------------------------------------------

Terakhir, analisis korelasi antar fitur numerik dilakukan untuk
mendeteksi redundansi. Berdasarkan heatmap pada Gambar 4.5, terlihat
bahwa sebagian besar pasangan fitur memiliki tingkat korelasi yang
rendah mendekati nol, warna abu-abu.

![](media/image10.png){width="5.539822834645669in"
height="2.4840048118985125in"}

[]{#_Toc217653250 .anchor}Gambar 4.5 Heatmap Korelasi Pearson Antar
Fitur Numerik

Tidak ditemukan korelasi tinggi yang mengindikasikan redundansi fitur
secara signifikan. Temuan ini menunjukkan bahwa setiap fitur numerik
membawa informasi yang relatif independen, sehingga proses seleksi fitur
berbasis korelasi tidak diperlukan. Oleh karena itu, strategi seleksi
fitur difokuskan pada metode berbasis variansi (Variance Threshold)
untuk menghilangkan fitur dengan kontribusi informasi yang rendah.

### Hasil Data Preparation

Tahap persiapan data bertujuan untuk mentransformasikan data mentah
dataset ToN-IoT menjadi format numerik yang konsisten dan siap digunakan
dalam pelatihan model *Federated Learning*. Implementasi tahap ini
dilakukan melalui serangkaian proses sistematis yang mencakup
pembersihan data berbasis protokol, transformasi fitur, seleksi fitur,
dan standardisasi. Seluruh proses dirancang untuk menjaga integritas
semantik data dan mencegah kebocoran informasi (data leakage) antara
data latih dan data uji.

#### Implementasi Pembersihan Data

Berdasarkan strategi yang dirancang pada Bab 3, proses pembersihan data
menangani missing values secara kontekstual. Nilai yang hilang pada
kolom spesifik protokol tidak dihapus atau diimputasi dengan rata-rata
global, melainkan diisi dengan nilai yang merepresentasikan \"ketiadaan
protokol\" atau modus dari protokol tersebut jika aktif.

Realisasi strategi penanganan missing values yang diterapkan adalah
sebagai berikut:

[]{#_Toc217653226 .anchor}Tabel 4.2 Strategi Implementasi Penanganan
Missing Values

  --------------------------------------------------------------
  **Kategori    **Kolom        **Nilai       **Alasan Semantik**
  Fitur**       Terkait**      Imputasi**    
  ------------- -------------- ------------- -------------------
  DNS           dns_query,     Mode (jika    Membedakan koneksi
                dns_rcode,     trafik DNS)   DNS valid dan
                dll.           atau -1       non-DNS.

  HTTP          http_method,   Mode (jika    Menandai koneksi
                http_uri, dll. trafik HTTP)  yang bukan
                               atau 0        aktivitas web.

  SSL           ssl_cipher,    \'none\'      Menandai koneksi
                ssl_subject,                 yang tidak
                dll.                         terenkripsi.

  Numerik Lain  Durasi, bytes, Median        Mengatasi skewness
                pkts                         distribusi data.

  Kategorikal   Service,       Mode atau     Menangani kategori
  Lain          proto, state   \'unknown\'   yang hilang.
  --------------------------------------------------------------

Kolom-kolom yang tidak relevan untuk deteksi intrusi atau yang bersifat
unik untuk setiap koneksi seperti *ip address* dan *port* sumber/tujuan
dihapus untuk mengurangi noise dan mencegah model menghafal alamat
spesifik.

#### Transformasi dan Seleksi Fitur

Transformasi variabel kategorikal dilakukan untuk mengonversi data
non-numerik menjadi format matriks yang dapat diproses oleh *deep
learning*.

a.  Label Encoding: Diterapkan pada variabel target *type* untuk
    klasifikasi *multi class*, mengubah 10 jenis serangan menjadi
    integer 0-9 pada Table 4.3.

> []{#_Toc217653227 .anchor}Tabel 4.3 Pemetaan Label Encoding
> (*Multi-class*)

  ----------------------------------------------------------------
  **Encoded   **Kategori Serangan  **Deskripsi Singkat**
  Label       (Asli)**             
  (Int)**                          
  ----------- -------------------- -------------------------------
  0           backdoor             Serangan akses belakang

  1           ddos                 Distributed Denial of Service

  2           dos                  Denial of Service

  3           injection            Serangan injeksi kode/SQL

  4           mitm                 Man-in-the-Middle (Kelas
                                   Minoritas)

  5           normal               Lalu Lintas Normal

  6           password             Serangan brute-force password

  7           ransomware           Serangan enkripsi data jahat

  8           scanning             Pemindaian port/jaringan

  9           xss                  Cross-Site Scripting
  ----------------------------------------------------------------

b.  One-Hot Encoding: Diterapkan pada fitur kategorikal nominal seperti
    *service*, *conn_state* untuk menghilangkan asumsi urutan ordinal.

Setelah encoding, fitur-fitur yang memiliki variansi sangat rendah
(nilai konstan atau hampir konstan) dieliminasi menggunakan metode
*variance threshold* dengan ambang batas 0.01. Hal ini menghasilkan
pengurangan dimensi fitur yang signifikan tanpa mengorbankan informasi
diskriminatif.

Selanjutnya, fitur numerik distandardisasi menggunakan *StandardScaler*
untuk mencapai distribusi dengan rata-rata 0 dan deviasi standar 1.
Proses fitting scaler dilakukan secara eksklusif pada data latih
(training set) untuk mencegah kebocoran statistik ke data uji.

#### Hasil Pembagian Data (Data Splitting)

Data dibagi menggunakan metode stratified splitting dengan rasio 80:20.
Metode ini memastikan bahwa proporsi kelas minoritas, khususnya serangan
MITM (0.49%), tetap terjaga baik di data latih maupun data uji.

[]{#_Toc217653228 .anchor}Tabel 4.4 Dimensi Data Hasil Preprocessing

  ---------------------------------------------------------------
   **Himpunan     **Jumlah     **Persentase**    **Keterangan**
     Data**       Sampel**                     
  ------------ -------------- ---------------- ------------------
  Training Set    168,834           80%         Digunakan untuk
                                               pelatihan lokal di
                                                    klien FL

    Test Set       42,209           20%         Digunakan untuk
                                               evaluasi global di
                                                     server

     Total        211,043           100%         Total records
                                                setelah cleaning
  ---------------------------------------------------------------

#### Implementasi Pipeline (Core Code)

Proses *preprocessing* diimplementasikan dalam dua *pipeline* terpisah
untuk skenario klasifikasi *binary* dan *multi-class*. Kode berikut
menunjukkan implementasi inti yang menggabungkan seluruh tahapan di
atas.

**Pipeline Klasifikasi *Binary***

Pada skenario ini, seluruh kategori serangan disatukan menjadi label 1
(Attack) dan lalu lintas normal menjadi 0 (Normal).

+----------------------------------------------------------------------+
| **def** prepare_binary_classification(**self**, **df**):             |
|                                                                      |
|     *\# 1. Protocol-Aware Cleaning*                                  |
|                                                                      |
|     df **=** *self*.clean_data(df)                                   |
|                                                                      |
|     *\# 2. Define Target (0: Normal, 1: Attack)*                     |
|                                                                      |
|     *\# Drop detailed attack \'type\', keep binary \'label\'*        |
|                                                                      |
|     df_binary **=** df.drop(**columns=**\[\'type\'\] **+**           |
| *self*.DROP_COLS, **errors=**\'ignore\')                             |
|                                                                      |
|     X **=** df_binary.drop(\'label\', **axis=1**)                    |
|                                                                      |
|     y **=** df_binary\[\'label\'\]                                   |
|                                                                      |
|     *\# 3. Stratified Train-Test Split*                              |
|                                                                      |
|     X_train, X_test, y_train, y_test **=** train_test_split(         |
|                                                                      |
|         X, y, **test_size=0.2**, **random_state=42**, **stratify=**y |
|                                                                      |
|     )                                                                |
|                                                                      |
|     *\# 4. Encoding & Selection Pipeline*                            |
|                                                                      |
|     *\# OneHotEncoder -\> VarianceThreshold -\> StandardScaler*      |
|                                                                      |
|     *\# Note: Fit only on X_train to prevent leakage*                |
|                                                                      |
|     X_train_processed **=** *self*.pipeline.fit_transform(X_train)   |
|                                                                      |
|     X_test_processed **=** *self*.pipeline.transform(X_test)         |
|                                                                      |
|     **return** {                                                     |
|                                                                      |
|         \'X_train\': X_train_processed, \'X_test\':                  |
| X_test_processed,                                                    |
|                                                                      |
|         \'y_train\': y_train.values,    \'y_test\': y_test.values    |
|                                                                      |
|     }                                                                |
+======================================================================+

[]{#_Toc217653251 .anchor}Gambar 4.6 Pipeline Klasifikasi *Binary Class*

**Pipeline Klasifikasi *Multi-class***

Pada skenario ini, target variabel adalah 10 kelas spesifik serangan.
Implementasi mencakup Label Encoding untuk target variabel.

+----------------------------------------------------------------------+
| **def** prepare_multiclass_classification(**self**, **df**):         |
|                                                                      |
|     *\# 1. Protocol-Aware Cleaning*                                  |
|                                                                      |
|     df **=** *self*.clean_data(df)                                   |
|                                                                      |
|     *\# 2. Define Target (10 Classes)*                               |
|                                                                      |
|     *\# Drop binary \'label\', keep detailed \'type\'*               |
|                                                                      |
|     df_multi **=** df.drop(**columns=**\[\'label\'\] **+**           |
| *self*.DROP_COLS, **errors=**\'ignore\')                             |
|                                                                      |
|     X **=** df_multi.drop(\'type\', **axis=1**)                      |
|                                                                      |
|     y **=** df_multi\[\'type\'\]                                     |
|                                                                      |
|     *\# 3. Label Encoding for Target*                                |
|                                                                      |
|     le **=** LabelEncoder()                                          |
|                                                                      |
|     y_encoded **=** le.fit_transform(y)                              |
|                                                                      |
|     *\# 4. Stratified Train-Test Split*                              |
|                                                                      |
|     X_train, X_test, y_train, y_test **=** train_test_split(         |
|                                                                      |
|         X, y_encoded, **test_size=0.2**, **random_state=42**,        |
| **stratify=**y_encoded                                               |
|                                                                      |
|     )                                                                |
|                                                                      |
|     *\# 5. Encoding & Selection Pipeline*                            |
|                                                                      |
|     *\# OneHotEncoder -\> VarianceThreshold -\> StandardScaler*      |
|                                                                      |
|     X_train_processed **=** *self*.pipeline.fit_transform(X_train)   |
|                                                                      |
|     X_test_processed **=** *self*.pipeline.transform(X_test)         |
|                                                                      |
|     **return** {                                                     |
|                                                                      |
|         \'X_train\': X_train_processed, \'X_test\':                  |
| X_test_processed,                                                    |
|                                                                      |
|         \'y_train\': y_train,           \'y_test\': y_test,          |
|                                                                      |
|         \'num_classes\': len(le.classes\_), \'classes\':             |
| le.classes\_                                                         |
|                                                                      |
|     }                                                                |
+======================================================================+

[]{#_Toc217653252 .anchor}Gambar 4.7 Pipeline Klasifikasi *Binary Class*

#### Output Artifacts

Hasil akhir dari proses ini disimpan dalam format serialisasi *.pkl*
yang memuat data latih dan uji yang telah diskalakan, label yang telah
dienkripsi, serta metadata *pipeline* *scaler* dan *encoder* yang telah
di-*fitting*. Artefak ini (binary_preprocessed.pkl dan
multiclass_preprocessed.pkl) menjadi input langsung bagi algoritma
*Federated Learning* untuk mendistribusikan data ke klien tanpa perlu
melakukan pemrosesan ulang, menjamin konsistensi fitur di seluruh
eksperimen.

### Modeling dan Implementasi Sistem

Tahap Modeling merupakan inti dari implementasi penelitian ini, di mana
arsitektur jaringan saraf tiruan dan algoritma agregasi Federated
Learning dikonfigurasi untuk membangun sistem deteksi intrusi yang
terdistribusi. Fokus utama pada tahap ini adalah penerjemahan desain
arsitektur model *MLP* dan *CNN-1D* ke dalam kode yang dapat dieksekusi,
serta konfigurasi strategi pelatihan federated untuk menangani
heterogenitas data pada lingkungan *smart city*.

Implementasi dilakukan menggunakan kerangka kerja simulasi Flower (flwr)
berbasis Python, yang memungkinkan orkestrasi pelatihan antara server
pusat dan klien (*gateway*) secara efisien.

#### Konfigurasi Lingkungan Eksperimen

Untuk menjamin validitas dan reprodusibilitas hasil eksperimen,
lingkungan simulasi diatur dengan parameter tetap yang konsisten di
seluruh skenario pengujian. Tabel 4.5 Konfigurasi Lingkungan
Tetapmerinci spesifikasi teknis lingkungan eksperimen yang digunakan.

[]{#_Ref217634792 .anchor}Tabel 4.5 Konfigurasi Lingkungan Tetap

  ----------------------------------
  **Parameter**   **Nilai**
  --------------- ------------------
  Framework       Flower (flwr)
                  1.24.0

  Backend         TensorFlow 2.20.0

  Jumlah Klien    5

  Jumlah Rounds   20

  Distribusi Data Non-IID
                  (Dirichlet)

  Random Seed dan 42
  Python Hash     
  Seed            
  ----------------------------------

Selain parameter di atas, kontrol variabilitas acak diterapkan secara
ketat pada level kode untuk memastikan setiap eksekusi menghasilkan
keluaran yang deterministik. Implementasi *seeding* dilakukan Gambar 4.8
konfigurasi Tetap.

+----------------------------------------------------------------------+
| **import** numpy **as** np                                           |
|                                                                      |
| **import** tensorflow **as** tf                                      |
|                                                                      |
| **import** os                                                        |
|                                                                      |
| *\# Set random seeds untuk reprodusibilitas*                         |
|                                                                      |
| np.random.seed(**42**)                                               |
|                                                                      |
| tf.random.set_seed(**42**)                                           |
|                                                                      |
| os.environ\[\'TF_CPP_MIN_LOG_LEVEL\'\] **=** \'2\'                   |
|                                                                      |
| os.environ\[\'PYTHONHASHSEED\'\] **=** \'42\'                        |
+======================================================================+

[]{#_Ref217634817 .anchor}Gambar 4.8 konfigurasi Tetap

Konfigurasi ini memastikan bahwa perbedaan performa yang diamati
semata-mata disebabkan oleh variasi algoritma atau hyperparameter yang
diuji, bukan oleh inisialisasi bobot yang acak.

#### Strategi Horizontal Federated Learning

Sesuai dengan desain penelitian, sistem ini menerapkan skema Horizontal
Federated Learning (HFL). Dalam skema ini, setiap klien
(merepresentasikan *gateway* IoT) memiliki struktur fitur yang identik
(35 fitur hasil preprocessing), namun memiliki sampel data yang berbeda
berdasarkan lokasi dan pola trafik lokalnya .

Dalam implementasi ini, server bertugas menginisialisasi model global
dan mendistribusikannya ke 5 klien. Setiap klien melakukan pelatihan
lokal (local training) menggunakan data privat mereka dan hanya
mengirimkan pembaruan parameter model (weights) kembali ke server untuk
agregasi. Data mentah lalu lintas jaringan tetap berada di sisi klien,
sehingga privasi data terjaga secara inheren.

#### Implementasi Arsitektur Deep Learning

Dua arsitektur model, yaitu Multi-Layer Perceptron (MLP) dan
Convolutional Neural Network 1D (CNN-1D), diimplementasikan menggunakan
TensorFlow/Keras. Kedua model dirancang fleksibel untuk menangani tugas
klasifikasi *binary* *output* 1 *neuron* dengan *sigmoid* maupun
*multi-class* output 10 neuron dengan *softmax*.

**Multi-Layer Perceptron (MLP)**

Model MLP dirancang sebagai baseline yang efisien untuk mempelajari
hubungan non-linear antar fitur statistik. Arsitektur ini menggunakan
lapisan Dense bertingkat dengan regularisasi Dropout dan L2 untuk
mencegah overfitting.

+----------------------------------------------------------------------+
| **def** create_mlp_model(**input_shape**, **num_classes=1**,         |
| **learning_rate=0.001**):                                            |
|                                                                      |
|     model **=** Sequential()                                         |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Layer 1: Input & Hidden*                                     |
|                                                                      |
|     model.add(Dense(**256** **if** num_classes **==** **1** **else** |
| **512**, **activation=**\'relu\',                                    |
|                                                                      |
|                     **input_shape=**(input_shape,),                  |
| **kernel_regularizer=**l2(**0.001**)))                               |
|                                                                      |
|     model.add(BatchNormalization())                                  |
|                                                                      |
|     model.add(Dropout(**0.3** **if** num_classes **==** **1**        |
| **else** **0.4**))                                                   |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Layer 2*                                                     |
|                                                                      |
|     model.add(Dense(**128** **if** num_classes **==** **1** **else** |
| **256**, **activation=**\'relu\',                                    |
|                                                                      |
|                     **kernel_regularizer=**l2(**0.001**)))           |
|                                                                      |
|     model.add(Dropout(**0.3** **if** num_classes **==** **1**        |
| **else** **0.4**))                                                   |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Layer 3 & 4 (Simplified)*                                    |
|                                                                      |
|     model.add(Dense(**64** **if** num_classes **==** **1** **else**  |
| **128**, **activation=**\'relu\'))                                   |
|                                                                      |
|     model.add(Dropout(**0.2**))                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Output Layer*                                                |
|                                                                      |
|     **if** num_classes **==** **1**:                                 |
|                                                                      |
|         model.add(Dense(**1**, **activation=**\'sigmoid\'))          |
|                                                                      |
|         loss **=** \'binary_crossentropy\'                           |
|                                                                      |
|     **else**:                                                        |
|                                                                      |
|         model.add(Dense(num_classes, **activation=**\'softmax\'))    |
|                                                                      |
|         loss **=** \'sparse_categorical_crossentropy\'               |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
| model.compile(**optimizer=**Adam(**learning_rate=**learning_rate),   |
|                                                                      |
|                   **loss=**loss, **metrics=**\[\'accuracy\'\])       |
|                                                                      |
|     **return** model                                                 |
+======================================================================+

[]{#_Toc217653254 .anchor}Gambar 4.9 Pipeline MLP

**Multi-Layer Perceptron (MLP)**

Model *CNN-1D* diimplementasikan untuk menangkap pola lokal spasial dari
fitur jaringan. Input data di-reshape menjadi format 3D *samples,
features, 1* agar kompatibel dengan lapisan konvolusi 1D.

+----------------------------------------------------------------------+
| **def** create_cnn_model(**input_shape**, **num_classes=1**,         |
| **learning_rate=0.001**):                                            |
|                                                                      |
|     model **=** Sequential()                                         |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Reshape input for CNN (batch, steps, channels)*              |
|                                                                      |
|     model.add(Input(**shape=**(input_shape, **1**)))                 |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Conv Block 1*                                                |
|                                                                      |
|     model.add(Conv1D(**64** **if** num_classes **==** **1** **else** |
| **128**, **3**, **activation=**\'relu\', **padding=**\'same\'))      |
|                                                                      |
|     model.add(BatchNormalization())                                  |
|                                                                      |
|     model.add(MaxPooling1D(**2**))                                   |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Conv Block 2*                                                |
|                                                                      |
|     model.add(Conv1D(**32** **if** num_classes **==** **1** **else** |
| **64**, **3**, **activation=**\'relu\', **padding=**\'same\'))       |
|                                                                      |
|     model.add(BatchNormalization())                                  |
|                                                                      |
|     model.add(MaxPooling1D(**2**))                                   |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Flatten & Dense*                                             |
|                                                                      |
|     model.add(Flatten())                                             |
|                                                                      |
|     model.add(Dense(**128**, **activation=**\'relu\'))               |
|                                                                      |
|     model.add(Dropout(**0.4**))                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|     *\# Output Layer*                                                |
|                                                                      |
|     **if** num_classes **==** **1**:                                 |
|                                                                      |
|         model.add(Dense(**1**, **activation=**\'sigmoid\'))          |
|                                                                      |
|         loss **=** \'binary_crossentropy\'                           |
|                                                                      |
|     **else**:                                                        |
|                                                                      |
|         model.add(Dense(num_classes, **activation=**\'softmax\'))    |
|                                                                      |
|         loss **=** \'sparse_categorical_crossentropy\'               |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
| model.compile(**optimizer=**Adam(**learning_rate=**learning_rate),   |
|                                                                      |
|                   **loss=**loss, **metrics=**\[\'accuracy\'\])       |
|                                                                      |
|     **return** model                                                 |
+======================================================================+

[]{#_Toc217653255 .anchor}Gambar 4.10 Pipeline CCN-1D

#### Simulasi Distribusi Data Non-IID

Untuk mensimulasikan kondisi heterogenitas data *smart city*,
implementasi menggunakan Distribusi Dirichlet. Parameter konsentrasi
$\alpha$ digunakan untuk mengontrol tingkat ketimpangan data antar
klien. Untuk mensimulasikan kondisi Non-IID maka nilai dari $\alpha$
adalah 0.3, sedangkan untuk mensimulasikan kondisi IID maka nilai dari
$\alpha$ adalah 5 untuk mendekati distribusi seimbang antara klient.

+----------------------------------------------------------------------+
| **def** split_data_non_iid(**X**, **y**, **n_clients=5**,            |
| **alpha=0.3**):                                                      |
|                                                                      |
|     *\# Dapatkan indeks untuk setiap kelas*                          |
|                                                                      |
|     n_classes **=** len(np.unique(y))                                |
|                                                                      |
|     client_indices **=** \[\[\] **for** \_ **in** range(n_clients)\] |
|                                                                      |
|                                                                      |
|                                                                      |
|     **for** k **in** range(n_classes):                               |
|                                                                      |
|         idx_k **=** np.where(y **==** k)\[**0**\]                    |
|                                                                      |
|         np.random.shuffle(idx_k)                                     |
|                                                                      |
|                                                                      |
|                                                                      |
|         *\# Generate proporsi menggunakan Dirichlet*                 |
|                                                                      |
|         proportions **=** np.random.dirichlet(np.repeat(alpha,       |
| n_clients))                                                          |
|                                                                      |
|                                                                      |
|                                                                      |
|         *\# Split indeks kelas k ke setiap klien berdasarkan         |
| proporsi*                                                            |
|                                                                      |
|         splits **=** np.split(idx_k,                                 |
| (np.cumsum(proportions)\[:**-1**\] **\*** len(idx_k)).astype(int))   |
|                                                                      |
|                                                                      |
|                                                                      |
|         **for** i **in** range(n_clients):                           |
|                                                                      |
|             client_indices\[i\].extend(splits\[i\])                  |
|                                                                      |
|                                                                      |
|                                                                      |
|     **return** client_indices                                        |
+======================================================================+

[]{#_Toc217653256 .anchor}Gambar 4.11 Pipeline *Dirichlet*

*\*
**Distribusi Data Binary per Klien**

[]{#_Ref217634890 .anchor}Tabel 4.6 Distribusi Binary (α=0.3 - Non-IID)

  ---------------------------------------------------------------------------
   **Client**    **Total    **Normal**   **Normal    **Attack**  **Attack %**
                Samples**                   %**                  
  ------------ ----------- ------------ ----------- ------------ ------------
    Client 1     56,382       34,004      60.30%       22,378       39.70%

    Client 2     102,976      5,332        5.20%       97,644       94.80%

    Client 3      1,419        252        17.80%       1,167        82.20%

  **Client 4**  **5,411**     **6**      **0.10%**   **5,405**    **99.90%**

    Client 5      2,646        406        15.30%       2,240        84.70%

     TOTAL       168,834      40,000        \-        128,834         \-
  ---------------------------------------------------------------------------

[]{#_Ref217634915 .anchor}Tabel 4.7 Distribusi Binary (α=5 - IID)

  -----------------------------------------------------------------------------
  **Client**        **Total   **Normal** **Normal %**   **Attack** **Attack %**
                  Samples**                                        
  ------------ ------------ ------------ ------------ ------------ ------------
  Client 1           18,363        9,011       49.10%        9,352       50.90%

  Client 2           52,347       12,919       24.70%       39,428       75.30%

  **Client 3**   **42,125**    **6,591**   **15.60%**   **35,534**   **84.40%**

  Client 4           34,395        6,444       18.70%       27,951       81.30%

  Client 5           21,604        5,035       23.30%       16,569       76.70%

  TOTAL             168,834       40,000           \-      128,834           \-
  -----------------------------------------------------------------------------

Tabel Tabel 4.6 dan Tabel 4.7 menyajikan distribusi data binary
classification (normal vs attack) pada masing-masing klien untuk dua
konfigurasi tingkat heterogenitas data, yaitu $\alpha\  = \ 0.3$
(Non-IID) dan $\alpha\  = \ 5.0$ (IID-like).

Pada skenario Non-IID $(\alpha\  = \ 0.3)$, terlihat bahwa distribusi
kelas antar klien sangat tidak seimbang. Beberapa klien didominasi
hampir sepenuhnya oleh data serangan, sementara klien lain memiliki
proporsi lalu lintas normal yang relatif lebih tinggi. Sebagai contoh,
Client 4 memiliki proporsi data serangan sebesar 99.9%, sedangkan Client
1 masih memiliki distribusi yang relatif lebih seimbang dengan 39.7%
data serangan. Rentang rasio serangan yang sangat lebar, yaitu 0.397
hingga 0.999, menunjukkan tingkat heterogenitas data yang ekstrem antar
klien.

Tingginya variasi distribusi ini tercermin dari nilai standar deviasi
rasio serangan sebesar 0.213, yang mengindikasikan kondisi Non-IID yang
kuat. Kondisi ini merepresentasikan skenario realistis pada lingkungan
IoT dan *smart city*, di mana setiap *gateway* atau *node* dapat
mengamati pola lalu lintas jaringan yang sangat berbeda bergantung pada
fungsi dan lokasi perangkat.

Sebaliknya, pada konfigurasi IID-like $(\alpha\  = \ 5.0)$ yang
ditunjukkan pada Tabel 4.7, distribusi kelas antar klien menjadi lebih
merata. Proporsi data serangan pada setiap klien berada dalam rentang
yang lebih sempit, yaitu 0.509 hingga 0.844, dengan standar deviasi yang
menurun menjadi 0.118. Penurunan variasi ini menunjukkan bahwa data
antar klien semakin mendekati asumsi IID, meskipun distribusi kelas
belum sepenuhnya identik.

**Distribusi Data Mutli-Class per Klien**

[]{#_Ref217634957 .anchor}Tabel 4.8 Distribusi Binary (α=0.3 - Non-IID)

  -----------------------------------------------------------------------------------------------------------------
    **Client**   **Total**    **0**    **1**    **2**    **3**   **4**    **5**    **6**    **7**    **8**    **9**
  ------------ ----------- -------- -------- -------- -------- ------- -------- -------- -------- -------- --------
      Client 1      44,505      706   11,118   11,248      375       3    2,269    5,881   10,061    1,833    1,011

      Client 2      61,553   14,638    2,720    2,398       65     610   35,991      151    2,647    1,725      608

      Client 3      26,032        0        0    1,105   12,547       2      748        1      769    7,370    3,490

      Client 4      12,697        7    1,832      158      165     208        0      281       24      862    9,160

      Client 5      24,047      649      330    1,091    2,848      11      992    9,686    2,499    4,210    1,731

         TOTAL     168,834   16,000   16,000   16,000   16,000     834   40,000   16,000   16,000   16,000   16,000
  -----------------------------------------------------------------------------------------------------------------

[]{#_Ref217634964 .anchor}Tabel 4.9 Distribusi Binary (α=5 - IID)

  -----------------------------------------------------------------------------------------------------------------
  **Client**     **Total**    **0**    **1**    **2**    **3**   **4**    **5**    **6**    **7**    **8**    **9**
  ------------ ----------- -------- -------- -------- -------- ------- -------- -------- -------- -------- --------
  Client 1          41,509    2,641    5,101    3,172    3,772     149   11,514    2,902    4,272    5,748    2,238

  Client 2          31,124    1,901    3,954    2,692    1,485     156    9,688    4,900    1,608    2,448    2,292

  Client 3          27,492    2,802    2,007    2,749    3,133     165    8,850    1,609    2,138    1,436    2,603

  Client 4          33,395    4,847    3,479    4,526    4,198      79    3,464    1,717    3,723    4,862    2,500

  Client 5          35,314    3,809    1,459    2,861    3,412     285    6,484    4,872    4,259    1,506    6,367

  TOTAL            168,834   16,000   16,000   16,000   16,000     834   40,000   16,000   16,000   16,000   16,000
  -----------------------------------------------------------------------------------------------------------------

Distribusi data untuk skenario *multi-class* classification ditampilkan
pada Tabel 4.8 (α = 0.3) dan Tabel 4.9 (α = 5.0). Dataset terdiri atas
sepuluh kelas, termasuk sembilan jenis serangan dan satu kelas normal.

Pada skenario Non-IID (α = 0.3), ketimpangan distribusi antar klien
terlihat jauh lebih kompleks dibandingkan kasus binary. Beberapa klien
hanya memiliki subset kelas tertentu, sementara kelas lain hampir tidak
muncul sama sekali. Sebagai contoh, Client 3 didominasi oleh kelas
*injection*, *scanning*, dan *xss*, dengan hampir tidak adanya kelas
*backdoor* dan i. Sementara itu, Client 2 memiliki dominasi kuat pada
kelas *normal* dan *backdoor*, tetapi sangat minim pada kelas *password*
dan *injection*.

Pola ini menunjukkan bahwa pada kondisi Non-IID, setiap klien tidak
hanya memiliki proporsi kelas yang berbeda, tetapi juga keragaman jenis
serangan yang sangat terbatas. Kondisi tersebut mencerminkan tantangan
utama *Federated Learning*, di mana model lokal dilatih pada distribusi
data yang sangat berbeda satu sama lain.

Pada konfigurasi IID-like (α = 5.0), distribusi kelas *multi-class*
antar klien menjadi jauh lebih seimbang. Setiap klien memiliki seluruh
kelas dengan proporsi yang relatif seragam, meskipun variasi kecil masih
dapat diamati. Tidak ada lagi klien yang hanya didominasi oleh satu atau
dua kelas tertentu, sehingga setiap model lokal memiliki cakupan
pengetahuan yang lebih luas terhadap berbagai jenis serangan.

**Perbandingan Tingkat Heterogenitas**

Tabel *binary dan multi-class* menyajikan ringkasan perbandingan tingkat
heterogenitas antara skenario Non-IID (α = 0.3) dan IID-like (α = 5.0).
Pada kasus binary, standar deviasi rasio serangan pada α = 0.3 tercatat
1.8 kali lebih tinggi dibandingkan α = 5.0. Perbedaan ini menjadi lebih
signifikan pada skenario *multi-class*, di mana rata-rata standar
deviasi distribusi kelas pada α = 0.3 mencapai sekitar 3.6 kali lebih
besar dibandingkan skenario IID-like.

Hasil ini mengonfirmasi bahwa heterogenitas data pada klasifikasi
*multi-class* bersifat lebih kompleks dan lebih menantang dibandingkan
binary classification. Dengan demikian, evaluasi performa model
Federated Learning pada kedua konfigurasi ini menjadi penting untuk
menilai kemampuan algoritma dalam menangani variasi distribusi data yang
ekstrem maupun mendekati IID.

#### Implementasi Federated Learning dengan Flower

Implementasi sistem FL menggunakan kelas NumPyClient dari Flower. Klien
menangani pelatihan lokal, sementara strategi server mengatur algoritma
agregasi.

**Klien Flower (Local Training)**

Klien menerima bobot global, melatih model pada data lokalnya, dan
mengembalikan bobot baru serta metrik evaluasi ke server.

+----------------------------------------------------------------------+
| **class** FlowerClient(fl.client.NumPyClient):                       |
|                                                                      |
|     **def** \_\_init\_\_(**self**, **model**, **X_train**,           |
| **y_train**, **X_val**, **y_val**, **batch_size**, **epochs**):      |
|                                                                      |
|         *self*.model **=** model                                     |
|                                                                      |
|         *self*.X_train, *self*.y_train **=** X_train, y_train        |
|                                                                      |
|         *self*.X_val, *self*.y_val **=** X_val, y_val                |
|                                                                      |
|         *self*.batch_size **=** batch_size                           |
|                                                                      |
|         *self*.epochs **=** epochs                                   |
|                                                                      |
|     **def** fit(**self**, **parameters**, **config**):               |
|                                                                      |
|         *self*.model.set_weights(parameters)                         |
|                                                                      |
|         history **=** *self*.model.fit(                              |
|                                                                      |
|             *self*.X_train, *self*.y_train,                          |
|                                                                      |
|             **epochs=***self*.epochs,                                |
|                                                                      |
|             **batch_size=***self*.batch_size,                        |
|                                                                      |
|             **verbose=0**                                            |
|                                                                      |
|         )                                                            |
|                                                                      |
|         **return** *self*.model.get_weights(), len(*self*.X_train),  |
| {\'loss\': history.history\[\'loss\'\]\[**-1**\]}                    |
|                                                                      |
|     **def** evaluate(**self**, **parameters**, **config**):          |
|                                                                      |
|         *self*.model.set_weights(parameters)                         |
|                                                                      |
|         loss, accuracy **=** *self*.model.evaluate(*self*.X_val,     |
| *self*.y_val, **verbose=0**)                                         |
|                                                                      |
|         **return** loss, len(*self*.X_val), {\"accuracy\": accuracy} |
+======================================================================+

[]{#_Toc217653257 .anchor}Gambar 4.12 Pipeline klient

**Algoritma Agregasi (Server)**

Penelitian ini mengimplementasikan dua strategi agregasi utama, yaitu
*Federated Averaging* (FedAvg) yang menggunakan rata-rata tertimbang
berdasarkan jumlah sampel data klien, serta *Federated Proximal*
(FedProx) yang menambahkan *proximal term* $(\mu)$ pada fungsi loss
klien untuk membatasi deviasi model lokal dari model global, sehingga
menjadi krusial dalam menangani data Non-IID.

+----------------------------------------------------------------------+
| *\# Contoh inisialisasi strategi FedAvg*                             |
|                                                                      |
| strategy **=** fl.server.strategy.FedAvg(                            |
|                                                                      |
|     **fraction_fit=1.0**,  *\# Semua klien berpartisipasi setiap     |
| round*                                                               |
|                                                                      |
|     **min_fit_clients=5**,                                           |
|                                                                      |
|     **min_available_clients=5**,                                     |
|                                                                      |
|     **eval_fn=**get_server_eval_fn() *\# Evaluasi global pada        |
| server*                                                              |
|                                                                      |
| )                                                                    |
|                                                                      |
| *\# Simulasi dijalankan dengan konfigurasi server*                   |
|                                                                      |
| fl.simulation.start_simulation(                                      |
|                                                                      |
|     **client_fn=**client_fn,                                         |
|                                                                      |
|     **num_clients=5**,                                               |
|                                                                      |
|     **config=**fl.server.ServerConfig(**num_rounds=20**),            |
|                                                                      |
|     **strategy=**strategy                                            |
|                                                                      |
| )                                                                    |
+======================================================================+

[]{#_Toc217653258 .anchor}Gambar 4.13 Contoh inisiasi server *Federated
Learning*

#### Simulasi Distribusi Data Non-IID

Untuk memastikan performa optimal dalam batasan sumber daya yang ada,
dilakukan *grid search* terbatas pada parameter kunci. Pencarian ini
bertujuan menemukan keseimbangan antara stabilitas konvergensi dan
efisiensi komputasi.

Ruang Pencarian Hyperparameter:

a.  Batch Size: \[*256, 512, 1024*\]

b.  Local Epochs: \[*1, 2*\]

c.  Learning Rate: \[*0.001, 0.0005*\]

d.  FedProx $\mu$: \[*0.01, 0.001*\] (khusus skenario FedProx)

Setiap kombinasi hyperparameter diuji pada skenario Non-IID
($\alpha = 0.3$) dan IID-like ($\alpha = 5$) untuk mengevaluasi
ketahanan model terhadap heterogenitas data.

**Hasil Grid Search pada Kondisi Non-IID (α = 0.3)**

[]{#_Ref217635064 .anchor}Tabel 4.10 Distribusi Binary (α=0.3 --
Non-IID)

  ------------------------------------------------------------------------------------------------------------------------------------
   **Batch   **E**     **LR**     **Model**    **Binary     **Binary     **Binary     **Multi    **Multi F1**   **Multi      **Train
   Size**                                       Acc**         F1**        AUC**        Acc**                     AUC**     Time (s)**
  --------- ------- ------------ ----------- ------------ ------------ ------------ ------------ ------------ ------------ -----------
     256       1       0.001         MLP        95.52%       97.14%       99.28%       71.11%       68.31%       96.43%       162.2

     256       1       0.001         CNN        95.73%       97.27%       99.18%       43.19%       32.99%       89.43%       436.9

     256       1       0.0005        MLP        95.00%       96.82%       99.33%       67.16%       63.49%       96.48%       162.2

     256       1       0.0005        CNN        95.72%       97.27%       99.67%       72.23%       69.73%       96.90%       426.4

     256       2       0.001         MLP        95.46%       97.10%       99.23%       69.36%       66.26%       97.84%       229.8

     256       2       0.001         CNN        88.91%       92.22%       99.09%       52.29%       45.81%       85.73%       660.3

     256       2       0.0005        MLP        95.61%       97.20%       99.35%       71.02%       68.25%       96.39%       228.1

     256       2       0.0005        CNN        95.74%       97.28%       99.75%       70.98%       66.26%       97.47%        639

     512       1       0.001         MLP        95.62%       97.21%       99.31%       67.23%       63.57%       96.20%        140

     512       1       0.001         CNN        95.60%       97.19%       99.57%       45.22%       36.25%       93.36%       445.7

   **512**   **1**   **0.0005**    **MLP**    **95.62%**   **97.20%**   **99.33%**   **66.77%**   **63.12%**   **95.84%**   **141.5**

   **512**   **1**   **0.0005**    **CNN**    **95.71%**   **97.26%**   **99.59%**   **73.27%**   **70.99%**   **97.64%**   **447.4**

     512       2       0.001         MLP        95.68%       97.24%       99.37%       71.18%       68.14%       97.56%       186.4

     512       2       0.001         CNN        86.44%       91.80%       92.39%       75.55%       73.47%       96.99%        683

     512       2       0.0005        MLP        95.62%       97.20%       99.43%       70.47%       66.73%       96.68%       190.2

     512       2       0.0005        CNN        90.48%       94.13%       96.42%       71.46%       66.68%       98.40%       691.7

    1024       1       0.001         MLP        95.55%       97.16%       99.26%       66.35%       62.06%       95.88%       129.3

    1024       1       0.001         CNN        95.53%       97.14%       99.45%       65.47%       59.41%       95.37%       454.2

    1024       1       0.0005        MLP        95.39%       97.06%       99.27%       68.34%       65.36%       95.37%       130.7

    1024       1       0.0005        CNN        95.73%       97.27%       99.60%       71.04%       68.14%       97.04%       458.9

    1024       2       0.001         MLP        95.53%       97.15%       99.35%       70.42%       67.20%       96.39%       172.8

    1024       2       0.001         CNN        95.78%       97.30%       99.71%       75.11%       72.96%       98.37%       704.8

    1024       2       0.0005        MLP        95.56%       97.17%       99.32%       67.62%       63.84%       96.32%       175.5

    1024       2       0.0005        CNN        95.80%       97.31%       99.74%       74.75%       73.17%       97.86%       711.2
  ------------------------------------------------------------------------------------------------------------------------------------

Hasil lengkap *grid search* pada kondisi Non-IID ekstrem (α = 0.3)
ditunjukkan pada Tabel 4.10. Secara umum, hasil eksperimen menunjukkan
bahwa binary classification relatif stabil pada hampir seluruh
konfigurasi, dengan nilai *accuracy* dan *AUC-ROC* yang konsisten tinggi
(di atas 95% dan mendekati 99%).

Sebaliknya, performa *multi-class* classification menunjukkan variasi
yang lebih signifikan antar konfigurasi. Hal ini mengindikasikan bahwa
klasifikasi *multi-class* pada kondisi Non-IID jauh lebih sensitif
terhadap pemilihan *hyperparameter*, terutama pada kombinasi *Batch
Size*, *Local Epochs*, dan arsitektur model.

Dari sisi arsitektur, model CNN cenderung menghasilkan performa
*multi-class* yang lebih tinggi dibandingkan MLP, namun dengan
konsekuensi waktu pelatihan yang lebih lama. Beberapa konfigurasi CNN
dengan Local Epochs = 2 menunjukkan peningkatan akurasi *multi-class*,
tetapi diiringi dengan peningkatan waktu training yang signifikan,
sehingga kurang efisien untuk skenario terdistribusi.

**Hasil Grid Search pada Kondisi IID (α = 5)**

[]{#_Ref217635093 .anchor}Tabel 4.11 Distribusi Binary (α=5 -- IID)

  ------------------------------------------------------------------------------------------------------------------------------------
   **Batch   **E**     **LR**     **Model**    **Binary     **Binary     **Binary     **Multi    **Multi F1**   **Multi      **Train
   Size**                                       Acc**         F1**        AUC**        Acc**                     AUC**     Time (s)**
  --------- ------- ------------ ----------- ------------ ------------ ------------ ------------ ------------ ------------ -----------
     256       1       0.001         MLP        95.63%       97.20%       99.36%       76.21%       75.08%       97.81%       160.6

     256       1       0.001         CNN        96.76%       97.85%       99.70%       60.57%       53.89%       91.04%       445.8

     256       1       0.0005        MLP        95.68%       97.24%       99.35%       73.45%       71.81%       97.63%        164

     256       1       0.0005        CNN        95.93%       97.39%       96.45%       78.07%       76.37%       98.04%       440.7

     256       2       0.001         MLP        96.62%       97.76%       99.54%       77.09%       76.37%       97.88%       209.7

     256       2       0.001         CNN        96.88%       97.92%       99.71%       61.90%       58.13%       92.31%       623.3

     256       2       0.0005        MLP        96.58%       97.74%       99.53%       77.95%       77.42%       98.08%       212.4

     256       2       0.0005        CNN        95.58%       97.17%       92.35%       57.47%       48.64%       89.82%        624

     512       1       0.001         MLP        95.67%       97.24%       99.37%       75.24%       74.28%       97.73%       150.2

     512       1       0.001         CNN        96.57%       97.72%       99.65%       59.67%       55.26%       94.23%        463

   **512**   **1**   **0.0005**    **MLP**    **95.68%**   **97.24%**   **99.35%**   **73.30%**   **72.28%**   **96.45%**   **142.8**

   **512**   **1**   **0.0005**    **CNN**    **96.67%**   **97.79%**   **99.62%**   **75.88%**   **74.61%**   **97.79%**   **457.3**

     512       2       0.001         MLP        96.61%       97.76%       99.59%       79.05%       78.46%       98.06%       181.5

     512       2       0.001         CNN        94.21%       96.08%       99.53%       40.25%       30.58%       71.32%        675

     512       2       0.0005        MLP        95.70%       97.25%       99.61%       78.27%       77.70%       98.00%       181.2

     512       2       0.0005        CNN        96.60%       97.74%       99.64%       77.13%       75.02%       97.69%       682.2

    1024       1       0.001         MLP        95.69%       97.25%       99.36%       71.19%       67.82%       95.99%       126.8

    1024       1       0.001         CNN        94.92%       96.58%       99.41%       56.81%       45.38%       93.36%       479.5

    1024       1       0.0005        MLP        95.69%       97.25%       99.29%       69.26%       64.73%       95.24%       126.9

    1024       1       0.0005        CNN        96.32%       97.55%       99.46%       61.15%       57.17%       93.94%       470.8

    1024       2       0.001         MLP        95.69%       97.24%       99.48%       77.79%       77.16%       98.01%       168.7

    1024       2       0.001         CNN        96.69%       97.81%       99.64%       80.05%       79.46%       98.25%       726.9

    1024       2       0.0005        MLP        95.70%       97.25%       99.42%       73.83%       73.12%       96.33%       168.3

    1024       2       0.0005        CNN        96.74%       97.84%       99.68%       74.05%       70.40%       97.58%       751.2
  ------------------------------------------------------------------------------------------------------------------------------------

Tabel 4.11 menyajikan hasil *grid search* pada kondisi IID-like (α =
5.0). Dibandingkan dengan skenario Non-IID, performa *multi-class*
classification pada kondisi ini meningkat secara konsisten di hampir
seluruh konfigurasi. Hal ini menunjukkan bahwa distribusi data yang
lebih homogen antar klien mempermudah proses konvergensi model global.

Model CNN kembali menunjukkan keunggulan pada task multi-class, dengan
beberapa konfigurasi mencapai akurasi di atas 80%. Namun demikian, pola
trade-off antara performa dan biaya komputasi tetap terlihat, di mana
peningkatan performa sering kali diiringi dengan waktu pelatihan yang
lebih panjang.

**Metode Seleksi Hyperparameter Optimal**

Pemilihan konfigurasi optimal tidak didasarkan pada satu metrik tunggal,
melainkan menggunakan pendekatan multi-kriteria. Setiap konfigurasi
dievaluasi berdasarkan lima metrik utama, yaitu Accuracy, Precision,
Recall, F1-Score, dan AUC-ROC, dengan bobot yang sama sebesar 20% untuk
masing-masing metrik.

Untuk memastikan keseimbangan performa antara task binary dan
multi-class, digunakan Balance Score yang didefinisikan sebagai:

  --------------------------------------------------------------------------------------------------------
  $$Balance\ Score\  = \frac{(WSbinary\  + \ WSmulti)}{2}\  - \ 0,1\  \times \ |Diff|$$   ( 4.1 )
  --------------------------------------------------------------------------------------- ----------------

  --------------------------------------------------------------------------------------------------------

Pendekatan ini bertujuan menghindari konfigurasi yang unggul pada satu
task namun lemah pada task lainnya, sekaligus mempertimbangkan perbedaan
performa antar task.

**Konfigurasi Terpilih**

Berdasarkan analisis Cost-Benefit dan prinsip Pareto Optimal,
konfigurasi terbaik pada kondisi Non-IID (α = 0.3) dipilih sebagai
berikut:

a.  Batch Size: \[*512*\]

b.  Local Epochs: \[*1*\]

c.  Learning Rate: \[*0.0005*\]

d.  FedProx $\mu$: \[*0.01, 0.001*\] (khusus skenario FedProx)

Konfigurasi ini memberikan Balance Score tertinggi dengan waktu
pelatihan yang relatif efisien, yaitu sekitar 447,4 detik (\~7,5 menit)
untuk CNN dan 141,5 detik (\~2,4 menit) untuk *MLP*.

Pada konfigurasi terpilih, performa binary classification mencapai
Accuracy 95.71%, F1-Score 97.26%, dan AUC-ROC 99.59%, menunjukkan
kemampuan deteksi serangan yang sangat baik. Sementara itu, pada
multi-class classification, model mencapai Accuracy 73.27%, F1-Score
70.99%, dan AUC-ROC 97.64%, meskipun dihadapkan pada ketimpangan kelas
yang signifikan, khususnya pada kelas *MITM* yang hanya memiliki 834
sampel.

### Analisis Federated Learning dari Eksperiment

Konfigurasi terpilih di atas menjadi landasan (*baseline*) yang
digunakan untuk seluruh skenario pengujian yang dibahas pada bagian
selanjutnya. Meskipun hasil awal menunjukkan performa yang menjanjikan,
evaluasi lebih lanjut sangat krusial untuk mengidentifikasi bagaimana
model merespons kompleksitas data jaringan yang bersifat heterogen.
Sub-bab berikut akan menguraikan analisis komparatif antara arsitektur
MLP dan CNN, serta menguji batas kemampuan algoritma FedAvg dan FedProx
dalam menjaga stabilitas model global. Fokus utama analisis ditekankan
pada kemampuan sistem mempertahankan deteksi serangan minoritas di
tengah kondisi data imbalance yang ekstrem. Pembahasan akan dimulai dari
gambaran performa secara umum menggunakan metrik global sebelum masuk ke
analisis mendalam pada level kelas serangan.

#### Gambaran Umum Hasil Eksperimen (Global Metrics)

Sub-bab ini menyajikan ringkasan performa global dari seluruh
konfigurasi eksperimen Federated Learning (FL) yang diuji, mencakup
variasi arsitektur model (MLP dan CNN), variasi distribusi data (IID dan
Non-IID), serta variasi algoritma agregasi (FedAvg dan FedProx) dengan
variasi parameter proximal (μ). Evaluasi global menggunakan metrik
Accuracy, Precision, Recall, F1-Score, dan AUC-ROC untuk menggambarkan
kualitas model secara agregat.

Secara umum, pada skenario IID performa klasifikasi biner cenderung
mencapai kondisi jenuh (ceiling effect) sehingga perbedaan antar
algoritma tidak terlalu menonjol. Sebaliknya, pada skenario multi-class,
perbedaan arsitektur dan algoritma lebih terlihat karena model perlu
membedakan pola serangan yang lebih beragam dan memiliki kemiripan fitur
antar kelas.

Ringkasan metrik global untuk skenario IID disajikan pada Tabel 4.12
menunjukkan bahwa konfigurasi CNN Multi-class dengan FedProx (μ=0.001)
memberikan performa terbaik pada IID (Accuracy 0.7861 dan F1-Score
0.7802), sedangkan tugas biner relatif setara pada seluruh algoritma.

[]{#_Ref217635177 .anchor}Tabel 4.12 Perbandingan Performa Algoritma
(Global Metrics) pada Skenario IID

  -----------------------------------------------------------------------------------------------
  **Model**   **Algoritma**   **Accuracy**   **Precision**   **Recall**   **F1      **AUC-ROC**
                                                                          Score**   
  ----------- --------------- -------------- --------------- ------------ --------- -------------
  MLP Binary  FedAvg          0.9569         0.9487          0.9974       0.9725    0.9929

  MLP Binary  FedProx         0.9569         0.9487          0.9974       0.9725    0.9933
              (μ=0.01)                                                              

  MLP Binary  FedProx         0.9569         0.9487          0.9974       0.9725    0.9931
              (μ=0.001)                                                             

  CNN Binary  FedAvg          0.9698         0.9916          0.9686       0.98      0.9968

  CNN Binary  FedProx         0.9687         0.9928          0.966        0.9792    0.9969
              (μ=0.01)                                                              

  CNN Binary  FedProx         0.966          0.9918          0.9634       0.9774    0.9962
              (μ=0.001)                                                             

  MLP Multi   FedAvg          0.7111         0.7462          0.7111       0.6757    0.9582

  MLP Multi   FedProx         0.7027         0.7292          0.7027       0.6816    0.9647
              (μ=0.01)                                                              

  MLP Multi   FedProx         0.7036         0.7389          0.7036       0.6815    0.9745
              (μ=0.001)                                                             

  CNN Multi   FedAvg          0.7778         0.8018          0.7778       0.7664    0.985

  CNN Multi   FedProx         0.7718         0.8083          0.7718       0.7649    0.9815
              (μ=0.01)                                                              

  CNN Multi   FedProx         0.7861         0.8192          0.7861       0.7802    0.9817
              (μ=0.001)                                                             
  -----------------------------------------------------------------------------------------------

Analisis per kelas pada skenario IID untuk konfigurasi CNN Multi-class
dirangkum pada Tabel 4.13menunjukkan bahwa peningkatan terbesar pada
kelas DoS terjadi saat menggunakan FedProx (μ=0.01), sementara performa
Injection justru terbaik pada FedProx (μ=0.001). Hal ini menegaskan
bahwa dampak regularisasi dapat berbeda antar kelas.

[]{#_Ref217635204 .anchor}Tabel 4.13 Detail Per Kelas (F1-Score) untuk
CNN Multi-class pada Skenario IID

  ----------------------------------------------------------------------
     **Kelas       **FedAvg      **FedProx     **FedProx      **Tren
    Serangan**      (F1)**       (μ=0.01)      (μ=0.001)     Terbaik**
                                  (F1)**        (F1)**     
  -------------- ------------- ------------- ------------- -------------
     Backdoor        0.63          0.65          0.63         FedProx
                                                              μ=0.01

       DDoS          0.94          0.94          0.94         Stabil

       DoS           0.25          0.37          0.34      FedProx (naik
                                                            signifikan)

    Injection        0.77          0.64          0.79         FedProx
                                                              μ=0.001

       MITM          0.26          0.19           0.1      FedAvg (sulit
                                                            dideteksi)

      Normal         0.92          0.93          0.93         FedProx

     Password        0.73          0.66          0.72         FedAvg

    Ransomware       0.76          0.79          0.79         FedProx

     Scanning         0.8          0.81           0.8         FedProx
                                                              μ=0.01

       XSS           0.88          0.88          0.88         Stabil
  ----------------------------------------------------------------------

Dari sisi efisiensi, Tabel 4.14menyajikan perbandingan waktu pelatihan
pada skenario IID. Tabel 4.14 memperlihatkan bahwa FedProx menambah
overhead waktu dibanding FedAvg karena komputasi proximal term. Pada
IID, overhead ini tidak selalu sebanding untuk tugas biner (karena
performa sudah jenuh), tetapi dapat dipertimbangkan pada CNN Multi-class
ketika terjadi peningkatan kinerja sebagaimana pada Tabel 4.12.

[]{#_Ref217635233 .anchor}Tabel 4.14 Efisiensi Waktu Pelatihan (Training
Cost) pada Skenario IID

  --------------------------------------------------------------------------
  **Algoritma**   **Model**     **Waktu Total **Rata-rata   **Keterangan**
                                (detik)**     per Round     
                                              (detik)**     
  --------------- ------------- ------------- ------------- ----------------
  FedAvg          MLP Binary    62.93         3.11          Tercepat

  FedAvg          CNN Binary    160.82        7.97          \-

  FedAvg          MLP Multi     88.37         4.37          \-

  FedAvg          CNN Multi     305.22        15.1          \-

  FedProx         MLP Binary    87.38         4.3           Lebih lambat
  (μ=0.01)                                                  \~38% vs FedAvg

  FedProx         CNN Binary    185.51        9.17          Lebih lambat
  (μ=0.01)                                                  \~15% vs FedAvg

  FedProx         MLP Multi     115.19        5.67          \-
  (μ=0.01)                                                  

  FedProx         CNN Multi     327.97        16.2          \-
  (μ=0.01)                                                  

  FedProx         MLP Binary    86.39         4.25          Mirip μ=0.01
  (μ=0.001)                                                 

  FedProx         CNN Binary    185.18        9.14          \-
  (μ=0.001)                                                 

  FedProx         MLP Multi     118.68        5.85          \-
  (μ=0.001)                                                 

  FedProx         CNN Multi     330.25        16.31         \-
  (μ=0.001)                                                 
  --------------------------------------------------------------------------

#### Analisis Performa Arsitektur Model: MLP vs CNN (Skenario Baseline)

Skenario baseline pada pembahasan ini didefinisikan sebagai FedAvg
dengan distribusi data IID, karena kondisi tersebut merepresentasikan
situasi ideal ketika data antar klien relatif seragam dan algoritma
agregasi standar umumnya sudah memadai. Analisis baseline berfokus pada
pengaruh arsitektur model terhadap kemampuan deteksi intrusi.

Berdasarkan Tabel 4.12 baris FedAvg), CNN menunjukkan keunggulan
konsisten dibanding MLP, terutama pada tugas multi-class. CNN
Multi-class mencapai Accuracy 0.7778 dan F1-Score 0.7664, lebih tinggi
daripada MLP Multi-class (Accuracy 0.7111 dan F1-Score 0.6757). Temuan
ini mengindikasikan bahwa CNN lebih efektif mengekstraksi fitur
diskriminatif untuk membedakan berbagai kelas serangan.

![](media/image11.png){width="3.935999562554681in"
height="3.483305993000875in"}

[]{#_Ref217635364 .anchor}Gambar 4.14 Confusion Matrix FedAvg pada
Skenario IID (MLP Binary, CNN Binary, MLP Multi-class, CNN Multi-class)

Pada Gambar 4.14 Confusion Matrix FedAvg pada Skenario IID (MLP Binary,
CNN Binary, MLP Multi-class, CNN Multi-class), klasifikasi biner
memperlihatkan perbedaan karakter keputusan model: MLP cenderung lebih
agresif mendeteksi serangan (False Negative kecil) namun menghasilkan
False Positive lebih tinggi sehingga meningkatkan potensi false alarm.
Sebaliknya, CNN biner lebih seimbang karena lebih baik mengidentifikasi
trafik normal. Pada multi-class, CNN menunjukkan prediksi kelas Normal
yang lebih bersih dan peningkatan akurasi pada kelas tertentu misalnya
XSS dan Scanning. Meskipun masih terdapat kebingungan konsisten antara
DoS dan Backdoor.

#### Dampak Heterogenitas Data: IID vs Non-IID

Heterogenitas data merupakan tantangan utama dalam FL karena distribusi
kelas pada tiap klien dapat berbeda. Pada skenario IID, update lokal
cenderung memiliki arah yang selaras sehingga model global stabil. Pada
skenario Non-IID (Dirichlet α=0.3), sebagian klien dapat didominasi oleh
kelas tertentu sehingga update lokal dapat saling bertabrakan dan model
global berisiko bias terhadap kelas mayoritas.

Penurunan performa akibat heterogenitas terlihat jelas pada tugas
multi-class. Perbandingan metrik global Non-IID ditunjukkan pada Tabel
4.15. Pada CNN Multi-class, FedAvg turun dari Accuracy 0.7778 (Tabel
4.12 Perbandingan Performa Algoritma (Global Metrics) pada Skenario IID)
menjadi 0.6918 (Non-IID; Tabel 4.15), yang mengindikasikan degradasi
kemampuan generalisasi ketika distribusi data antar klien timpang.

[]{#_Ref217635680 .anchor}Tabel 4.15 Perbandingan Performa Algoritma
(Global Metrics) pada Skenario Non-IID (Dirichlet α=0.3)

  -----------------------------------------------------------------------------------------------
  **Model**   **Algoritma**   **Accuracy**   **Precision**   **Recall**   **F1      **AUC-ROC**
                                                                          Score**   
  ----------- --------------- -------------- --------------- ------------ --------- -------------
  MLP Binary  FedAvg          0.9562         0.9474          0.998        0.972     0.9927

  MLP Binary  FedProx         0.9561         0.9474          0.9978       0.972     0.9934
              (μ=0.01)                                                              

  MLP Binary  FedProx         0.9562         0.9474          0.998        0.972     0.9932
              (μ=0.001)                                                             

  CNN Binary  FedAvg          0.9571         0.949           0.9974       0.9726    0.9961

  CNN Binary  FedProx         0.9574         0.9486          0.9982       0.9728    0.996
              (μ=0.01)                                                              

  CNN Binary  FedProx         0.9578         0.9491          0.9983       0.9731    0.9959
              (μ=0.001)                                                             

  MLP Multi   FedAvg          0.6695         0.683           0.6695       0.6323    0.9604

  MLP Multi   FedProx         0.6976         0.7353          0.6976       0.671     0.9614
              (μ=0.01)                                                              

  MLP Multi   FedProx         0.6686         0.6868          0.6686       0.6317    0.9578
              (μ=0.001)                                                             

  CNN Multi   FedAvg          0.6918         0.7923          0.6918       0.6554    0.9742

  CNN Multi   FedProx         0.7304         0.7724          0.7304       0.7143    0.9734
              (μ=0.01)                                                              

  CNN Multi   FedProx         0.6937         0.7924          0.6937       0.6547    0.976
              (μ=0.001)                                                             
  -----------------------------------------------------------------------------------------------

![](media/image12.png){width="5.377770122484689in"
height="4.755814741907262in"}

[]{#_Toc217653260 .anchor}Gambar 4.15 Confusion Matrix FedAvg pada
Skenario Non-IID (MLP Binary, CNN Binary, MLP Multi-class, CNN
Multi-class)

Gambar 4.15 menunjukkan bahwa klasifikasi biner tetap relatif robust
pada Non-IID karena hanya memisahkan dua kelas. Namun, pada multi-class
terjadi kegagalan lebih serius: kelas Backdoor hampir tidak terdeteksi
mendekati 0%, serta kebingungan kuat antara Injection dan Password.
Fenomena ini konsisten dengan client drift dan catastrophic forgetting,
yaitu pengetahuan kelas minoritas/langka tertimpa oleh update dari klien
yang tidak memiliki kelas tersebut.

#### Analisis Efektivitas Algoritma: FedAvg vs FedProx

FedAvg merupakan metode agregasi standar yang menghitung rata-rata bobot
dari klien. Pada kondisi IID, FedAvg cenderung stabil karena update
klien relatif homogen. Akan tetapi, pada Non-IID, FedAvg rentan bias
terhadap klien mayoritas sehingga pengetahuan kelas minoritas dapat
tenggelam. FedProx memperbaiki hal tersebut dengan menambahkan proximal
term (μ) yang membatasi penyimpangan model lokal terhadap model global,
sehingga menekan client drift.

Efektivitas FedProx pada Non-IID tercermin pada Tabel 4.15, khususnya
CNN Multi-class: FedProx (μ=0.01) meningkatkan Accuracy dari 0.6918
(FedAvg) menjadi 0.7304 dan F1-Score dari 0.6554 menjadi 0.7143. Bukti
per kelas pada Tabel 4.16 menunjukkan bahwa peningkatan ini terutama
berasal dari pemulihan kelas minoritas seperti Backdoor dan perbaikan
Injection.

[]{#_Ref217635632 .anchor}Tabel 4.16 Detail Per Kelas (F1-Score) untuk
CNN Multi-class pada Skenario Non-IID (Dirichlet α=0.3)

  ------------------------------------------------------------------------
  **Kelas       **FedAvg      **FedProx     **FedProx     **Keterangan**
  Serangan**    (F1)**        (μ=0.01)      (μ=0.001)     
                              (F1)**        (F1)**        
  ------------- ------------- ------------- ------------- ----------------
  Backdoor      0.0           0.65          0.01          Peningkatan
                                                          masif pada
                                                          μ=0.01

  DDoS          0.92          0.91          0.92          Stabil

  DoS           0.53          0.3           0.54          FedAvg/μ=0.001
                                                          sedikit lebih
                                                          baik

  Injection     0.18          0.38          0.15          μ=0.01 membaik

  MITM          0.14          0.22          0.3           Sulit dideteksi

  Normal        0.9           0.9           0.89          Stabil

  Password      0.57          0.62          0.58          μ=0.01 membaik

  Ransomware    0.8           0.78          0.8           Stabil

  Scanning      0.8           0.8           0.8           Stabil

  XSS           0.86          0.84          0.87          Stabil
  ------------------------------------------------------------------------

![](media/image13.png){width="5.209302274715661in"
height="4.606830708661417in"}

[]{#_Ref217635527 .anchor}Gambar 4.16 Confusion Matrix FedProx (μ=0.01)
pada Skenario Non-IID

Pada Gambar 4.16 Confusion Matrix FedProx (μ=0.01) pada Skenario
Non-IID, FedProx (μ=0.01) memperlihatkan pemulihan deteksi Backdoor yang
sebelumnya hampir hilang pada FedAvg Non-IID. Meski terdapat efek
samping berupa kebingungan terbalik antara DoS dan Backdoor, konfigurasi
ini lebih aman untuk IDS karena lebih baik salah mengklasifikasikan tipe
serangan dibanding gagal mendeteksi serangan langka sama sekali
(Bierbrauer dkk., 2025b).

![](media/image14.png){width="5.290697725284339in"
height="4.678812335958005in"}

[]{#_Ref217635551 .anchor}Gambar 4.17 Confusion Matrix FedProx (μ=0.001)
pada Skenario Non-IID

Gambar 4.17 Confusion Matrix FedProx (μ=0.001) pada Skenario
Non-IIDmenunjukkan bahwa FedProx (μ=0.001) tidak cukup kuat pada Non-IID
berat. Pola misklasifikasi kembali mirip FedAvg, khususnya kegagalan
mendeteksi kelas minoritas seperti Backdoor dan rendahnya performa
Injection. Hal ini memperkuat argumen bahwa pada distribusi data sangat
heterogen, diperlukan μ lebih besar untuk menahan drift model lokal.

Dari sisi biaya komputasi pada Non-IID, Tabel 4.17 menunjukkan bahwa
FedProx menambah overhead waktu dibanding FedAvg. Namun, pada konteks
Non-IID overhead ini dapat dipertimbangkan sebagai investasi, karena
peningkatan performa multi-class (khususnya pada CNN Multi-class)
bersifat substantif sebagaimana terlihat pada Tabel 4.15 dan Tabel 4.16.

[]{#_Ref217635607 .anchor}Tabel 4.17 Efisiensi Waktu Pelatihan (Training
Cost) pada Skenario Non-IID

  -----------------------------------------------------------------------
  **Algoritma**   **Model**     **Waktu Total **Rata-rata   **Overhead vs
                                (detik)**     per Round     FedAvg**
                                              (detik)**     
  --------------- ------------- ------------- ------------- -------------
  FedAvg          MLP Binary    63.17         3.12          \-

  FedAvg          CNN Binary    151.44        7.51          \-

  FedAvg          MLP Multi     87.43         4.32          \-

  FedAvg          CNN Multi     304.76        15.08         \-

  FedProx         MLP Binary    89.42         4.4           +41%
  (μ=0.01)                                                  

  FedProx         CNN Binary    179.92        8.87          +18%
  (μ=0.01)                                                  

  FedProx         MLP Multi     108.77        5.35          +24%
  (μ=0.01)                                                  

  FedProx         CNN Multi     333.27        16.46         +9%
  (μ=0.01)                                                  

  FedProx         MLP Binary    89.35         4.39          +41%
  (μ=0.001)                                                 

  FedProx         CNN Binary    179.98        8.87          +18%
  (μ=0.001)                                                 

  FedProx         MLP Multi     111.97        5.51          +28%
  (μ=0.001)                                                 

  FedProx         CNN Multi     325.66        16.08         +6%
  (μ=0.001)                                                 
  -----------------------------------------------------------------------

#### Analisis Sensitivitas Parameter Proximal $\mathbf{\mu}$

Analisis sensitivitas parameter proximal $(\mu)$ menjelaskan bagaimana
kekuatan regularisasi FedProx memengaruhi stabilitas dan fleksibilitas
pembelajaran. Secara intuitif, $\mu$ berperan sebagai *redline* antara
model lokal dan model global: $\mu$ kecil memberi fleksibilitas lebih
besar pada pembelajaran lokal, sedangkan $\mu$ besar menahan update
lokal agar tidak terlalu menyimpang.

Rangkuman perilaku $\mu$ pada dua kondisi distribusi data disajikan pada
*Tabel 4.18* menegaskan bahwa pemilihan $\mu$ bersifat kontekstual: μ
kecil cenderung cocok untuk IID karena menghindari over-regularization,
sementara $\mu$ lebih besar diperlukan pada Non-IID untuk menahan client
drift dan memulihkan kelas minoritas.

[]{#_Ref217635723 .anchor}*Tabel 4.18 Perilaku FedProx terhadap Variasi
Parameter Proximal (μ) pada Skenario IID dan Non-IID*

  ----------------------------------------------------------------------
  **Skenario Data**      **Perilaku μ Kecil     **Perilaku μ
                         (0.001)**              Sedang/Besar (0.01)**
  ---------------------- ---------------------- ------------------------
  IID (Seragam)          Efektif sebagai        Berpotensi terlalu kaku
                         regularisasi ringan;   (over-regularization);
                         membantu generalisasi  pada beberapa kelas
                         tanpa menghambat       dapat menurunkan
                         pembelajaran fitur     performa karena model
                         lokal yang relevan.    lokal dipaksa terlalu
                         Hasil optimal terlihat mirip global, padahal
                         pada CNN Multi-class.  data lokal sudah
                                                representatif.

  Non-IID (Timpang)      Gagal/terlalu lemah    Sangat efektif; mampu
                         (too weak); penalti    menahan client drift
                         kecil sehingga model   serta memulihkan
                         lokal tetap divergen   pembelajaran kelas
                         mengikuti bias data    minoritas/langka
                         lokal, menghasilkan    (misalnya Backdoor) yang
                         performa mirip FedAvg. hilang pada FedAvg.
  ----------------------------------------------------------------------

![](media/image15.png){width="5.127946194225721in"
height="4.534884076990376in"}

[]{#_Ref217635768 .anchor}Gambar 4.18 Confusion Matrix FedProx (μ=0.01)
pada Skenario IID

Berdasarkan Gambar 4.18 Confusion Matrix FedProx (μ=0.01) pada Skenario
IID, pada data IID penggunaan μ=0.01 cenderung menghasilkan regularisasi
yang terlalu kuat untuk sebagian kelas multi-class. Dampaknya, beberapa
kelas (misalnya DoS) dapat membaik, namun kelas Injection cenderung
menurun karena model menjadi kurang fleksibel dalam mempelajari
pemisahan fitur yang halus.

![](media/image16.png){width="5.167390638670166in"
height="4.569767060367454in"}

[]{#_Toc217653264 .anchor}Gambar 4.19 Confusion Matrix FedProx (μ=0.001)
pada Skenario IID

Gambar 4.14 menunjukkan bahwa μ=0.001 pada IID menjadi titik
keseimbangan (sweet spot) karena regularisasi ringan mampu meningkatkan
generalisasi tanpa menghambat pembelajaran. Hal ini konsisten dengan
Tabel 4.12 (CNN Multi-class mencapai Accuracy 0.7861) dan Tabel 4.13
yang menunjukkan pemulihan performa Injection.

### Dokumentasi Hasil Penelitian

Seluruh kode sumber dan artefak penelitian ini didokumentasikan
menggunakan sistem *version control* pada platform GitHub. Hal ini
bertujuan untuk menjamin transparansi, memudahkan penelusuran riwayat
pengembangan, serta mendukung reprodusibilitas hasil eksperimen.
Dokumentasi teknis beserta panduan penggunaan lengkap dapat diakses
melalui tautan berikut: <https://github.com/elnoersan/Paper> .

## BAB V Kesimpulan

### Kesimpulan

Berdasarkan hasil eksperimen yang telah dilakukan, dapat disimpulkan
bahwa karakteristik lalu lintas jaringan pada lingkungan *smart city*
yang bersifat heterogen menyebabkan distribusi data antar *gateway*
cenderung Non-IID. Kondisi ini berdampak langsung pada performa sistem
*Network Intrusion Detection System* (NIDS) *berbasis Federated
Learning*, terutama pada skenario klasifikasi *multi-class* yang
melibatkan kelas serangan langka. Temuan ini menunjukkan bahwa evaluasi
performa tidak dapat hanya mengandalkan metrik agregat global, tetapi
perlu mempertimbangkan perilaku model terhadap distribusi data yang
tidak merata antar klien.

Hasil perbandingan algoritma menunjukkan bahwa *Federated Averaging*
(FedAvg) memiliki performa yang stabil dan efisien pada tugas deteksi
biner, baik pada kondisi IID maupun Non-IID. Namun, pada skenario
multi-class dengan heterogenitas data yang tinggi (α=0.3), FedAvg
cenderung mengalami degradasi performa yang signifikan pada beberapa
kelas minoritas, seperti *backdoor* dan *mitm*, yang pada beberapa
konfigurasi tidak berhasil dipelajari sama sekali. Hal ini
mengindikasikan bahwa pendekatan agregasi standar berpotensi mengabaikan
informasi penting yang hanya muncul pada sebagian kecil klien.

Penerapan *Federated Proximal* (FedProx) dengan parameter $\mu = 0.01$
menunjukkan kemampuan yang lebih baik dalam menjaga stabilitas
pembelajaran pada kondisi Non-IID. Secara khusus, FedProx mampu
memulihkan performa pada kelas serangan yang sebelumnya gagal dipelajari
oleh FedAvg, meskipun dengan konsekuensi peningkatan waktu pelatihan.
Temuan ini menegaskan bahwa mekanisme regularisasi proximal efektif
dalam mengurangi client drift, terutama ketika distribusi data antar
klien sangat tidak seimbang.

Dari sisi arsitektur model, CNN 1D secara konsisten menunjukkan performa
yang lebih baik dibandingkan MLP pada tugas klasifikasi *multi-class*,
terutama dalam menangkap pola kompleks pada lalu lintas jaringan. Namun
demikian, peningkatan performa tersebut disertai dengan beban komputasi
yang lebih tinggi, sehingga pemilihan model perlu disesuaikan dengan
keterbatasan sumber daya pada perangkat *edge*. Untuk kebutuhan deteksi
biner yang lebih sederhana, MLP dengan FedAvg tetap menjadi alternatif
yang rasional karena efisiensi dan kestabilannya.

Secara keseluruhan, hasil penelitian ini menunjukkan bahwa tidak
terdapat satu konfigurasi tunggal yang optimal untuk seluruh skenario
Smart City. Pemilihan algoritma Federated Learning dan arsitektur model
perlu mempertimbangkan tingkat heterogenitas data, kebutuhan
granularitas deteksi, serta keterbatasan komputasi pada perangkat..

### Saran

Penelitian ini masih dilakukan dalam bentuk simulasi terkontrol dengan
dataset statis dan lingkungan eksperimen terbatas. Oleh karena itu,
pengembangan selanjutnya diperlukan untuk mendekatkan skenario
eksperimen dengan kondisi operasional sistem nyata. Pengujian pada
lingkungan yang lebih dinamis dan kompleks diharapkan dapat memberikan
gambaran yang lebih realistis mengenai stabilitas dan keterbatasan
sistem Federated Learning. Selain itu, pendekatan evaluasi yang lebih
beragam dapat membantu mengidentifikasi potensi risiko dan kegagalan
sistem sejak tahap awal.

- Penelitian selanjutnya disarankan mengimplementasikan Federated
  Learning menggunakan *framework* seperti **Flower** pada lingkungan
  berbasis *container*, misalnya Docker. Agar simulasi komunikasi
  klien--server lebih mendekati kondisi nyata serta mudah direplikasi.

- Evaluasi lanjutan dapat difokuskan pada **ketahanan sistem** melalui
  pengujian beban, seperti peningkatan trafik secara tiba-tiba, trafik
  burst, distribusi input yang sangat tidak seimbang antar klien, serta
  kondisi keterbatasan sumber daya (CPU dan memori).

- Penggunaan **data sintetis** dan **alat test penetrasi keamanan**
  untuk mensimulasikan anomali atau serangan langka dapat
  dipertimbangkan guna menguji stabilitas model di luar skenario dataset
  yang bersifat statis.

Hasil penelitian ini memberikan gambaran awal mengenai perilaku
algoritma *Federated Learning* pada kondisi data heterogen dan homogen.
Namun, penerapan pada lingkungan nyata memerlukan penyesuaian terhadap
skala jaringan, karakteristik perangkat, serta ketersediaan
infrastruktur pendukung. Oleh karena itu, hasil penelitian sebaiknya
diposisikan sebagai panduan awal, bukan sebagai solusi final yang
langsung dapat digeneralisasi. Pertimbangan praktis di lapangan tetap
menjadi faktor penting dalam pengambilan keputusan implementasi.

- Rekomendasi konfigurasi hasil penelitian ini berpotensi diterapkan
  pada **skala wilayah kecil**, seperti kecamatan, distrik, kampung,
  atau kota kecil, dengan catatan tersedia infrastruktur jaringan dan
  komputasi yang memadai.

- Pada lingkungan **heterogen (Non-IID)** yang membutuhkan klasifikasi
  serangan secara detail, kombinasi **FedProx (μ=0.01) dengan CNN**
  lebih disarankan karena lebih stabil dalam menangani ketimpangan
  distribusi data.

- Untuk kebutuhan **deteksi biner** atau lingkungan dengan keterbatasan
  sumber daya, **FedAvg dengan MLP** dapat menjadi alternatif yang lebih
  efisien dan ringan.

- Apabila sistem diarahkan ke **perangkat edge dengan sumber daya sangat
  terbatas** (misalnya MCU), perlu dipertimbangkan pemilihan pendekatan
  Federated Learning (horizontal, vertikal, atau hibrida) serta
  penerapan teknik optimisasi model seperti **quantization**.

## DAFTAR PUSTAKA

Abdel-Basset, M., Hawash, H., Moustafa, N., Razzak, I., & Abd Elfattah,
M. (2024). Privacy-preserved learning from non-i.i.d data in
fog-assisted IoT: A federated learning approach. *Digital Communications
and Networks*, *10*(2), 404--415.
https://doi.org/10.1016/j.dcan.2022.12.013

Ahmad, Z., Shahid Khan, A., Wai Shiang, C., Abdullah, J., & Ahmad, F.
(2021). Network intrusion detection system: A systematic study of
machine learning and deep learning approaches. *Transactions on Emerging
Telecommunications Technologies*, *32*(1).
https://doi.org/10.1002/ett.4150

Ahmadi, K., & Javidan, R. (2023). DDoS Attack Detection in a Real Urban
IoT Environment Using Federated Deep Learning. *Proceedings of the 2023
IEEE International Conference on Cyber Security and Resilience, CSR
2023*, 117--122. https://doi.org/10.1109/CSR57506.2023.10224916

Al-Ghadi, T. Q., Manickam, S., Widia, I. D. M., Wulandari, E. R. N., &
Karuppayah, S. (2025). Leveraging federated learning for DoS attack
detection in IoT networks based on ensemble feature selection and deep
learning models. *Cyber Security and Applications*, *3*, 100098.
https://doi.org/10.1016/j.csa.2025.100098

Al-Huthaifi, R., Li, T., Huang, W., Gu, J., & Li, C. (2023). Federated
learning in smart cities: Privacy and security survey. *Information
Sciences*, *632*, 833--857. https://doi.org/10.1016/j.ins.2023.03.033

Ali, A., Assam, M., Khan, F. U., Ghadi, Y. Y., Nurdaulet, Z., Zhibek,
A., Shah, S. Y., & Alahmadi, T. J. (2024). An optimized multilayer
perceptron-based network intrusion detection using Gray Wolf
Optimization. *Computers and Electrical Engineering*, *120*, 109838.
https://doi.org/10.1016/j.compeleceng.2024.109838

Alsaedi, A., Moustafa, N., Tari, Z., Mahmood, A., & Anwar, A. (2020).
TON_IoT Telemetry Dataset: A New Generation Dataset of IoT and IIoT for
Data-Driven Intrusion Detection Systems. *IEEE Access*, *8*,
165130--165150. https://doi.org/10.1109/ACCESS.2020.3022862

Barker, L., & Brooks, A. (2023). *IDC FutureScape IDC FutureScape:
Worldwide Smart Cities and Communities 2024 Predictions*.
https://www.idc.com/wp-content/uploads/2025/03/IDC_FutureScape_Worldwide_Smart_Cities_and_Communities_2024_Predictions\_-\_2023_Oct.pdf

Bierbrauer, D. A., Coffey, S. M., Willeke, M. R., Beggs, J. D., &
Bastian, N. D. (2025a). Data-efficient Federated Learning for Edge
Network Intrusion Detection. *Engineering Applications of Artificial
Intelligence*, *150*, 110685.
https://doi.org/10.1016/j.engappai.2025.110685

Bierbrauer, D. A., Coffey, S. M., Willeke, M. R., Beggs, J. D., &
Bastian, N. D. (2025b). Data-efficient Federated Learning for Edge
Network Intrusion Detection. *Engineering Applications of Artificial
Intelligence*, *150*, 110685.
https://doi.org/10.1016/j.engappai.2025.110685

Bodagala, H., & Priyanka, H. (2022). Security for IoT using Federated
Learning. *Proceedings - 2022 International Conference on Recent Trends
in Microelectronics, Automation, Computing and Communications Systems,
ICMACC 2022*, 131--136.
https://doi.org/10.1109/ICMACC54824.2022.10093557

Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. (2002). A fast and
elitist multiobjective genetic algorithm: NSGA-II. *IEEE Transactions on
Evolutionary Computation*, *6*(2), 182--197.
https://doi.org/10.1109/4235.996017

Feng, Y., & Sakurai, K. (2025). *Network Intrusion Detection: Evolution
from Conventional Approaches to LLM Collaboration and Emerging Risks*.
http://arxiv.org/abs/2510.23313

Ferrag, M. A., Maglaras, L., Moschoyiannis, S., & Janicke, H. (2020).
Deep learning for cyber security intrusion detection: Approaches,
datasets, and comparative study. *Journal of Information Security and
Applications*, *50*, 102419. https://doi.org/10.1016/j.jisa.2019.102419

Frightera, F. (2023). *Reproducibility in Keras Models*.
https://keras.io/examples/keras_recipes/reproducibility_recipes/

Hijazi, N. M., Aloqaily, M., Guizani, M., Ouni, B., & Karray, F. (2024).
Secure Federated Learning with Fully Homomorphic Encryption for IoT
Communications. *IEEE Internet of Things Journal*, *11*(3), 4289--4300.
https://doi.org/10.1109/JIOT.2023.3302065

Javeed, D., Saeed, M. S., Adil, M., Kumar, P., & Jolfaei, A. (2024). A
federated learning-based zero trust intrusion detection system for
Internet of Things. *Ad Hoc Networks*, *162*, 103540.
https://doi.org/10.1016/j.adhoc.2024.103540

Kunang, Y. N., Nurmaini, S., Stiawan, D., & Suprapto, B. Y. (2021a).
Attack classification of an intrusion detection system using deep
learning and hyperparameter optimization. *Journal of Information
Security and Applications*, *58*, 102804.
https://doi.org/10.1016/j.jisa.2021.102804

Kunang, Y. N., Nurmaini, S., Stiawan, D., & Suprapto, B. Y. (2021b).
Attack classification of an intrusion detection system using deep
learning and hyperparameter optimization. *Journal of Information
Security and Applications*, *58*, 102804.
https://doi.org/10.1016/j.jisa.2021.102804

LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature*,
*521*(7553), 436--444. https://doi.org/10.1038/nature14539

Li, T., Sahu, A. K., Zaheer, M., Sanjabi, M., Talwalkar, A., & Smith, V.
(2020). *FEDERATED OPTIMIZATION IN HETEROGENEOUS NETWORKS*.

McMahan, H. B., Moore, E., Ramage, D., Hampson, S., & Arcas, B. A. y.
(2023). *Communication-Efficient Learning of Deep Networks from
Decentralized Data*. http://arxiv.org/abs/1602.05629

Morgan, S. (2025, Desember 11). *2025 Cybersecurity Almanac: 100 Facts,
Figures, Predictions And Statistics*. Cybercrime Magazine.

Moustafa, N. (2021). A new distributed architecture for evaluating
AI-based security systems at the edge: Network TON_IoT datasets.
*Sustainable Cities and Society*, *72*, 102994.
https://doi.org/10.1016/j.scs.2021.102994

Olanrewaju-George, B., & Pranggono, B. (2025). Federated learning-based
intrusion detection system for the internet of things using unsupervised
and supervised deep learning models. *Cyber Security and Applications*,
*3*. https://doi.org/10.1016/j.csa.2024.100068

Panahi, M., Roumanjani, F., & Ranjbar, V. (t.t.). *Machine
Learning-Based Intrusion Detection Systems for IoT Security: A Survey*.

Qazi, E.-H., Imran, M., Haider, N., Shoaib, M., & Razzak, I. (2022a). An
intelligent and efficient network intrusion detection system using deep
learning. *Computers and Electrical Engineering*, *99*, 107764.
https://doi.org/10.1016/j.compeleceng.2022.107764

Qazi, E.-H., Imran, M., Haider, N., Shoaib, M., & Razzak, I. (2022b). An
intelligent and efficient network intrusion detection system using deep
learning. *Computers and Electrical Engineering*, *99*, 107764.
https://doi.org/10.1016/j.compeleceng.2022.107764

Schröer, C., Kruse, F., & Gómez, J. M. (2021). A Systematic Literature
Review on Applying CRISP-DM Process Model. *Procedia Computer Science*,
*181*, 526--534. https://doi.org/10.1016/j.procs.2021.01.199

Statista Research Department. (2025, Desember 1). *Number of internet
and social media users worldwide as of October 2025*. Statista Research
Department.
https://www.statista.com/statistics/617136/digital-population-worldwide/#:\~:text=Number%20of%20internet%20and%20social%20media%20users%20worldwide%202025&text=As%20of%20October%202025%2C%206.04,population%2C%20were%20social%20media%20users.

Thakur, A., Tyagi, R., Tripathy, H. K., Yang, T., Rathore, R. S., Mo,
D., & Wang, L. (2024). Detecting Network Attack using Federated Learning
for IoT Devices. *2024 International Conference on Intelligent
Algorithms for Computational Intelligence Systems (IACIS)*, 1--6.
https://doi.org/10.1109/IACIS61494.2024.10721980

Thantharate, P., & T, A. (2023). CYBRIA - Pioneering Federated Learning
for Privacy-Aware Cybersecurity with Brilliance. *2023 IEEE 20th
International Conference on Smart Communities: Improving Quality of Life
using AI, Robotics and IoT (HONET)*, 56--61.
https://doi.org/10.1109/HONET59747.2023.10374608

Tiwari, A. (2022). Supervised learning: From theory to applications.
Dalam *Artificial Intelligence and Machine Learning for EDGE Computing*
(hlm. 23--32). Elsevier.
https://doi.org/10.1016/B978-0-12-824054-0.00026-5

Upreti, D., Yang, E., Kim, H., & Seo, C. (2024). A Comprehensive Survey
on Federated Learning in the Healthcare Area: Concept and Applications.
*Computer Modeling in Engineering & Sciences*, *140*(3), 2239--2274.
https://doi.org/10.32604/cmes.2024.048932

Zhu, H., Xu, J., Liu, S., & Jin, Y. (2021). *Federated Learning on
Non-IID Data: A Survey*. http://arxiv.org/abs/2106.06843

 

**\**

## LAMPIRAN
