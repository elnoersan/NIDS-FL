# TON_IoT Network Dataset - EDA Report
**Dataset Shape**: 211,043 rows x 44 columns
**Load Time**: 0.37 seconds

## 1. Basic Information

### Data Types
| Data Type   |   Count |
|:------------|--------:|
| object      |      27 |
| int64       |      16 |
| float64     |       1 |

### Statistics
| Metric            | Value   |
|:------------------|:--------|
| Total Records     | 211,043 |
| Total Columns     | 44      |
| Duplicate Rows    | 20,569  |
| Memory Usage (MB) | 306.76  |

## 2. Target Distribution

### Attack Types
| Attack Type   |   Count | Percentage   |
|:--------------|--------:|:-------------|
| normal        |   50000 | 23.69%       |
| backdoor      |   20000 | 9.48%        |
| ddos          |   20000 | 9.48%        |
| dos           |   20000 | 9.48%        |
| injection     |   20000 | 9.48%        |
| password      |   20000 | 9.48%        |
| scanning      |   20000 | 9.48%        |
| ransomware    |   20000 | 9.48%        |
| xss           |   20000 | 9.48%        |
| mitm          |    1043 | 0.49%        |

## 3. Missing Values Analysis

| Metric                    | Value      |
|:--------------------------|:-----------|
| Kolom dengan missing      | 22 dari 44 |
| Kolom dengan >50% missing | 22         |
| Kolom dengan >90% missing | 16         |

## 4. Protocol-Specific Features

Missing values pada protocol-specific features adalah NORMAL (not applicable)

## 5. Numerical Features

|              |      Mean |              Std |   Min |              Max |   Zeros (%) |
|:-------------|----------:|-----------------:|------:|-----------------:|------------:|
| duration     |      7.7  |    564.14        |     0 |  93516.9         |       28.44 |
| src_bytes    | 258114    |      1.70949e+07 |     0 |      3.89086e+09 |       65.46 |
| dst_bytes    | 258805    |      1.80256e+07 |     0 |      3.91385e+09 |       70.55 |
| missed_bytes |  34432.3  |      5.26162e+06 |     0 |      1.85453e+09 |       98.6  |
| src_pkts     |      9.6  |     91.78        |     0 |  24623           |        8.1  |
| dst_pkts     |      3.85 |    330.71        |     0 | 121942           |       39.44 |
| src_ip_bytes |    776.08 |  22297           |     0 |      6.52263e+06 |        8.1  |
| dst_ip_bytes |   1584.69 | 190180           |     0 |      8.63955e+07 |       39.44 |
| src_port     |  38646.5  |  19307.3         |     1 |  65528           |        0    |
| dst_port     |   3495.15 |  10191.6         |     0 |  65467           |        0.02 |

## 6. Categorical Features

| Feature          |   Unique Values | Cardinality   |
|:-----------------|----------------:|:--------------|
| proto            |               3 | Low           |
| service          |               9 | Low           |
| conn_state       |              13 | Medium        |
| dns_query        |             726 | High          |
| dns_AA           |               3 | Low           |
| dns_RD           |               3 | Low           |
| dns_RA           |               3 | Low           |
| dns_rejected     |               3 | Low           |
| ssl_version      |               4 | Low           |
| ssl_cipher       |               6 | Low           |
| ssl_resumed      |               3 | Low           |
| ssl_established  |               3 | Low           |
| ssl_subject      |               6 | Low           |
| ssl_issuer       |               5 | Low           |
| http_trans_depth |              11 | Medium        |

## 7. Correlation Analysis

No high correlations found (|r| > 0.7)


## 8. Attack Patterns

| Attack Type   |   Sample Size |   src_bytes_mean |   src_bytes_median |   dst_bytes_mean |   dst_bytes_median |   duration_mean |   duration_median |
|:--------------|--------------:|-----------------:|-------------------:|-----------------:|-------------------:|----------------:|------------------:|
| backdoor      |         20000 |    173.17        |                  0 |    794.41        |                  0 |           37.02 |              0    |
| ddos          |         20000 |      2.38395e+06 |                  0 |      2.49887e+06 |                  0 |           17.08 |              0    |
| dos           |         20000 |     21.19        |                  0 |   4613.17        |                  0 |            0.49 |              0    |
| injection     |         20000 | 194818           |                256 | 200242           |               2153 |            1.45 |              0.25 |
| mitm          |          1043 |  14528.9         |                 94 |   4657.85        |                436 |           28.05 |              0.06 |
| normal        |         50000 |   2127.62        |                  0 |   9767.99        |                  0 |            3.99 |              0    |
| password      |         20000 |    127.49        |                155 |   1222.27        |                651 |            0.71 |              0    |
| ransomware    |         20000 |      0           |                  0 |      0           |                  0 |            0    |              0    |
| scanning      |         20000 |      4.05        |                  0 |     27.53        |                  0 |            0.31 |              0    |
| xss           |         20000 | 138478           |                  0 |    510.22        |                  0 |           12.76 |              0    |

## 9. Summary

### 1. Dataset Overview
- Shape: (211043, 44)
- Memory: 306.76 MB
- Duplicates: 20,569

### 2. Data Types
- object: 27 columns
- int64: 16 columns
- float64: 1 columns

### 3. Missing Values
- Total missing cells: 4,384,861

### 4. Attack Distribution
- normal: 50,000 (23.69%)
- backdoor: 20,000 (9.48%)
- ddos: 20,000 (9.48%)
- dos: 20,000 (9.48%)
- injection: 20,000 (9.48%)


---
**EDA SELESAI**
