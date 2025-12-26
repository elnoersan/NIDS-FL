"""
Exploratory Data Analysis (EDA) untuk TON_IoT Network Dataset
===============================================================
Script ini melakukan analisis mendalam terhadap dataset TON_IoT TANPA melakukan
pembersihan data. Tujuannya adalah untuk memahami karakteristik data mentah
sebelum memutuskan strategi preprocessing yang tepat.

Berdasarkan paper: TON_IoT Network Dataset
Author: Nour Moustafa, UNSW Canberra
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from collections import Counter
import time

warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class TONIoTExplorer:
    """
    Class untuk melakukan EDA komprehensif pada TON_IoT dataset
    tanpa melakukan cleaning/preprocessing
    """
    
    def __init__(self, filepath):
        """
        Initialize dengan memuat data mentah
        """
        print("="*70)
        print("TON_IoT Network Dataset - Exploratory Data Analysis")
        print("="*70)
        print("\n🔍 Memuat dataset mentah (tanpa modifikasi)...\n")
        
        start_time = time.time()
        self.df_raw = pd.read_csv(filepath, low_memory=False)
        self.df_raw.columns = self.df_raw.columns.str.strip()
        
        load_time = time.time() - start_time
        print(f"✅ Dataset berhasil dimuat dalam {load_time:.2f} detik")
        print(f"📊 Shape: {self.df_raw.shape[0]:,} baris × {self.df_raw.shape[1]} kolom\n")
        
    def basic_info(self):
        """
        Menampilkan informasi dasar dataset
        """
        print("\n" + "="*70)
        print("1️⃣  INFORMASI DASAR DATASET")
        print("="*70)
        
        print("\n📋 Tipe Data Kolom:")
        print("-" * 70)
        dtype_counts = self.df_raw.dtypes.value_counts()
        for dtype, count in dtype_counts.items():
            print(f"  • {dtype}: {count} kolom")
        
        print("\n📏 Ukuran Memory:")
        print("-" * 70)
        memory_usage = self.df_raw.memory_usage(deep=True).sum() / 1024**2
        print(f"  • Total: {memory_usage:.2f} MB")
        
        print("\n🔢 Statistik Dasar:")
        print("-" * 70)
        print(f"  • Total Records: {len(self.df_raw):,}")
        print(f"  • Total Columns: {len(self.df_raw.columns)}")
        print(f"  • Duplicate Rows: {self.df_raw.duplicated().sum():,}")
        
        print("\n📝 Sample Data (5 baris pertama):")
        print("-" * 70)
        print(self.df_raw.head())
        
    def analyze_target_distribution(self):
        """
        Analisis distribusi label dan type (target variables)
        """
        print("\n" + "="*70)
        print("2️⃣  ANALISIS TARGET VARIABLES (Label & Type)")
        print("="*70)
        
        # Label Distribution (Binary: Normal vs Attack)
        if 'label' in self.df_raw.columns:
            print("\n🎯 Distribusi LABEL (Binary Classification):")
            print("-" * 70)
            label_counts = self.df_raw['label'].value_counts()
            label_pct = self.df_raw['label'].value_counts(normalize=True) * 100
            
            for label, count in label_counts.items():
                pct = label_pct[label]
                label_name = "Normal" if label == 0 else "Attack"
                print(f"  • {label_name} ({label}): {count:,} ({pct:.2f}%)")
            
            # Imbalance Ratio
            if len(label_counts) == 2:
                ratio = max(label_counts) / min(label_counts)
                print(f"\n  ⚠️  Imbalance Ratio: {ratio:.2f}:1")
                if ratio > 10:
                    print(f"      (Highly Imbalanced! Pertimbangkan sampling techniques)")
        
        # Type Distribution (Multi-class: Attack Types)
        if 'type' in self.df_raw.columns:
            print("\n\n🎯 Distribusi TYPE (Multi-class Classification):")
            print("-" * 70)
            type_counts = self.df_raw['type'].value_counts()
            type_pct = self.df_raw['type'].value_counts(normalize=True) * 100
            
            print(f"{'Attack Type':<20} {'Count':>12} {'Percentage':>12}")
            print("-" * 70)
            for attack_type, count in type_counts.items():
                pct = type_pct[attack_type]
                print(f"{str(attack_type):<20} {count:>12,} {pct:>11.2f}%")
            
            # Visualisasi
            plt.figure(figsize=(14, 6))
            
            # Plot 1: Bar chart
            plt.subplot(1, 2, 1)
            type_counts.plot(kind='bar', color='skyblue', edgecolor='black')
            plt.title('Distribusi Attack Types', fontsize=14, fontweight='bold')
            plt.xlabel('Attack Type', fontsize=11)
            plt.ylabel('Count', fontsize=11)
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', alpha=0.3)
            
            # Plot 2: Pie chart
            plt.subplot(1, 2, 2)
            colors = plt.cm.Set3(range(len(type_counts)))
            plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%',
                   colors=colors, startangle=90)
            plt.title('Proporsi Attack Types', fontsize=14, fontweight='bold')
            
            plt.tight_layout()
            plt.savefig('toniot_target_distribution.png', dpi=300, bbox_inches='tight')
            print("\n  📊 Visualisasi disimpan: 'toniot_target_distribution.png'")
            plt.close()
    
    def analyze_missing_values(self):
        """
        Analisis komprehensif missing values dan placeholder '-'
        """
        print("\n" + "="*70)
        print("3️⃣  ANALISIS MISSING VALUES & PLACEHOLDER")
        print("="*70)
        
        # Count actual NaN
        null_counts = self.df_raw.isnull().sum()
        null_pct = (null_counts / len(self.df_raw)) * 100
        
        # Count placeholder '-'
        dash_counts = (self.df_raw == '-').sum()
        dash_pct = (dash_counts / len(self.df_raw)) * 100
        
        # Total missing (NaN + '-')
        total_missing = null_counts + dash_counts
        total_missing_pct = (total_missing / len(self.df_raw)) * 100
        
        # Filter kolom dengan missing values
        missing_df = pd.DataFrame({
            'Column': self.df_raw.columns,
            'NaN_Count': null_counts.values,
            'NaN_Pct': null_pct.values,
            'Dash_Count': dash_counts.values,
            'Dash_Pct': dash_pct.values,
            'Total_Missing': total_missing.values,
            'Total_Missing_Pct': total_missing_pct.values
        })
        
        missing_df = missing_df[missing_df['Total_Missing'] > 0].sort_values(
            'Total_Missing_Pct', ascending=False
        )
        
        if len(missing_df) > 0:
            print("\n📊 Kolom dengan Missing Values (diurutkan dari tertinggi):")
            print("-" * 70)
            print(f"{'Column':<25} {'NaN%':>8} {'Dash%':>8} {'Total%':>8} {'Count':>10}")
            print("-" * 70)
            
            for _, row in missing_df.head(20).iterrows():
                print(f"{row['Column']:<25} {row['NaN_Pct']:>7.2f}% "
                      f"{row['Dash_Pct']:>7.2f}% {row['Total_Missing_Pct']:>7.2f}% "
                      f"{int(row['Total_Missing']):>10,}")
            
            if len(missing_df) > 20:
                print(f"\n  ... dan {len(missing_df) - 20} kolom lainnya")
            
            # Summary statistics
            print("\n\n📈 Ringkasan Missing Values:")
            print("-" * 70)
            print(f"  • Kolom dengan missing: {len(missing_df)} dari {len(self.df_raw.columns)}")
            print(f"  • Kolom dengan >50% missing: {(missing_df['Total_Missing_Pct'] > 50).sum()}")
            print(f"  • Kolom dengan >90% missing: {(missing_df['Total_Missing_Pct'] > 90).sum()}")
            
            # Visualisasi
            if len(missing_df) > 0:
                top_missing = missing_df.head(15)
                
                plt.figure(figsize=(12, 6))
                x = range(len(top_missing))
                width = 0.35
                
                plt.bar([i - width/2 for i in x], top_missing['NaN_Pct'], 
                       width, label='NaN', color='#ff6b6b', edgecolor='black')
                plt.bar([i + width/2 for i in x], top_missing['Dash_Pct'], 
                       width, label="Placeholder '-'", color='#4ecdc4', edgecolor='black')
                
                plt.xlabel('Kolom', fontsize=11, fontweight='bold')
                plt.ylabel('Persentase Missing (%)', fontsize=11, fontweight='bold')
                plt.title('Top 15 Kolom dengan Missing Values', 
                         fontsize=14, fontweight='bold')
                plt.xticks(x, top_missing['Column'], rotation=45, ha='right')
                plt.legend()
                plt.grid(axis='y', alpha=0.3)
                plt.tight_layout()
                plt.savefig('toniot_missing_values.png', dpi=300, bbox_inches='tight')
                print("\n  📊 Visualisasi disimpan: 'toniot_missing_values.png'")
                plt.close()
        else:
            print("\n✅ Tidak ada missing values dalam dataset!")
    
    def analyze_protocol_specific_features(self):
        """
        Analisis fitur yang spesifik untuk protokol tertentu
        (DNS, HTTP, SSL) - ini yang PENTING untuk TON_IoT!
        """
        print("\n" + "="*70)
        print("4️⃣  ANALISIS PROTOCOL-SPECIFIC FEATURES")
        print("="*70)
        print("\n⚠️  Catatan: Missing values pada protocol-specific features")
        print("    seringkali BUKAN data hilang, tapi 'not applicable'!")
        
        # Identifikasi protokol
        if 'proto' in self.df_raw.columns:
            print("\n\n🔌 Distribusi Protokol Transport Layer:")
            print("-" * 70)
            proto_counts = self.df_raw['proto'].value_counts()
            proto_pct = self.df_raw['proto'].value_counts(normalize=True) * 100
            
            for proto, count in proto_counts.items():
                pct = proto_pct[proto]
                print(f"  • {proto}: {count:,} ({pct:.2f}%)")
        
        if 'service' in self.df_raw.columns:
            print("\n\n🌐 Distribusi Services (Application Layer):")
            print("-" * 70)
            service_counts = self.df_raw['service'].value_counts().head(15)
            service_pct = self.df_raw['service'].value_counts(normalize=True).head(15) * 100
            
            print(f"{'Service':<20} {'Count':>12} {'Percentage':>12}")
            print("-" * 70)
            for service, count in service_counts.items():
                pct = service_pct[service]
                print(f"{str(service):<20} {count:>12,} {pct:>11.2f}%")
        
        # DNS Features Analysis
        dns_cols = ['dns_query', 'dns_qclass', 'dns_qtype', 'dns_rcode', 
                    'dns_AA', 'dns_RD', 'dns_RA', 'dns_rejected']
        dns_available = [col for col in dns_cols if col in self.df_raw.columns]
        
        if dns_available:
            print("\n\n🔍 DNS Features Analysis:")
            print("-" * 70)
            
            # Hitung records dengan data DNS
            dns_present = self.df_raw[dns_available[0]].notna().sum()
            dns_pct = (dns_present / len(self.df_raw)) * 100
            
            print(f"  • Records dengan DNS data: {dns_present:,} ({dns_pct:.2f}%)")
            print(f"  • Records tanpa DNS data: {len(self.df_raw) - dns_present:,} "
                  f"({100-dns_pct:.2f}%)")
            print(f"\n  💡 Insight: {100-dns_pct:.2f}% records TIDAK menggunakan DNS")
            print(f"     → Missing values pada DNS features adalah NORMAL!")
        
        # HTTP Features Analysis
        http_cols = ['http_method', 'http_uri', 'http_version', 'http_trans_depth',
                     'http_request_body_len', 'http_response_body_len', 
                     'http_status_code', 'http_user_agent']
        http_available = [col for col in http_cols if col in self.df_raw.columns]
        
        if http_available:
            print("\n\n🌐 HTTP Features Analysis:")
            print("-" * 70)
            
            http_present = self.df_raw[http_available[0]].notna().sum()
            http_pct = (http_present / len(self.df_raw)) * 100
            
            print(f"  • Records dengan HTTP data: {http_present:,} ({http_pct:.2f}%)")
            print(f"  • Records tanpa HTTP data: {len(self.df_raw) - http_present:,} "
                  f"({100-http_pct:.2f}%)")
            print(f"\n  💡 Insight: {100-http_pct:.2f}% records TIDAK menggunakan HTTP")
            print(f"     → Missing values pada HTTP features adalah NORMAL!")
            
            if 'http_method' in self.df_raw.columns:
                print("\n  📊 HTTP Methods yang digunakan:")
                http_methods = self.df_raw['http_method'].value_counts().head(10)
                for method, count in http_methods.items():
                    print(f"     • {method}: {count:,}")
        
        # SSL Features Analysis
        ssl_cols = ['ssl_version', 'ssl_cipher', 'ssl_resumed', 
                    'ssl_established', 'ssl_subject', 'ssl_issuer']
        ssl_available = [col for col in ssl_cols if col in self.df_raw.columns]
        
        if ssl_available:
            print("\n\n🔐 SSL/TLS Features Analysis:")
            print("-" * 70)
            
            ssl_present = self.df_raw[ssl_available[0]].notna().sum()
            ssl_pct = (ssl_present / len(self.df_raw)) * 100
            
            print(f"  • Records dengan SSL data: {ssl_present:,} ({ssl_pct:.2f}%)")
            print(f"  • Records tanpa SSL data: {len(self.df_raw) - ssl_present:,} "
                  f"({100-ssl_pct:.2f}%)")
            print(f"\n  💡 Insight: {100-ssl_pct:.2f}% records TIDAK menggunakan SSL")
            print(f"     → Missing values pada SSL features adalah NORMAL!")
    
    def analyze_numerical_features(self):
        """
        Analisis statistik deskriptif untuk fitur numerik
        """
        print("\n" + "="*70)
        print("5️⃣  ANALISIS NUMERICAL FEATURES")
        print("="*70)
        
        # Identifikasi kolom numerik
        numeric_cols = self.df_raw.select_dtypes(include=[np.number]).columns.tolist()
        
        # Exclude label columns
        numeric_cols = [col for col in numeric_cols if col not in ['label']]
        
        if len(numeric_cols) > 0:
            print(f"\n📊 Ditemukan {len(numeric_cols)} kolom numerik")
            print("-" * 70)
            
            # Connection-level numerics (yang selalu ada)
            connection_numerics = ['duration', 'src_bytes', 'dst_bytes', 
                                  'missed_bytes', 'src_pkts', 'dst_pkts',
                                  'src_ip_bytes', 'dst_ip_bytes', 
                                  'src_port', 'dst_port']
            
            available_connection = [col for col in connection_numerics 
                                   if col in numeric_cols]
            
            if available_connection:
                print("\n🔗 Connection-Level Features:")
                print("-" * 70)
                
                stats_df = self.df_raw[available_connection].describe().T
                stats_df['zeros'] = (self.df_raw[available_connection] == 0).sum()
                stats_df['zeros_pct'] = (stats_df['zeros'] / len(self.df_raw)) * 100
                
                print(f"{'Feature':<20} {'Mean':>12} {'Std':>12} {'Min':>12} "
                      f"{'Max':>12} {'Zeros%':>10}")
                print("-" * 70)
                
                for idx, row in stats_df.iterrows():
                    print(f"{idx:<20} {row['mean']:>12.2f} {row['std']:>12.2f} "
                          f"{row['min']:>12.2f} {row['max']:>12.2f} "
                          f"{row['zeros_pct']:>9.2f}%")
                
                # Deteksi outliers menggunakan IQR
                print("\n\n🚨 Deteksi Outliers (IQR Method):")
                print("-" * 70)
                
                for col in available_connection[:5]:  # Top 5 saja
                    Q1 = self.df_raw[col].quantile(0.25)
                    Q3 = self.df_raw[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    
                    outliers = ((self.df_raw[col] < lower_bound) | 
                               (self.df_raw[col] > upper_bound)).sum()
                    outliers_pct = (outliers / len(self.df_raw)) * 100
                    
                    print(f"  • {col}: {outliers:,} outliers ({outliers_pct:.2f}%)")
                
                # Visualisasi distribusi
                fig, axes = plt.subplots(2, 3, figsize=(15, 10))
                axes = axes.flatten()
                
                for idx, col in enumerate(available_connection[:6]):
                    # Remove zeros untuk visualisasi yang lebih baik
                    data = self.df_raw[self.df_raw[col] > 0][col]
                    
                    if len(data) > 0:
                        axes[idx].hist(data, bins=50, color='steelblue', 
                                      edgecolor='black', alpha=0.7)
                        axes[idx].set_title(f'{col} Distribution\n(excluding zeros)', 
                                          fontsize=10, fontweight='bold')
                        axes[idx].set_xlabel('Value', fontsize=9)
                        axes[idx].set_ylabel('Frequency', fontsize=9)
                        axes[idx].grid(axis='y', alpha=0.3)
                    else:
                        axes[idx].text(0.5, 0.5, 'No non-zero data', 
                                      ha='center', va='center')
                        axes[idx].set_title(col, fontsize=10)
                
                plt.tight_layout()
                plt.savefig('toniot_numerical_distributions.png', 
                           dpi=300, bbox_inches='tight')
                print("\n  📊 Visualisasi disimpan: 'toniot_numerical_distributions.png'")
                plt.close()
        
        else:
            print("\n⚠️  Tidak ada kolom numerik yang ditemukan!")
    
    def analyze_categorical_features(self):
        """
        Analisis fitur kategorikal
        """
        print("\n" + "="*70)
        print("6️⃣  ANALISIS CATEGORICAL FEATURES")
        print("="*70)
        
        categorical_cols = self.df_raw.select_dtypes(include=['object']).columns.tolist()
        
        # Exclude target dan IP addresses
        exclude_cols = ['label', 'type', 'src_ip', 'dst_ip']
        categorical_cols = [col for col in categorical_cols if col not in exclude_cols]
        
        if len(categorical_cols) > 0:
            print(f"\n📊 Ditemukan {len(categorical_cols)} kolom kategorikal")
            print("-" * 70)
            
            # Analyze key categorical features
            key_categoricals = ['proto', 'service', 'conn_state']
            available_categoricals = [col for col in key_categoricals 
                                     if col in categorical_cols]
            
            for col in available_categoricals:
                print(f"\n🔤 Feature: {col}")
                print("-" * 70)
                
                value_counts = self.df_raw[col].value_counts()
                unique_count = self.df_raw[col].nunique()
                
                print(f"  • Unique values: {unique_count}")
                print(f"  • Most common values:")
                
                for val, count in value_counts.head(10).items():
                    pct = (count / len(self.df_raw)) * 100
                    print(f"     - {val}: {count:,} ({pct:.2f}%)")
                
                if unique_count > 10:
                    print(f"     ... dan {unique_count - 10} nilai lainnya")
            
            # Cardinality check
            print("\n\n📈 Cardinality Analysis:")
            print("-" * 70)
            print(f"{'Feature':<25} {'Unique Values':>15} {'Cardinality':>15}")
            print("-" * 70)
            
            for col in categorical_cols[:15]:
                unique_count = self.df_raw[col].nunique()
                cardinality = "Low" if unique_count < 10 else \
                             "Medium" if unique_count < 50 else "High"
                print(f"{col:<25} {unique_count:>15,} {cardinality:>15}")
            
        else:
            print("\n⚠️  Tidak ada kolom kategorikal yang ditemukan!")
    
    def analyze_correlations(self):
        """
        Analisis korelasi antar fitur numerik
        """
        print("\n" + "="*70)
        print("7️⃣  ANALISIS KORELASI FITUR NUMERIK")
        print("="*70)
        
        numeric_cols = self.df_raw.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(numeric_cols) > 2:
            # Pilih fitur penting untuk korelasi
            key_features = ['src_bytes', 'dst_bytes', 'src_pkts', 'dst_pkts',
                           'duration', 'src_port', 'dst_port', 'label']
            
            available_features = [col for col in key_features 
                                 if col in numeric_cols]
            
            if len(available_features) > 2:
                print(f"\n📊 Menghitung korelasi untuk {len(available_features)} fitur...")
                
                corr_matrix = self.df_raw[available_features].corr()
                
                # Find highly correlated pairs
                print("\n🔗 Highly Correlated Features (|r| > 0.7):")
                print("-" * 70)
                
                found_high_corr = False
                for i in range(len(corr_matrix.columns)):
                    for j in range(i+1, len(corr_matrix.columns)):
                        corr_val = corr_matrix.iloc[i, j]
                        if abs(corr_val) > 0.7:
                            col1 = corr_matrix.columns[i]
                            col2 = corr_matrix.columns[j]
                            print(f"  • {col1} ↔ {col2}: {corr_val:.3f}")
                            found_high_corr = True
                
                if not found_high_corr:
                    print("  ✅ Tidak ada korelasi tinggi yang ditemukan")
                
                # Heatmap
                plt.figure(figsize=(12, 10))
                mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
                sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f',
                           cmap='coolwarm', center=0, square=True,
                           linewidths=1, cbar_kws={"shrink": 0.8})
                plt.title('Correlation Heatmap - Key Features', 
                         fontsize=14, fontweight='bold', pad=20)
                plt.tight_layout()
                plt.savefig('toniot_correlation_heatmap.png', 
                           dpi=300, bbox_inches='tight')
                print("\n  📊 Visualisasi disimpan: 'toniot_correlation_heatmap.png'")
                plt.close()
        else:
            print("\n⚠️  Tidak cukup kolom numerik untuk analisis korelasi")
    
    def analyze_attack_patterns(self):
        """
        Analisis pola serangan per type
        """
        print("\n" + "="*70)
        print("8️⃣  ANALISIS POLA SERANGAN PER TYPE")
        print("="*70)
        
        if 'type' not in self.df_raw.columns:
            print("\n⚠️  Kolom 'type' tidak ditemukan!")
            return
        
        attack_types = self.df_raw['type'].unique()
        
        # Analisis per attack type
        key_features = ['src_bytes', 'dst_bytes', 'duration', 'src_pkts', 'dst_pkts']
        available_features = [col for col in key_features if col in self.df_raw.columns]
        
        if available_features:
            print(f"\n📊 Statistik per Attack Type (Top 5 fitur):")
            print("-" * 70)
            
            for attack in list(attack_types)[:10]:  # Top 10 attack types
                print(f"\n🎯 {attack}:")
                attack_data = self.df_raw[self.df_raw['type'] == attack]
                
                print(f"  • Sample size: {len(attack_data):,}")
                
                for feature in available_features[:3]:
                    mean_val = attack_data[feature].mean()
                    median_val = attack_data[feature].median()
                    print(f"  • {feature}: mean={mean_val:.2f}, median={median_val:.2f}")
    
    def generate_summary_report(self):
        """
        Generate ringkasan lengkap dari semua analisis
        """
        print("\n" + "="*70)
        print("📋 RINGKASAN LENGKAP EDA")
        print("="*70)
        
        print("\n1️⃣  Dataset Overview:")
        print(f"   • Shape: {self.df_raw.shape}")
        print(f"   • Memory: {self.df_raw.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        print(f"   • Duplicates: {self.df_raw.duplicated().sum():,}")
        
        print("\n2️⃣  Data Types:")
        for dtype, count in self.df_raw.dtypes.value_counts().items():
            print(f"   • {dtype}: {count} columns")
        
        print("\n3️⃣  Missing Values:")
        total_missing = (self.df_raw.isnull().sum() + (self.df_raw == '-').sum()).sum()
        total_cells = self.df_raw.shape[0] * self.df_raw.shape[1]
        missing_pct = (total_missing / total_cells) * 100
        print(f"   • Total missing cells: {total_missing:,} ({missing_pct:.2f}%)")
        
        if 'type' in self.df_raw.columns:
            print("\n4️⃣  Attack Distribution:")
            for attack, count in self.df_raw['type'].value_counts().head(5).items():
                pct = (count / len(self.df_raw)) * 100
                print(f"   • {attack}: {count:,} ({pct:.2f}%)")
        
        print("\n" + "="*70)
        print("✅ EDA SELESAI - Review data sebelum preprocessing!")
        print("="*70)
        
        print("\n🔖 Simpan hasil EDA ini untuk referensi di masa mendatang.\n")

