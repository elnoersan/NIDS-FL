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
from IPython.display import display, HTML, Markdown
from io import StringIO

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
        self.markdown_report = []
        
        print("="*70)
        print("TON_IoT Network Dataset - Exploratory Data Analysis")
        print("="*70)
        print("\nMemuat dataset mentah (tanpa modifikasi)...\n")
        
        start_time = time.time()
        self.df_raw = pd.read_csv(filepath, low_memory=False)
        self.df_raw.columns = self.df_raw.columns.str.strip()
        
        load_time = time.time() - start_time
        print(f"Dataset berhasil dimuat dalam {load_time:.2f} detik")
        print(f"Shape: {self.df_raw.shape[0]:,} baris x {self.df_raw.shape[1]} kolom\n")
        
        # Add to markdown report
        self.markdown_report.append("# TON_IoT Network Dataset - EDA Report\n")
        self.markdown_report.append(f"**Dataset Shape**: {self.df_raw.shape[0]:,} rows x {self.df_raw.shape[1]} columns\n")
        self.markdown_report.append(f"**Load Time**: {load_time:.2f} seconds\n\n")
        
    def basic_info(self):
        """
        Menampilkan informasi dasar dataset
        """
        display(HTML("<h2>1. INFORMASI DASAR DATASET</h2>"))
        
        # Data types
        dtype_counts = self.df_raw.dtypes.value_counts()
        dtype_df = pd.DataFrame({
            'Data Type': dtype_counts.index.astype(str),
            'Count': dtype_counts.values
        })
        
        display(HTML("<h3>Tipe Data Kolom</h3>"))
        display(dtype_df)
        
        # Memory usage
        memory_usage = self.df_raw.memory_usage(deep=True).sum() / 1024**2
        
        # Statistics
        stats_df = pd.DataFrame({
            'Metric': ['Total Records', 'Total Columns', 'Duplicate Rows', 'Memory Usage (MB)'],
            'Value': [
                f"{len(self.df_raw):,}",
                f"{len(self.df_raw.columns)}",
                f"{self.df_raw.duplicated().sum():,}",
                f"{memory_usage:.2f}"
            ]
        })
        
        display(HTML("<h3>Statistik Dasar</h3>"))
        display(stats_df)
        
        # Sample data
        display(HTML("<h3>Sample Data (5 baris pertama)</h3>"))
        display(self.df_raw.head())
        
        # Markdown report
        self.markdown_report.append("## 1. Basic Information\n\n")
        self.markdown_report.append("### Data Types\n")
        self.markdown_report.append(dtype_df.to_markdown(index=False))
        self.markdown_report.append("\n\n### Statistics\n")
        self.markdown_report.append(stats_df.to_markdown(index=False))
        self.markdown_report.append("\n\n")
        
    def analyze_target_distribution(self):
        """
        Analisis distribusi label dan type (target variables)
        """
        display(HTML("<h2>2. ANALISIS TARGET VARIABLES (Label & Type)</h2>"))
        
        # Label Distribution
        if 'label' in self.df_raw.columns:
            display(HTML("<h3>Distribusi LABEL (Binary Classification)</h3>"))
            
            label_counts = self.df_raw['label'].value_counts()
            label_pct = self.df_raw['label'].value_counts(normalize=True) * 100
            
            label_df = pd.DataFrame({
                'Label': ['Normal' if x == 0 else 'Attack' for x in label_counts.index],
                'Count': label_counts.values,
                'Percentage': [f"{x:.2f}%" for x in label_pct.values]
            })
            
            display(label_df)
            
            # Imbalance ratio
            if len(label_counts) == 2:
                ratio = max(label_counts) / min(label_counts)
                display(HTML(f"<p><b>Imbalance Ratio:</b> {ratio:.2f}:1</p>"))
                if ratio > 10:
                    display(HTML("<p style='color:orange;'><b>WARNING:</b> Highly Imbalanced! Consider sampling techniques</p>"))
        
        # Type Distribution
        if 'type' in self.df_raw.columns:
            display(HTML("<h3>Distribusi TYPE (Multi-class Classification)</h3>"))
            
            type_counts = self.df_raw['type'].value_counts()
            type_pct = self.df_raw['type'].value_counts(normalize=True) * 100
            
            type_df = pd.DataFrame({
                'Attack Type': type_counts.index,
                'Count': type_counts.values,
                'Percentage': [f"{x:.2f}%" for x in type_pct.values]
            })
            
            display(type_df)
            
            # Visualisasi
            fig, axes = plt.subplots(2, 2, figsize=(16, 12))
            
            # Plot 1: Bar chart
            ax1 = axes[0, 0]
            type_counts.plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')
            ax1.set_title('Distribusi Attack Types (Bar Chart)', fontsize=14, fontweight='bold')
            ax1.set_xlabel('Attack Type', fontsize=11)
            ax1.set_ylabel('Count', fontsize=11)
            ax1.tick_params(axis='x', rotation=45)
            ax1.grid(axis='y', alpha=0.3)
            
            # Plot 2: Pie chart
            ax2 = axes[0, 1]
            colors = plt.cm.Set3(range(len(type_counts)))
            ax2.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%',
                   colors=colors, startangle=90)
            ax2.set_title('Proporsi Attack Types (Pie Chart)', fontsize=14, fontweight='bold')
            
            # Plot 3: Horizontal bar for better readability
            ax3 = axes[1, 0]
            type_counts.plot(kind='barh', ax=ax3, color='lightcoral', edgecolor='black')
            ax3.set_title('Distribusi Attack Types (Horizontal)', fontsize=14, fontweight='bold')
            ax3.set_xlabel('Count', fontsize=11)
            ax3.set_ylabel('Attack Type', fontsize=11)
            ax3.grid(axis='x', alpha=0.3)
            
            # Plot 4: Log scale for better visibility
            ax4 = axes[1, 1]
            type_counts.plot(kind='bar', ax=ax4, color='lightgreen', edgecolor='black', logy=True)
            ax4.set_title('Distribusi Attack Types (Log Scale)', fontsize=14, fontweight='bold')
            ax4.set_xlabel('Attack Type', fontsize=11)
            ax4.set_ylabel('Count (log scale)', fontsize=11)
            ax4.tick_params(axis='x', rotation=45)
            ax4.grid(axis='y', alpha=0.3)
            
            plt.tight_layout()
            plt.savefig('toniot_target_distribution.png', dpi=300, bbox_inches='tight')
            display(HTML("<p><b>Visualisasi disimpan:</b> toniot_target_distribution.png</p>"))
            plt.show()
            
            # Markdown report
            self.markdown_report.append("## 2. Target Distribution\n\n")
            self.markdown_report.append("### Attack Types\n")
            self.markdown_report.append(type_df.to_markdown(index=False))
            self.markdown_report.append("\n\n")
    
    def analyze_missing_values(self):
        """
        Analisis komprehensif missing values dan placeholder '-'
        """
        display(HTML("<h2>3. ANALISIS MISSING VALUES & PLACEHOLDER</h2>"))
        
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
            display(HTML("<h3>Kolom dengan Missing Values (Top 20)</h3>"))
            
            display_df = missing_df.head(20).copy()
            display_df['NaN_Pct'] = display_df['NaN_Pct'].apply(lambda x: f"{x:.2f}%")
            display_df['Dash_Pct'] = display_df['Dash_Pct'].apply(lambda x: f"{x:.2f}%")
            display_df['Total_Missing_Pct'] = display_df['Total_Missing_Pct'].apply(lambda x: f"{x:.2f}%")
            
            display(display_df)
            
            # Summary statistics
            summary_df = pd.DataFrame({
                'Metric': [
                    'Kolom dengan missing',
                    'Kolom dengan >50% missing',
                    'Kolom dengan >90% missing'
                ],
                'Value': [
                    f"{len(missing_df)} dari {len(self.df_raw.columns)}",
                    str((missing_df['Total_Missing_Pct'] > 50).sum()),
                    str((missing_df['Total_Missing_Pct'] > 90).sum())
                ]
            })
            
            display(HTML("<h3>Ringkasan Missing Values</h3>"))
            display(summary_df)
            
            # Visualisasi
            top_missing = missing_df.head(15)
            
            plt.figure(figsize=(14, 8))
            x = np.arange(len(top_missing))
            width = 0.35
            
            plt.bar(x - width/2, top_missing['NaN_Pct'], 
                   width, label='NaN', color='#ff6b6b', edgecolor='black')
            plt.bar(x + width/2, top_missing['Dash_Pct'], 
                   width, label="Placeholder '-'", color='#4ecdc4', edgecolor='black')
            
            plt.xlabel('Kolom', fontsize=12, fontweight='bold')
            plt.ylabel('Persentase Missing (%)', fontsize=12, fontweight='bold')
            plt.title('Top 15 Kolom dengan Missing Values', fontsize=14, fontweight='bold')
            plt.xticks(x, top_missing['Column'], rotation=45, ha='right')
            plt.legend(fontsize=11)
            plt.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            plt.savefig('toniot_missing_values.png', dpi=300, bbox_inches='tight')
            display(HTML("<p><b>Visualisasi disimpan:</b> toniot_missing_values.png</p>"))
            plt.show()
            
            # Markdown report
            self.markdown_report.append("## 3. Missing Values Analysis\n\n")
            self.markdown_report.append(summary_df.to_markdown(index=False))
            self.markdown_report.append("\n\n")
        else:
            display(HTML("<p style='color:green;'><b>Tidak ada missing values dalam dataset!</b></p>"))
    
    def analyze_protocol_specific_features(self):
        """
        Analisis fitur yang spesifik untuk protokol tertentu
        (DNS, HTTP, SSL) - ini yang PENTING untuk TON_IoT!
        """
        display(HTML("<h2>4. ANALISIS PROTOCOL-SPECIFIC FEATURES</h2>"))
        display(HTML("<p style='color:orange;'><b>Catatan:</b> Missing values pada protocol-specific features seringkali BUKAN data hilang, tapi 'not applicable'!</p>"))
        
        protocol_summary = []
        
        # Protocol Distribution
        if 'proto' in self.df_raw.columns:
            display(HTML("<h3>Distribusi Protokol Transport Layer</h3>"))
            
            proto_counts = self.df_raw['proto'].value_counts()
            proto_pct = self.df_raw['proto'].value_counts(normalize=True) * 100
            
            proto_df = pd.DataFrame({
                'Protocol': proto_counts.index,
                'Count': proto_counts.values,
                'Percentage': [f"{x:.2f}%" for x in proto_pct.values]
            })
            
            display(proto_df)
            protocol_summary.append(proto_df)
        
        # Service Distribution
        if 'service' in self.df_raw.columns:
            display(HTML("<h3>Distribusi Services (Application Layer) - Top 15</h3>"))
            
            service_counts = self.df_raw['service'].value_counts().head(15)
            service_pct = self.df_raw['service'].value_counts(normalize=True).head(15) * 100
            
            service_df = pd.DataFrame({
                'Service': service_counts.index,
                'Count': service_counts.values,
                'Percentage': [f"{x:.2f}%" for x in service_pct.values]
            })
            
            display(service_df)
        
        # DNS Features Analysis
        dns_cols = ['dns_query', 'dns_qclass', 'dns_qtype', 'dns_rcode', 
                    'dns_AA', 'dns_RD', 'dns_RA', 'dns_rejected']
        dns_available = [col for col in dns_cols if col in self.df_raw.columns]
        
        if dns_available:
            display(HTML("<h3>DNS Features Analysis</h3>"))
            
            dns_present = self.df_raw[dns_available[0]].notna().sum()
            dns_pct = (dns_present / len(self.df_raw)) * 100
            
            dns_df = pd.DataFrame({
                'Metric': ['Records dengan DNS data', 'Records tanpa DNS data'],
                'Count': [f"{dns_present:,}", f"{len(self.df_raw) - dns_present:,}"],
                'Percentage': [f"{dns_pct:.2f}%", f"{100-dns_pct:.2f}%"]
            })
            
            display(dns_df)
            display(HTML(f"<p><b>Insight:</b> {100-dns_pct:.2f}% records TIDAK menggunakan DNS → Missing values pada DNS features adalah NORMAL!</p>"))
        
        # HTTP Features Analysis
        http_cols = ['http_method', 'http_uri', 'http_version', 'http_trans_depth',
                     'http_request_body_len', 'http_response_body_len', 
                     'http_status_code', 'http_user_agent']
        http_available = [col for col in http_cols if col in self.df_raw.columns]
        
        if http_available:
            display(HTML("<h3>HTTP Features Analysis</h3>"))
            
            http_present = self.df_raw[http_available[0]].notna().sum()
            http_pct = (http_present / len(self.df_raw)) * 100
            
            http_df = pd.DataFrame({
                'Metric': ['Records dengan HTTP data', 'Records tanpa HTTP data'],
                'Count': [f"{http_present:,}", f"{len(self.df_raw) - http_present:,}"],
                'Percentage': [f"{http_pct:.2f}%", f"{100-http_pct:.2f}%"]
            })
            
            display(http_df)
            display(HTML(f"<p><b>Insight:</b> {100-http_pct:.2f}% records TIDAK menggunakan HTTP → Missing values pada HTTP features adalah NORMAL!</p>"))
            
            if 'http_method' in self.df_raw.columns:
                display(HTML("<h4>HTTP Methods yang digunakan</h4>"))
                http_methods = self.df_raw['http_method'].value_counts().head(10)
                http_method_df = pd.DataFrame({
                    'Method': http_methods.index,
                    'Count': http_methods.values
                })
                display(http_method_df)
        
        # SSL Features Analysis
        ssl_cols = ['ssl_version', 'ssl_cipher', 'ssl_resumed', 
                    'ssl_established', 'ssl_subject', 'ssl_issuer']
        ssl_available = [col for col in ssl_cols if col in self.df_raw.columns]
        
        if ssl_available:
            display(HTML("<h3>SSL/TLS Features Analysis</h3>"))
            
            ssl_present = self.df_raw[ssl_available[0]].notna().sum()
            ssl_pct = (ssl_present / len(self.df_raw)) * 100
            
            ssl_df = pd.DataFrame({
                'Metric': ['Records dengan SSL data', 'Records tanpa SSL data'],
                'Count': [f"{ssl_present:,}", f"{len(self.df_raw) - ssl_present:,}"],
                'Percentage': [f"{ssl_pct:.2f}%", f"{100-ssl_pct:.2f}%"]
            })
            
            display(ssl_df)
            display(HTML(f"<p><b>Insight:</b> {100-ssl_pct:.2f}% records TIDAK menggunakan SSL → Missing values pada SSL features adalah NORMAL!</p>"))
        
        # Markdown report
        self.markdown_report.append("## 4. Protocol-Specific Features\n\n")
        self.markdown_report.append("Missing values pada protocol-specific features adalah NORMAL (not applicable)\n\n")
    
    def analyze_numerical_features(self):
        """
        Analisis statistik deskriptif untuk fitur numerik dengan scatter plots
        """
        display(HTML("<h2>5. ANALISIS NUMERICAL FEATURES</h2>"))
        
        # Identifikasi kolom numerik
        numeric_cols = self.df_raw.select_dtypes(include=[np.number]).columns.tolist()
        numeric_cols = [col for col in numeric_cols if col not in ['label']]
        
        if len(numeric_cols) > 0:
            display(HTML(f"<p>Ditemukan {len(numeric_cols)} kolom numerik</p>"))
            
            # Connection-level numerics
            connection_numerics = ['duration', 'src_bytes', 'dst_bytes', 
                                  'missed_bytes', 'src_pkts', 'dst_pkts',
                                  'src_ip_bytes', 'dst_ip_bytes', 
                                  'src_port', 'dst_port']
            
            available_connection = [col for col in connection_numerics 
                                   if col in numeric_cols]
            
            if available_connection:
                display(HTML("<h3>Connection-Level Features Statistics</h3>"))
                
                stats_df = self.df_raw[available_connection].describe().T
                stats_df['zeros'] = (self.df_raw[available_connection] == 0).sum()
                stats_df['zeros_pct'] = (stats_df['zeros'] / len(self.df_raw)) * 100
                
                stats_display = stats_df[['mean', 'std', 'min', 'max', 'zeros_pct']].copy()
                stats_display.columns = ['Mean', 'Std', 'Min', 'Max', 'Zeros (%)']
                stats_display = stats_display.round(2)
                
                display(stats_display)
                
                # Outlier detection
                display(HTML("<h3>Deteksi Outliers (IQR Method)</h3>"))
                
                outlier_data = []
                for col in available_connection[:5]:
                    Q1 = self.df_raw[col].quantile(0.25)
                    Q3 = self.df_raw[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    
                    outliers = ((self.df_raw[col] < lower_bound) | 
                               (self.df_raw[col] > upper_bound)).sum()
                    outliers_pct = (outliers / len(self.df_raw)) * 100
                    
                    outlier_data.append({
                        'Feature': col,
                        'Outliers': f"{outliers:,}",
                        'Percentage': f"{outliers_pct:.2f}%"
                    })
                
                outlier_df = pd.DataFrame(outlier_data)
                display(outlier_df)
                
                # Visualisasi distribusi
                fig, axes = plt.subplots(2, 3, figsize=(18, 12))
                axes = axes.flatten()
                
                for idx, col in enumerate(available_connection[:6]):
                    data = self.df_raw[self.df_raw[col] > 0][col]
                    
                    if len(data) > 0:
                        axes[idx].hist(data, bins=50, color='steelblue', 
                                      edgecolor='black', alpha=0.7)
                        axes[idx].set_title(f'{col} Distribution\n(excluding zeros)', 
                                          fontsize=11, fontweight='bold')
                        axes[idx].set_xlabel('Value', fontsize=10)
                        axes[idx].set_ylabel('Frequency', fontsize=10)
                        axes[idx].grid(axis='y', alpha=0.3)
                    else:
                        axes[idx].text(0.5, 0.5, 'No non-zero data', 
                                      ha='center', va='center', fontsize=10)
                        axes[idx].set_title(col, fontsize=11)
                
                plt.tight_layout()
                plt.savefig('toniot_numerical_distributions.png', dpi=300, bbox_inches='tight')
                display(HTML("<p><b>Visualisasi disimpan:</b> toniot_numerical_distributions.png</p>"))
                plt.show()
                
                # Scatter plots dengan label
                if 'type' in self.df_raw.columns:
                    display(HTML("<h3>Scatter Plots - Persebaran Data per Attack Type</h3>"))
                    
                    # Pilih fitur untuk scatter
                    scatter_features = [col for col in ['src_bytes', 'dst_bytes', 'duration', 'src_pkts'] 
                                       if col in available_connection]
                    
                    if len(scatter_features) >= 2:
                        # Sample data untuk visualisasi yang lebih cepat
                        sample_size = min(10000, len(self.df_raw))
                        df_sample = self.df_raw.sample(n=sample_size, random_state=42)
                        
                        # Create unique colors for each attack type
                        attack_types = df_sample['type'].unique()
                        colors_map = dict(zip(attack_types, plt.cm.tab20(np.linspace(0, 1, len(attack_types)))))
                        
                        fig, axes = plt.subplots(2, 2, figsize=(16, 14))
                        
                        # Scatter 1: src_bytes vs dst_bytes
                        if 'src_bytes' in scatter_features and 'dst_bytes' in scatter_features:
                            ax = axes[0, 0]
                            for attack_type in attack_types:
                                mask = df_sample['type'] == attack_type
                                ax.scatter(df_sample[mask]['src_bytes'], 
                                          df_sample[mask]['dst_bytes'],
                                          c=[colors_map[attack_type]], 
                                          label=attack_type, 
                                          alpha=0.6, 
                                          s=30,
                                          edgecolors='black',
                                          linewidths=0.3)
                            ax.set_xlabel('Source Bytes', fontsize=11, fontweight='bold')
                            ax.set_ylabel('Destination Bytes', fontsize=11, fontweight='bold')
                            ax.set_title('Source Bytes vs Destination Bytes', fontsize=12, fontweight='bold')
                            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
                            ax.grid(alpha=0.3)
                        
                        # Scatter 2: duration vs src_bytes
                        if 'duration' in scatter_features and 'src_bytes' in scatter_features:
                            ax = axes[0, 1]
                            for attack_type in attack_types:
                                mask = df_sample['type'] == attack_type
                                ax.scatter(df_sample[mask]['duration'], 
                                          df_sample[mask]['src_bytes'],
                                          c=[colors_map[attack_type]], 
                                          label=attack_type, 
                                          alpha=0.6, 
                                          s=30,
                                          edgecolors='black',
                                          linewidths=0.3)
                            ax.set_xlabel('Duration', fontsize=11, fontweight='bold')
                            ax.set_ylabel('Source Bytes', fontsize=11, fontweight='bold')
                            ax.set_title('Duration vs Source Bytes', fontsize=12, fontweight='bold')
                            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
                            ax.grid(alpha=0.3)
                        
                        # Scatter 3: src_pkts vs dst_pkts
                        if 'src_pkts' in scatter_features and 'dst_pkts' in available_connection:
                            ax = axes[1, 0]
                            for attack_type in attack_types:
                                mask = df_sample['type'] == attack_type
                                ax.scatter(df_sample[mask]['src_pkts'], 
                                          df_sample[mask].get('dst_pkts', 0),
                                          c=[colors_map[attack_type]], 
                                          label=attack_type, 
                                          alpha=0.6, 
                                          s=30,
                                          edgecolors='black',
                                          linewidths=0.3)
                            ax.set_xlabel('Source Packets', fontsize=11, fontweight='bold')
                            ax.set_ylabel('Destination Packets', fontsize=11, fontweight='bold')
                            ax.set_title('Source Packets vs Destination Packets', fontsize=12, fontweight='bold')
                            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
                            ax.grid(alpha=0.3)
                        
                        # Scatter 4: duration vs dst_bytes
                        if 'duration' in scatter_features and 'dst_bytes' in scatter_features:
                            ax = axes[1, 1]
                            for attack_type in attack_types:
                                mask = df_sample['type'] == attack_type
                                ax.scatter(df_sample[mask]['duration'], 
                                          df_sample[mask]['dst_bytes'],
                                          c=[colors_map[attack_type]], 
                                          label=attack_type, 
                                          alpha=0.6, 
                                          s=30,
                                          edgecolors='black',
                                          linewidths=0.3)
                            ax.set_xlabel('Duration', fontsize=11, fontweight='bold')
                            ax.set_ylabel('Destination Bytes', fontsize=11, fontweight='bold')
                            ax.set_title('Duration vs Destination Bytes', fontsize=12, fontweight='bold')
                            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
                            ax.grid(alpha=0.3)
                        
                        plt.tight_layout()
                        plt.savefig('toniot_scatter_plots.png', dpi=300, bbox_inches='tight')
                        display(HTML("<p><b>Visualisasi disimpan:</b> toniot_scatter_plots.png</p>"))
                        plt.show()
                
                # Markdown report
                self.markdown_report.append("## 5. Numerical Features\n\n")
                self.markdown_report.append(stats_display.to_markdown())
                self.markdown_report.append("\n\n")
        else:
            display(HTML("<p style='color:orange;'><b>Tidak ada kolom numerik yang ditemukan!</b></p>"))
    
    def analyze_categorical_features(self):
        """
        Analisis fitur kategorikal
        """
        display(HTML("<h2>6. ANALISIS CATEGORICAL FEATURES</h2>"))
        
        categorical_cols = self.df_raw.select_dtypes(include=['object']).columns.tolist()
        exclude_cols = ['label', 'type', 'src_ip', 'dst_ip']
        categorical_cols = [col for col in categorical_cols if col not in exclude_cols]
        
        if len(categorical_cols) > 0:
            display(HTML(f"<p>Ditemukan {len(categorical_cols)} kolom kategorikal</p>"))
            
            # Analyze key categorical features
            key_categoricals = ['proto', 'service', 'conn_state']
            available_categoricals = [col for col in key_categoricals 
                                     if col in categorical_cols]
            
            for col in available_categoricals:
                display(HTML(f"<h3>Feature: {col}</h3>"))
                
                value_counts = self.df_raw[col].value_counts()
                unique_count = self.df_raw[col].nunique()
                
                display(HTML(f"<p><b>Unique values:</b> {unique_count}</p>"))
                
                top_values = value_counts.head(10)
                top_pct = (top_values / len(self.df_raw) * 100)
                
                top_df = pd.DataFrame({
                    'Value': top_values.index,
                    'Count': top_values.values,
                    'Percentage': [f"{x:.2f}%" for x in top_pct.values]
                })
                
                display(HTML("<p><b>Most common values (Top 10):</b></p>"))
                display(top_df)
                
                if unique_count > 10:
                    display(HTML(f"<p>... dan {unique_count - 10} nilai lainnya</p>"))
            
            # Cardinality analysis
            display(HTML("<h3>Cardinality Analysis</h3>"))
            
            cardinality_data = []
            for col in categorical_cols[:15]:
                unique_count = self.df_raw[col].nunique()
                cardinality = "Low" if unique_count < 10 else \
                             "Medium" if unique_count < 50 else "High"
                cardinality_data.append({
                    'Feature': col,
                    'Unique Values': unique_count,
                    'Cardinality': cardinality
                })
            
            cardinality_df = pd.DataFrame(cardinality_data)
            display(cardinality_df)
            
            # Markdown report
            self.markdown_report.append("## 6. Categorical Features\n\n")
            self.markdown_report.append(cardinality_df.to_markdown(index=False))
            self.markdown_report.append("\n\n")
        else:
            display(HTML("<p style='color:orange;'><b>Tidak ada kolom kategorikal yang ditemukan!</b></p>"))
    
    def analyze_correlations(self):
        """
        Analisis korelasi antar fitur numerik - COMPLETE (kanan kiri atas bawah)
        """
        display(HTML("<h2>7. ANALISIS KORELASI FITUR NUMERIK</h2>"))
        
        numeric_cols = self.df_raw.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(numeric_cols) > 2:
            # Pilih fitur penting untuk korelasi
            key_features = ['src_bytes', 'dst_bytes', 'src_pkts', 'dst_pkts',
                           'duration', 'src_port', 'dst_port', 'label']
            
            available_features = [col for col in key_features 
                                 if col in numeric_cols]
            
            if len(available_features) > 2:
                display(HTML(f"<p>Menghitung korelasi untuk {len(available_features)} fitur...</p>"))
                
                corr_matrix = self.df_raw[available_features].corr()
                
                # Find highly correlated pairs
                display(HTML("<h3>Highly Correlated Features (|r| > 0.7)</h3>"))
                
                high_corr_data = []
                for i in range(len(corr_matrix.columns)):
                    for j in range(i+1, len(corr_matrix.columns)):
                        corr_val = corr_matrix.iloc[i, j]
                        if abs(corr_val) > 0.7:
                            col1 = corr_matrix.columns[i]
                            col2 = corr_matrix.columns[j]
                            high_corr_data.append({
                                'Feature 1': col1,
                                'Feature 2': col2,
                                'Correlation': f"{corr_val:.3f}"
                            })
                
                if high_corr_data:
                    high_corr_df = pd.DataFrame(high_corr_data)
                    display(high_corr_df)
                else:
                    display(HTML("<p style='color:green;'><b>Tidak ada korelasi tinggi yang ditemukan</b></p>"))
                
                # COMPLETE Heatmap - Tampilkan semua nilai (kanan kiri atas bawah)
                fig, axes = plt.subplots(1, 2, figsize=(20, 8))
                
                # Heatmap 1: Full correlation matrix (lengkap tanpa mask)
                ax1 = axes[0]
                sns.heatmap(corr_matrix, annot=True, fmt='.2f',
                           cmap='coolwarm', center=0, square=True,
                           linewidths=1, cbar_kws={"shrink": 0.8},
                           ax=ax1, vmin=-1, vmax=1)
                ax1.set_title('Complete Correlation Heatmap\n(All Values)', 
                         fontsize=14, fontweight='bold', pad=20)
                
                # Heatmap 2: Triangle untuk readability
                ax2 = axes[1]
                mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
                sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f',
                           cmap='coolwarm', center=0, square=True,
                           linewidths=1, cbar_kws={"shrink": 0.8},
                           ax=ax2, vmin=-1, vmax=1)
                ax2.set_title('Correlation Heatmap - Lower Triangle\n(Better Readability)', 
                         fontsize=14, fontweight='bold', pad=20)
                
                plt.tight_layout()
                plt.savefig('toniot_correlation_heatmap.png', dpi=300, bbox_inches='tight')
                display(HTML("<p><b>Visualisasi disimpan:</b> toniot_correlation_heatmap.png</p>"))
                plt.show()
                
                # Markdown report
                self.markdown_report.append("## 7. Correlation Analysis\n\n")
                if high_corr_data:
                    self.markdown_report.append(high_corr_df.to_markdown(index=False))
                else:
                    self.markdown_report.append("No high correlations found (|r| > 0.7)\n")
                self.markdown_report.append("\n\n")
        else:
            display(HTML("<p style='color:orange;'><b>Tidak cukup kolom numerik untuk analisis korelasi</b></p>"))
    
    def analyze_attack_patterns(self):
        """
        Analisis pola serangan per type
        """
        display(HTML("<h2>8. ANALISIS POLA SERANGAN PER TYPE</h2>"))
        
        if 'type' not in self.df_raw.columns:
            display(HTML("<p style='color:red;'><b>Kolom 'type' tidak ditemukan!</b></p>"))
            return
        
        attack_types = self.df_raw['type'].unique()
        
        key_features = ['src_bytes', 'dst_bytes', 'duration', 'src_pkts', 'dst_pkts']
        available_features = [col for col in key_features if col in self.df_raw.columns]
        
        if available_features:
            display(HTML(f"<p>Statistik per Attack Type (Top 10 attack types)</p>"))
            
            attack_stats = []
            for attack in list(attack_types)[:10]:
                attack_data = self.df_raw[self.df_raw['type'] == attack]
                
                stats_row = {'Attack Type': attack, 'Sample Size': len(attack_data)}
                
                for feature in available_features[:3]:
                    mean_val = attack_data[feature].mean()
                    median_val = attack_data[feature].median()
                    stats_row[f'{feature}_mean'] = f"{mean_val:.2f}"
                    stats_row[f'{feature}_median'] = f"{median_val:.2f}"
                
                attack_stats.append(stats_row)
            
            attack_stats_df = pd.DataFrame(attack_stats)
            display(attack_stats_df)
            
            # Markdown report
            self.markdown_report.append("## 8. Attack Patterns\n\n")
            self.markdown_report.append(attack_stats_df.to_markdown(index=False))
            self.markdown_report.append("\n\n")
    
    def generate_summary_report(self):
        """
        Generate ringkasan lengkap dari semua analisis
        """
        display(HTML("<h2>RINGKASAN LENGKAP EDA</h2>"))
        
        summary_data = {
            '1. Dataset Overview': [
                f"Shape: {self.df_raw.shape}",
                f"Memory: {self.df_raw.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
                f"Duplicates: {self.df_raw.duplicated().sum():,}"
            ],
            '2. Data Types': [
                f"{dtype}: {count} columns" 
                for dtype, count in self.df_raw.dtypes.value_counts().items()
            ],
            '3. Missing Values': [
                f"Total missing cells: {(self.df_raw.isnull().sum() + (self.df_raw == '-').sum()).sum():,}"
            ]
        }
        
        if 'type' in self.df_raw.columns:
            summary_data['4. Attack Distribution'] = [
                f"{attack}: {count:,} ({count/len(self.df_raw)*100:.2f}%)"
                for attack, count in self.df_raw['type'].value_counts().head(5).items()
            ]
        
        for section, items in summary_data.items():
            display(HTML(f"<h3>{section}</h3>"))
            for item in items:
                display(HTML(f"<p>{item}</p>"))
        
        display(HTML("<hr>"))
        display(HTML("<p style='color:green; font-size:16px;'><b>EDA SELESAI - Review data sebelum preprocessing!</b></p>"))
        display(HTML("<p><i>Simpan hasil EDA ini untuk referensi di masa mendatang.</i></p>"))
        
        # Finalize markdown report
        self.markdown_report.append("## 9. Summary\n\n")
        for section, items in summary_data.items():
            self.markdown_report.append(f"### {section}\n")
            for item in items:
                self.markdown_report.append(f"- {item}\n")
            self.markdown_report.append("\n")
        
        self.markdown_report.append("\n---\n**EDA SELESAI**\n")
    
    def export_to_markdown(self, filename='EDA_Report.md'):
        """
        Export laporan EDA ke file markdown
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(''.join(self.markdown_report))
        
        display(HTML(f"<h3>Export Successful!</h3>"))
        display(HTML(f"<p>Laporan EDA telah diekspor ke: <b>{filename}</b></p>"))
        print(f"\nLaporan berhasil disimpan: {filename}")
        
        return filename
