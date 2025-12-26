# Federated Learning

## Federated Learning Averaging

### IID-like

#### 1. Batchsize 512 Epochs 1 Learning Rate 0.0005 Alpha Dirichlet 5

#### Round Result

MEMULAI PELATIHAN FEDERATED AVERAGING (FEDAVG) DENGAN FLOWER

--- PELATIHAN DETEKSI BINER DENGAN FLOWER ---

Melatih Model MLP Binary...

[INFO] Starting Flower federated learning for mlp_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
I0000 00:00:1765910947.710974  816873 gpu_device.cc:2020] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 2082 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1650 SUPER, pci bus id: 0000:07:00.0, compute capability: 7.5
      Round 1 - Avg Train Loss: 0.5128
      Round 1 - Avg Train Acc: 0.8829 - Time: 9.77s
      Round 2 - Avg Train Loss: 0.3424
      Round 2 - Avg Train Acc: 0.9453 - Time: 2.77s
      Round 3 - Avg Train Loss: 0.2976
      Round 3 - Avg Train Acc: 0.9462 - Time: 2.93s
      Round 4 - Avg Train Loss: 0.2602
      Round 4 - Avg Train Acc: 0.9466 - Time: 2.63s
      Round 5 - Avg Train Loss: 0.2324
      Round 5 - Avg Train Acc: 0.9475 - Time: 2.66s
      Round 6 - Avg Train Loss: 0.2105
      Round 6 - Avg Train Acc: 0.9480 - Time: 2.72s
      Round 7 - Avg Train Loss: 0.1917
      Round 7 - Avg Train Acc: 0.9489 - Time: 2.67s
      Round 8 - Avg Train Loss: 0.1782
      Round 8 - Avg Train Acc: 0.9496 - Time: 2.68s
      Round 9 - Avg Train Loss: 0.1670
      Round 9 - Avg Train Acc: 0.9504 - Time: 2.67s
      Round 10 - Avg Train Loss: 0.1578
      Round 10 - Avg Train Acc: 0.9506 - Time: 3.06s
      Round 11 - Avg Train Loss: 0.1519
      Round 11 - Avg Train Acc: 0.9511 - Time: 2.72s
      Round 12 - Avg Train Loss: 0.1457
      Round 12 - Avg Train Acc: 0.9513 - Time: 2.64s
      Round 13 - Avg Train Loss: 0.1415
      Round 13 - Avg Train Acc: 0.9513 - Time: 2.64s
      Round 14 - Avg Train Loss: 0.1375
      Round 14 - Avg Train Acc: 0.9516 - Time: 3.11s
      Round 15 - Avg Train Loss: 0.1343
      Round 15 - Avg Train Acc: 0.9514 - Time: 2.65s
      Round 16 - Avg Train Loss: 0.1324
      Round 16 - Avg Train Acc: 0.9515 - Time: 2.66s
      Round 17 - Avg Train Loss: 0.1295
      Round 17 - Avg Train Acc: 0.9517 - Time: 3.18s
      Round 18 - Avg Train Loss: 0.1276
      Round 18 - Avg Train Acc: 0.9518 - Time: 2.77s
      Round 19 - Avg Train Loss: 0.1270
      Round 19 - Avg Train Acc: 0.9517 - Time: 2.67s
      Round 20 - Avg Train Loss: 0.1239
      Round 20 - Avg Train Acc: 0.9530 - Time: 2.65s
   ✓ Model weights updated from federated training

Federated learning completed in 62.93s
   Captured 20 rounds of training metrics
   Avg time per round: 3.11s

Melatih Model CNN Binary...

[INFO] Starting Flower federated learning for cnn_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
      Round 1 - Avg Train Loss: 0.2837
      Round 1 - Avg Train Acc: 0.8851 - Time: 13.40s
      Round 2 - Avg Train Loss: 0.1478
      Round 2 - Avg Train Acc: 0.9447 - Time: 8.12s
      Round 3 - Avg Train Loss: 0.1354
      Round 3 - Avg Train Acc: 0.9471 - Time: 7.98s
      Round 4 - Avg Train Loss: 0.1305
      Round 4 - Avg Train Acc: 0.9479 - Time: 8.40s
      Round 5 - Avg Train Loss: 0.1247
      Round 5 - Avg Train Acc: 0.9501 - Time: 8.33s
      Round 6 - Avg Train Loss: 0.1201
      Round 6 - Avg Train Acc: 0.9516 - Time: 7.98s
      Round 7 - Avg Train Loss: 0.1159
      Round 7 - Avg Train Acc: 0.9523 - Time: 6.49s
      Round 8 - Avg Train Loss: 0.1100
      Round 8 - Avg Train Acc: 0.9545 - Time: 8.37s
      Round 9 - Avg Train Loss: 0.1046
      Round 9 - Avg Train Acc: 0.9562 - Time: 7.97s
      Round 10 - Avg Train Loss: 0.0987
      Round 10 - Avg Train Acc: 0.9589 - Time: 6.46s
      Round 11 - Avg Train Loss: 0.0935
      Round 11 - Avg Train Acc: 0.9608 - Time: 6.51s
      Round 12 - Avg Train Loss: 0.0906
      Round 12 - Avg Train Acc: 0.9614 - Time: 8.47s
      Round 13 - Avg Train Loss: 0.0856
      Round 13 - Avg Train Acc: 0.9640 - Time: 8.40s
      Round 14 - Avg Train Loss: 0.0826
      Round 14 - Avg Train Acc: 0.9652 - Time: 8.87s
      Round 15 - Avg Train Loss: 0.0829
      Round 15 - Avg Train Acc: 0.9651 - Time: 8.07s
      Round 16 - Avg Train Loss: 0.0805
      Round 16 - Avg Train Acc: 0.9670 - Time: 6.96s
      Round 17 - Avg Train Loss: 0.0788
      Round 17 - Avg Train Acc: 0.9667 - Time: 7.84s
      Round 18 - Avg Train Loss: 0.0784
      Round 18 - Avg Train Acc: 0.9672 - Time: 6.38s
      Round 19 - Avg Train Loss: 0.0767
      Round 19 - Avg Train Acc: 0.9677 - Time: 6.45s
      Round 20 - Avg Train Loss: 0.0768
      Round 20 - Avg Train Acc: 0.9678 - Time: 8.01s
   ✓ Model weights updated from federated training

Federated learning completed in 160.82s
   Captured 20 rounds of training metrics
   Avg time per round: 7.97s

--- PELATIHAN KLASIFIKASI MULTI-KELAS DENGAN FLOWER ---

Melatih Model MLP Multi-class...

[INFO] Starting Flower federated learning for mlp_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
      Round 1 - Avg Train Loss: 2.0829
      Round 1 - Avg Train Acc: 0.5779 - Time: 10.48s
      Round 2 - Avg Train Loss: 1.6193
      Round 2 - Avg Train Acc: 0.6695 - Time: 4.63s
      Round 3 - Avg Train Loss: 1.4268
      Round 3 - Avg Train Acc: 0.6814 - Time: 5.02s
      Round 4 - Avg Train Loss: 1.2831
      Round 4 - Avg Train Acc: 0.6869 - Time: 3.66s
      Round 5 - Avg Train Loss: 1.1705
      Round 5 - Avg Train Acc: 0.6916 - Time: 3.58s
      Round 6 - Avg Train Loss: 1.0797
      Round 6 - Avg Train Acc: 0.6936 - Time: 3.71s
      Round 7 - Avg Train Loss: 1.0116
      Round 7 - Avg Train Acc: 0.6955 - Time: 4.68s
      Round 8 - Avg Train Loss: 0.9556
      Round 8 - Avg Train Acc: 0.6984 - Time: 3.69s
      Round 9 - Avg Train Loss: 0.9133
      Round 9 - Avg Train Acc: 0.6989 - Time: 3.59s
      Round 10 - Avg Train Loss: 0.8794
      Round 10 - Avg Train Acc: 0.7004 - Time: 3.98s
      Round 11 - Avg Train Loss: 0.8521
      Round 11 - Avg Train Acc: 0.7019 - Time: 3.65s
      Round 12 - Avg Train Loss: 0.8310
      Round 12 - Avg Train Acc: 0.7033 - Time: 3.61s
      Round 13 - Avg Train Loss: 0.8121
      Round 13 - Avg Train Acc: 0.7037 - Time: 3.73s
      Round 14 - Avg Train Loss: 0.7985
      Round 14 - Avg Train Acc: 0.7065 - Time: 4.83s
      Round 15 - Avg Train Loss: 0.7850
      Round 15 - Avg Train Acc: 0.7074 - Time: 4.81s
      Round 16 - Avg Train Loss: 0.7750
      Round 16 - Avg Train Acc: 0.7103 - Time: 3.56s
      Round 17 - Avg Train Loss: 0.7639
      Round 17 - Avg Train Acc: 0.7123 - Time: 4.08s
      Round 18 - Avg Train Loss: 0.7544
      Round 18 - Avg Train Acc: 0.7153 - Time: 3.73s
      Round 19 - Avg Train Loss: 0.7451
      Round 19 - Avg Train Acc: 0.7166 - Time: 3.68s
      Round 20 - Avg Train Loss: 0.7390
      Round 20 - Avg Train Acc: 0.7195 - Time: 4.76s
   ✓ Model weights updated from federated training

Federated learning completed in 88.37s
   Captured 20 rounds of training metrics
   Avg time per round: 4.37s

Melatih Model CNN Multi-class...

[INFO] Starting Flower federated learning for cnn_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
      Round 1 - Avg Train Loss: 1.3692
      Round 1 - Avg Train Acc: 0.5452 - Time: 19.96s
      Round 2 - Avg Train Loss: 0.9916
      Round 2 - Avg Train Acc: 0.6602 - Time: 15.47s
      Round 3 - Avg Train Loss: 0.9050
      Round 3 - Avg Train Acc: 0.6765 - Time: 15.24s
      Round 4 - Avg Train Loss: 0.8520
      Round 4 - Avg Train Acc: 0.6864 - Time: 14.41s
      Round 5 - Avg Train Loss: 0.8145
      Round 5 - Avg Train Acc: 0.6924 - Time: 15.24s
      Round 6 - Avg Train Loss: 0.7839
      Round 6 - Avg Train Acc: 0.6978 - Time: 13.42s
      Round 7 - Avg Train Loss: 0.7579
      Round 7 - Avg Train Acc: 0.7041 - Time: 15.75s
      Round 8 - Avg Train Loss: 0.7406
      Round 8 - Avg Train Acc: 0.7102 - Time: 12.68s
      Round 9 - Avg Train Loss: 0.7226
      Round 9 - Avg Train Acc: 0.7157 - Time: 14.30s
      Round 10 - Avg Train Loss: 0.7008
      Round 10 - Avg Train Acc: 0.7237 - Time: 15.22s
      Round 11 - Avg Train Loss: 0.6818
      Round 11 - Avg Train Acc: 0.7321 - Time: 15.30s
      Round 12 - Avg Train Loss: 0.6683
      Round 12 - Avg Train Acc: 0.7381 - Time: 15.81s
      Round 13 - Avg Train Loss: 0.6606
      Round 13 - Avg Train Acc: 0.7420 - Time: 15.45s
      Round 14 - Avg Train Loss: 0.6477
      Round 14 - Avg Train Acc: 0.7461 - Time: 15.18s
      Round 15 - Avg Train Loss: 0.6373
      Round 15 - Avg Train Acc: 0.7500 - Time: 15.27s
      Round 16 - Avg Train Loss: 0.6285
      Round 16 - Avg Train Acc: 0.7535 - Time: 14.32s
      Round 17 - Avg Train Loss: 0.6133
      Round 17 - Avg Train Acc: 0.7607 - Time: 15.29s
      Round 18 - Avg Train Loss: 0.6129
      Round 18 - Avg Train Acc: 0.7614 - Time: 15.74s
      Round 19 - Avg Train Loss: 0.6021
      Round 19 - Avg Train Acc: 0.7654 - Time: 15.20s
      Round 20 - Avg Train Loss: 0.6006
      Round 20 - Avg Train Acc: 0.7663 - Time: 12.82s
   ✓ Model weights updated from federated training

Federated learning completed in 305.22s
   Captured 20 rounds of training metrics
   Avg time per round: 15.10s

Semua model berhasil dilatih!

#### Model Evaluasi

2025-12-17 01:59:26.173593: I external/local_xla/xla/service/service.cc:163] XLA service 0x7f6c600197e0 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2025-12-17 01:59:26.173608: I external/local_xla/xla/service/service.cc:171]   StreamExecutor device (0): NVIDIA GeForce GTX 1650 SUPER, Compute Capability 7.5
2025-12-17 01:59:26.177938: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:269] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.

EVALUASI SEMUA MODEL

--- EVALUASI MODEL BINARY ---

[1/4] MLP Binary...
2025-12-17 01:59:26.210944: I external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:473] Loaded cuDNN version 91600
I0000 00:00:1765911566.486509  816941 device_compiler.h:196] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.

📊 EVALUATION METRICS - MLP Binary (FedAvg):
   • Accuracy: 0.9569
   • Precision: 0.9487
   • Recall: 0.9974
   • F1 Score: 0.9725
   • AUC-ROC: 0.9929

📋 CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.83      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.96     42209

[2/4] CNN Binary...

📊 EVALUATION METRICS - CNN Binary (FedAvg):
   • Accuracy: 0.9698
   • Precision: 0.9916
   • Recall: 0.9686
   • F1 Score: 0.9800
   • AUC-ROC: 0.9968

📋 CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.91      0.97      0.94     10000
      Attack       0.99      0.97      0.98     32209

    accuracy                           0.97     42209
   macro avg       0.95      0.97      0.96     42209
weighted avg       0.97      0.97      0.97     42209

--- EVALUASI MODEL MULTI-CLASS ---

[3/4] MLP Multi-class...

📊 EVALUATION METRICS - MLP Multi (FedAvg):
   • Accuracy: 0.7111
   • Precision: 0.7462
   • Recall: 0.7111
   • F1 Score: 0.6757
   • AUC-ROC: 0.9582

📋 CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.45      0.99      0.62      4000
        ddos       0.95      0.90      0.92      4000
         dos       0.47      0.13      0.21      4000
   injection       0.54      0.92      0.68      4000
        mitm       0.33      0.00      0.01       209
      normal       0.98      0.83      0.90     10000
    password       0.69      0.05      0.10      4000
  ransomware       0.66      0.86      0.75      4000
    scanning       0.80      0.77      0.79      4000
         xss       0.85      0.79      0.82      4000

    accuracy                           0.71     42209
   macro avg       0.67      0.63      0.58     42209
weighted avg       0.75      0.71      0.68     42209

[4/4] CNN Multi-class...

📊 EVALUATION METRICS - CNN Multi (FedAvg):
   • Accuracy: 0.7778
   • Precision: 0.8018
   • Recall: 0.7778
   • F1 Score: 0.7664
   • AUC-ROC: 0.9850

📋 CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.46      1.00      0.63      4000
        ddos       0.95      0.93      0.94      4000
         dos       0.52      0.16      0.25      4000
   injection       0.94      0.66      0.77      4000
        mitm       0.43      0.19      0.26       209
      normal       0.88      0.97      0.92     10000
    password       0.71      0.74      0.73      4000
  ransomware       0.90      0.65      0.76      4000
    scanning       0.83      0.77      0.80      4000
         xss       0.93      0.84      0.88      4000

    accuracy                           0.78     42209
   macro avg       0.75      0.69      0.69     42209
weighted avg       0.80      0.78      0.77     42209

---

### Non IID

#### 2. Batchsize 512 Epochs 1 Learning Rate 0.0005 Alpha Dirichlet 0.3

#### Round Result

MEMULAI PELATIHAN FEDERATED AVERAGING (FEDAVG) DENGAN FLOWER

--- PELATIHAN DETEKSI BINER DENGAN FLOWER ---

Melatih Model MLP Binary...

[INFO] Starting Flower federated learning for mlp_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1

I0000 00:00:1765912305.622348  870034 gpu_device.cc:2020] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 2103 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1650 SUPER, pci bus id: 0000:07:00.0, compute capability: 7.5
      Round 1 - Avg Train Loss: 0.6679
      Round 1 - Avg Train Acc: 0.7594 - Time: 8.85s
      Round 2 - Avg Train Loss: 0.2735
      Round 2 - Avg Train Acc: 0.9650 - Time: 2.77s
      Round 3 - Avg Train Loss: 0.2074
      Round 3 - Avg Train Acc: 0.9673 - Time: 2.90s
      Round 4 - Avg Train Loss: 0.1682
      Round 4 - Avg Train Acc: 0.9682 - Time: 2.72s
      Round 5 - Avg Train Loss: 0.1385
      Round 5 - Avg Train Acc: 0.9692 - Time: 2.73s
      Round 6 - Avg Train Loss: 0.1219
      Round 6 - Avg Train Acc: 0.9699 - Time: 2.70s
      Round 7 - Avg Train Loss: 0.1099
      Round 7 - Avg Train Acc: 0.9701 - Time: 2.74s
      Round 8 - Avg Train Loss: 0.1002
      Round 8 - Avg Train Acc: 0.9708 - Time: 2.69s
      Round 9 - Avg Train Loss: 0.0963
      Round 9 - Avg Train Acc: 0.9713 - Time: 2.84s
      Round 10 - Avg Train Loss: 0.0909
      Round 10 - Avg Train Acc: 0.9713 - Time: 3.05s
      Round 11 - Avg Train Loss: 0.0896
      Round 11 - Avg Train Acc: 0.9718 - Time: 3.08s
      Round 12 - Avg Train Loss: 0.0875
      Round 12 - Avg Train Acc: 0.9714 - Time: 2.83s
      Round 13 - Avg Train Loss: 0.0846
      Round 13 - Avg Train Acc: 0.9725 - Time: 2.78s
      Round 14 - Avg Train Loss: 0.0841
      Round 14 - Avg Train Acc: 0.9725 - Time: 2.78s
      Round 15 - Avg Train Loss: 0.0824
      Round 15 - Avg Train Acc: 0.9722 - Time: 2.72s
      Round 16 - Avg Train Loss: 0.0838
      Round 16 - Avg Train Acc: 0.9719 - Time: 2.78s
      Round 17 - Avg Train Loss: 0.0812
      Round 17 - Avg Train Acc: 0.9723 - Time: 3.22s
      Round 18 - Avg Train Loss: 0.0805
      Round 18 - Avg Train Acc: 0.9724 - Time: 2.83s
      Round 19 - Avg Train Loss: 0.0800
      Round 19 - Avg Train Acc: 0.9725 - Time: 2.76s
      Round 20 - Avg Train Loss: 0.0799
      Round 20 - Avg Train Acc: 0.9725 - Time: 2.73s
   ✓ Model weights updated from federated training

Federated learning completed in 63.17s
   Captured 20 rounds of training metrics
   Avg time per round: 3.12s

Melatih Model CNN Binary...

[INFO] Starting Flower federated learning for cnn_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
      Round 1 - Avg Train Loss: 0.4952
      Round 1 - Avg Train Acc: 0.7091 - Time: 13.13s
      Round 2 - Avg Train Loss: 0.0969
      Round 2 - Avg Train Acc: 0.9661 - Time: 7.35s
      Round 3 - Avg Train Loss: 0.0847
      Round 3 - Avg Train Acc: 0.9697 - Time: 7.09s
      Round 4 - Avg Train Loss: 0.0823
      Round 4 - Avg Train Acc: 0.9708 - Time: 7.08s
      Round 5 - Avg Train Loss: 0.0779
      Round 5 - Avg Train Acc: 0.9714 - Time: 6.62s
      Round 6 - Avg Train Loss: 0.0764
      Round 6 - Avg Train Acc: 0.9726 - Time: 6.63s
      Round 7 - Avg Train Loss: 0.0715
      Round 7 - Avg Train Acc: 0.9737 - Time: 6.61s
      Round 8 - Avg Train Loss: 0.0665
      Round 8 - Avg Train Acc: 0.9754 - Time: 7.06s
      Round 9 - Avg Train Loss: 0.0667
      Round 9 - Avg Train Acc: 0.9742 - Time: 6.97s
      Round 10 - Avg Train Loss: 0.0636
      Round 10 - Avg Train Acc: 0.9765 - Time: 6.69s
      Round 11 - Avg Train Loss: 0.0621
      Round 11 - Avg Train Acc: 0.9775 - Time: 7.26s
      Round 12 - Avg Train Loss: 0.0636
      Round 12 - Avg Train Acc: 0.9754 - Time: 7.38s
      Round 13 - Avg Train Loss: 0.0619
      Round 13 - Avg Train Acc: 0.9772 - Time: 8.03s
      Round 14 - Avg Train Loss: 0.0554
      Round 14 - Avg Train Acc: 0.9795 - Time: 8.50s
      Round 15 - Avg Train Loss: 0.0555
      Round 15 - Avg Train Acc: 0.9794 - Time: 8.24s
      Round 16 - Avg Train Loss: 0.0541
      Round 16 - Avg Train Acc: 0.9791 - Time: 7.55s
      Round 17 - Avg Train Loss: 0.0540
      Round 17 - Avg Train Acc: 0.9797 - Time: 7.27s
      Round 18 - Avg Train Loss: 0.0520
      Round 18 - Avg Train Acc: 0.9804 - Time: 6.73s
      Round 19 - Avg Train Loss: 0.0534
      Round 19 - Avg Train Acc: 0.9803 - Time: 6.77s
      Round 20 - Avg Train Loss: 0.0515
      Round 20 - Avg Train Acc: 0.9815 - Time: 7.24s
   ✓ Model weights updated from federated training

Federated learning completed in 151.44s
   Captured 20 rounds of training metrics
   Avg time per round: 7.51s

--- PELATIHAN KLASIFIKASI MULTI-KELAS DENGAN FLOWER ---

Melatih Model MLP Multi-class...

[INFO] Starting Flower federated learning for mlp_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1

      Round 1 - Avg Train Loss: 1.8523
      Round 1 - Avg Train Acc: 0.6984 - Time: 10.76s
      Round 2 - Avg Train Loss: 1.4191
      Round 2 - Avg Train Acc: 0.7741 - Time: 3.73s
      Round 3 - Avg Train Loss: 1.2185
      Round 3 - Avg Train Acc: 0.7881 - Time: 4.95s
      Round 4 - Avg Train Loss: 1.0668
      Round 4 - Avg Train Acc: 0.7940 - Time: 3.64s
      Round 5 - Avg Train Loss: 0.9471
      Round 5 - Avg Train Acc: 0.7991 - Time: 3.69s
      Round 6 - Avg Train Loss: 0.8619
      Round 6 - Avg Train Acc: 0.8006 - Time: 3.87s
      Round 7 - Avg Train Loss: 0.7909
      Round 7 - Avg Train Acc: 0.8050 - Time: 3.56s
      Round 8 - Avg Train Loss: 0.7386
      Round 8 - Avg Train Acc: 0.8065 - Time: 4.65s
      Round 9 - Avg Train Loss: 0.6989
      Round 9 - Avg Train Acc: 0.8095 - Time: 3.58s
      Round 10 - Avg Train Loss: 0.6702
      Round 10 - Avg Train Acc: 0.8085 - Time: 4.18s
      Round 11 - Avg Train Loss: 0.6476
      Round 11 - Avg Train Acc: 0.8114 - Time: 3.82s
      Round 12 - Avg Train Loss: 0.6275
      Round 12 - Avg Train Acc: 0.8132 - Time: 3.67s
      Round 13 - Avg Train Loss: 0.6123
      Round 13 - Avg Train Acc: 0.8145 - Time: 3.76s
      Round 14 - Avg Train Loss: 0.6022
      Round 14 - Avg Train Acc: 0.8151 - Time: 3.75s
      Round 15 - Avg Train Loss: 0.5935
      Round 15 - Avg Train Acc: 0.8170 - Time: 3.88s
      Round 16 - Avg Train Loss: 0.5847
      Round 16 - Avg Train Acc: 0.8180 - Time: 3.59s
      Round 17 - Avg Train Loss: 0.5799
      Round 17 - Avg Train Acc: 0.8186 - Time: 4.21s
      Round 18 - Avg Train Loss: 0.5693
      Round 18 - Avg Train Acc: 0.8211 - Time: 4.67s
      Round 19 - Avg Train Loss: 0.5678
      Round 19 - Avg Train Acc: 0.8213 - Time: 4.67s
      Round 20 - Avg Train Loss: 0.5637
      Round 20 - Avg Train Acc: 0.8224 - Time: 3.66s
   ✓ Model weights updated from federated training

Federated learning completed in 87.43s
   Captured 20 rounds of training metrics
   Avg time per round: 4.32s

Melatih Model CNN Multi-class...

[INFO] Starting Flower federated learning for cnn_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
      Round 1 - Avg Train Loss: 1.0618
      Round 1 - Avg Train Acc: 0.6840 - Time: 18.72s
      Round 2 - Avg Train Loss: 0.7744
      Round 2 - Avg Train Acc: 0.7684 - Time: 15.94s
      Round 3 - Avg Train Loss: 0.6910
      Round 3 - Avg Train Acc: 0.7883 - Time: 15.15s
      Round 4 - Avg Train Loss: 0.6545
      Round 4 - Avg Train Acc: 0.7970 - Time: 14.50s
      Round 5 - Avg Train Loss: 0.6375
      Round 5 - Avg Train Acc: 0.7996 - Time: 15.16s
      Round 6 - Avg Train Loss: 0.6237
      Round 6 - Avg Train Acc: 0.8028 - Time: 15.65s
      Round 7 - Avg Train Loss: 0.5998
      Round 7 - Avg Train Acc: 0.8075 - Time: 13.72s
      Round 8 - Avg Train Loss: 0.5892
      Round 8 - Avg Train Acc: 0.8113 - Time: 15.31s
      Round 9 - Avg Train Loss: 0.5772
      Round 9 - Avg Train Acc: 0.8150 - Time: 15.27s
      Round 10 - Avg Train Loss: 0.5617
      Round 10 - Avg Train Acc: 0.8198 - Time: 13.44s
      Round 11 - Avg Train Loss: 0.5499
      Round 11 - Avg Train Acc: 0.8225 - Time: 15.23s
      Round 12 - Avg Train Loss: 0.5428
      Round 12 - Avg Train Acc: 0.8246 - Time: 16.06s
      Round 13 - Avg Train Loss: 0.5275
      Round 13 - Avg Train Acc: 0.8285 - Time: 15.36s
      Round 14 - Avg Train Loss: 0.5186
      Round 14 - Avg Train Acc: 0.8314 - Time: 13.54s
      Round 15 - Avg Train Loss: 0.5109
      Round 15 - Avg Train Acc: 0.8345 - Time: 15.19s
      Round 16 - Avg Train Loss: 0.4999
      Round 16 - Avg Train Acc: 0.8378 - Time: 15.25s
      Round 17 - Avg Train Loss: 0.4970
      Round 17 - Avg Train Acc: 0.8397 - Time: 15.18s
      Round 18 - Avg Train Loss: 0.4867
      Round 18 - Avg Train Acc: 0.8432 - Time: 14.94s
      Round 19 - Avg Train Loss: 0.4758
      Round 19 - Avg Train Acc: 0.8464 - Time: 14.55s
      Round 20 - Avg Train Loss: 0.4721
      Round 20 - Avg Train Acc: 0.8471 - Time: 13.43s
   ✓ Model weights updated from federated training

Federated learning completed in 304.76s
   Captured 20 rounds of training metrics
   Avg time per round: 15.08s

Semua model berhasil dilatih!

#### Model Evaluasi

EVALUASI SEMUA MODEL

--- EVALUASI MODEL BINARY ---

[1/4] MLP Binary...
2025-12-17 02:21:53.548803: I external/local_xla/xla/service/service.cc:163] XLA service 0x7fce58006270 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2025-12-17 02:21:53.548818: I external/local_xla/xla/service/service.cc:171]   StreamExecutor device (0): NVIDIA GeForce GTX 1650 SUPER, Compute Capability 7.5
2025-12-17 02:21:53.552657: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:269] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.
2025-12-17 02:21:53.586066: I external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:473] Loaded cuDNN version 91600
I0000 00:00:1765912913.850656  870270 device_compiler.h:196] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.

📊 EVALUATION METRICS - MLP Binary (FedAvg):
   • Accuracy: 0.9562
   • Precision: 0.9474
   • Recall: 0.9980
   • F1 Score: 0.9720
   • AUC-ROC: 0.9927

📋 CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.82      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.95     42209

[2/4] CNN Binary...

📊 EVALUATION METRICS - CNN Binary (FedAvg):
   • Accuracy: 0.9571
   • Precision: 0.9490
   • Recall: 0.9974
   • F1 Score: 0.9726
   • AUC-ROC: 0.9961

📋 CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.83      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.96     42209

--- EVALUASI MODEL MULTI-CLASS ---

[3/4] MLP Multi-class...

📊 EVALUATION METRICS - MLP Multi (FedAvg):
   • Accuracy: 0.6695
   • Precision: 0.6830
   • Recall: 0.6695
   • F1 Score: 0.6323
   • AUC-ROC: 0.9604

📋 CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.00      0.00      0.00      4000
        ddos       0.93      0.90      0.92      4000
         dos       0.36      0.88      0.51      4000
   injection       0.77      0.08      0.14      4000
        mitm       0.20      0.00      0.01       209
      normal       0.97      0.82      0.89     10000
    password       0.44      0.74      0.56      4000
  ransomware       0.66      0.86      0.75      4000
    scanning       0.79      0.78      0.78      4000
         xss       0.83      0.76      0.80      4000

    accuracy                           0.67     42209
   macro avg       0.59      0.58      0.53     42209
weighted avg       0.68      0.67      0.63     42209

[4/4] CNN Multi-class...

📊 EVALUATION METRICS - CNN Multi (FedAvg):
   • Accuracy: 0.6918
   • Precision: 0.7923
   • Recall: 0.6918
   • F1 Score: 0.6554
   • AUC-ROC: 0.9742

📋 CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       1.00      0.00      0.00      4000
        ddos       0.92      0.91      0.92      4000
         dos       0.37      0.94      0.53      4000
   injection       0.70      0.10      0.18      4000
        mitm       0.59      0.08      0.14       209
      normal       0.97      0.83      0.90     10000
    password       0.47      0.74      0.57      4000
  ransomware       0.71      0.91      0.80      4000
    scanning       0.83      0.78      0.80      4000
         xss       0.90      0.82      0.86      4000

    accuracy                           0.69     42209
   macro avg       0.75      0.61      0.57     42209
weighted avg       0.79      0.69      0.66     42209

---

## Federated Learning Proximal

### IID-like

#### 1. Batchsize 512 Epochs 1 Learning Rate 0.0005 Alpha Dirichlet 5 Mu 0.01

#### Round Result

MEMULAI PELATIHAN FEDERATED PROXIMAL (FEDPROX) DENGAN FLOWER
Proximal Term (μ) - Binary: 0.01, Multi-class: 0.01

--- PELATIHAN DETEKSI BINER DENGAN FEDPROX ---

Melatih Model MLP Binary...

[INFO] Starting Flower FedProx federated learning for mlp_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.01

I0000 00:00:1765913711.289869  917371 gpu_device.cc:2020] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 2103 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1650 SUPER, pci bus id: 0000:07:00.0, compute capability: 7.5
      Round 1 - Avg Train Loss: 0.7093
      Round 1 - Avg Train Acc: 0.8837 - Time: 9.60s
      Round 2 - Avg Train Loss: 0.7389
      Round 2 - Avg Train Acc: 0.9447 - Time: 3.55s
      Round 3 - Avg Train Loss: 0.7385
      Round 3 - Avg Train Acc: 0.9471 - Time: 3.65s
      Round 4 - Avg Train Loss: 0.7387
      Round 4 - Avg Train Acc: 0.9468 - Time: 3.65s
      Round 5 - Avg Train Loss: 0.7393
      Round 5 - Avg Train Acc: 0.9476 - Time: 3.72s
      Round 6 - Avg Train Loss: 0.7391
      Round 6 - Avg Train Acc: 0.9476 - Time: 3.70s
      Round 7 - Avg Train Loss: 0.7385
      Round 7 - Avg Train Acc: 0.9489 - Time: 3.83s
      Round 8 - Avg Train Loss: 0.7396
      Round 8 - Avg Train Acc: 0.9491 - Time: 4.24s
      Round 9 - Avg Train Loss: 0.7390
      Round 9 - Avg Train Acc: 0.9499 - Time: 3.90s
      Round 10 - Avg Train Loss: 0.7389
      Round 10 - Avg Train Acc: 0.9507 - Time: 4.19s
      Round 11 - Avg Train Loss: 0.7391
      Round 11 - Avg Train Acc: 0.9514 - Time: 3.90s
      Round 12 - Avg Train Loss: 0.7387
      Round 12 - Avg Train Acc: 0.9518 - Time: 3.95s
      Round 13 - Avg Train Loss: 0.7392
      Round 13 - Avg Train Acc: 0.9519 - Time: 4.07s
      Round 14 - Avg Train Loss: 0.7386
      Round 14 - Avg Train Acc: 0.9527 - Time: 4.12s
      Round 15 - Avg Train Loss: 0.7383
      Round 15 - Avg Train Acc: 0.9524 - Time: 4.10s
      Round 16 - Avg Train Loss: 0.7389
      Round 16 - Avg Train Acc: 0.9520 - Time: 4.24s
      Round 17 - Avg Train Loss: 0.7387
      Round 17 - Avg Train Acc: 0.9521 - Time: 4.13s
      Round 18 - Avg Train Loss: 0.7392
      Round 18 - Avg Train Acc: 0.9520 - Time: 4.54s
      Round 19 - Avg Train Loss: 0.7383
      Round 19 - Avg Train Acc: 0.9530 - Time: 4.58s
      Round 20 - Avg Train Loss: 0.7395
      Round 20 - Avg Train Acc: 0.9522 - Time: 4.33s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 87.38s
   Captured 20 rounds of training metrics
   Avg time per round: 4.30s

Melatih Model CNN Binary...

[INFO] Starting Flower FedProx federated learning for cnn_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.01
      Round 1 - Avg Train Loss: 0.7161
      Round 1 - Avg Train Acc: 0.8878 - Time: 13.54s
      Round 2 - Avg Train Loss: 0.7368
      Round 2 - Avg Train Acc: 0.9456 - Time: 8.83s
      Round 3 - Avg Train Loss: 0.7367
      Round 3 - Avg Train Acc: 0.9481 - Time: 7.51s
      Round 4 - Avg Train Loss: 0.7365
      Round 4 - Avg Train Acc: 0.9494 - Time: 7.57s
      Round 5 - Avg Train Loss: 0.7368
      Round 5 - Avg Train Acc: 0.9497 - Time: 9.37s
      Round 6 - Avg Train Loss: 0.7367
      Round 6 - Avg Train Acc: 0.9527 - Time: 9.31s
      Round 7 - Avg Train Loss: 0.7370
      Round 7 - Avg Train Acc: 0.9560 - Time: 9.39s
      Round 8 - Avg Train Loss: 0.7367
      Round 8 - Avg Train Acc: 0.9581 - Time: 9.00s
      Round 9 - Avg Train Loss: 0.7370
      Round 9 - Avg Train Acc: 0.9606 - Time: 7.77s
      Round 10 - Avg Train Loss: 0.7365
      Round 10 - Avg Train Acc: 0.9613 - Time: 7.82s
      Round 11 - Avg Train Loss: 0.7370
      Round 11 - Avg Train Acc: 0.9617 - Time: 8.25s
      Round 12 - Avg Train Loss: 0.7371
      Round 12 - Avg Train Acc: 0.9637 - Time: 9.26s
      Round 13 - Avg Train Loss: 0.7375
      Round 13 - Avg Train Acc: 0.9639 - Time: 9.60s
      Round 14 - Avg Train Loss: 0.7374
      Round 14 - Avg Train Acc: 0.9657 - Time: 9.72s
      Round 15 - Avg Train Loss: 0.7374
      Round 15 - Avg Train Acc: 0.9641 - Time: 9.68s
      Round 16 - Avg Train Loss: 0.7375
      Round 16 - Avg Train Acc: 0.9653 - Time: 9.81s
      Round 17 - Avg Train Loss: 0.7382
      Round 17 - Avg Train Acc: 0.9660 - Time: 8.57s
      Round 18 - Avg Train Loss: 0.7378
      Round 18 - Avg Train Acc: 0.9669 - Time: 9.51s
      Round 19 - Avg Train Loss: 0.7381
      Round 19 - Avg Train Acc: 0.9677 - Time: 9.39s
      Round 20 - Avg Train Loss: 0.7381
      Round 20 - Avg Train Acc: 0.9667 - Time: 9.49s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 185.51s
   Captured 20 rounds of training metrics
   Avg time per round: 9.17s

--- PELATIHAN KLASIFIKASI MULTI-KELAS DENGAN FEDPROX ---

Melatih Model MLP Multi-class...

[INFO] Starting Flower FedProx federated learning for mlp_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.01
      Round 1 - Avg Train Loss: 0.1000
      Round 1 - Avg Train Acc: 0.5613 - Time: 10.91s
      Round 2 - Avg Train Loss: 0.1000
      Round 2 - Avg Train Acc: 0.6699 - Time: 5.58s
      Round 3 - Avg Train Loss: 0.1000
      Round 3 - Avg Train Acc: 0.6838 - Time: 4.65s
      Round 4 - Avg Train Loss: 0.1000
      Round 4 - Avg Train Acc: 0.6899 - Time: 5.61s
      Round 5 - Avg Train Loss: 0.1000
      Round 5 - Avg Train Acc: 0.6928 - Time: 5.57s
      Round 6 - Avg Train Loss: 0.1000
      Round 6 - Avg Train Acc: 0.6959 - Time: 4.79s
      Round 7 - Avg Train Loss: 0.1000
      Round 7 - Avg Train Acc: 0.6971 - Time: 5.73s
      Round 8 - Avg Train Loss: 0.1000
      Round 8 - Avg Train Acc: 0.6990 - Time: 5.74s
      Round 9 - Avg Train Loss: 0.1000
      Round 9 - Avg Train Acc: 0.7004 - Time: 4.77s
      Round 10 - Avg Train Loss: 0.1000
      Round 10 - Avg Train Acc: 0.7019 - Time: 4.89s
      Round 11 - Avg Train Loss: 0.1000
      Round 11 - Avg Train Acc: 0.7014 - Time: 4.78s
      Round 12 - Avg Train Loss: 0.1000
      Round 12 - Avg Train Acc: 0.7039 - Time: 5.75s
      Round 13 - Avg Train Loss: 0.1000
      Round 13 - Avg Train Acc: 0.7041 - Time: 5.79s
      Round 14 - Avg Train Loss: 0.1000
      Round 14 - Avg Train Acc: 0.7055 - Time: 4.84s
      Round 15 - Avg Train Loss: 0.1000
      Round 15 - Avg Train Acc: 0.7082 - Time: 5.85s
      Round 16 - Avg Train Loss: 0.1000
      Round 16 - Avg Train Acc: 0.7100 - Time: 5.92s
      Round 17 - Avg Train Loss: 0.1000
      Round 17 - Avg Train Acc: 0.7123 - Time: 6.12s
      Round 18 - Avg Train Loss: 0.1000
      Round 18 - Avg Train Acc: 0.7146 - Time: 5.13s
      Round 19 - Avg Train Loss: 0.1000
      Round 19 - Avg Train Acc: 0.7175 - Time: 5.02s
      Round 20 - Avg Train Loss: 0.1000
      Round 20 - Avg Train Acc: 0.7204 - Time: 6.05s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 115.19s
   Captured 20 rounds of training metrics
   Avg time per round: 5.67s

 Melatih Model CNN Multi-class...

[INFO] Starting Flower FedProx federated learning for cnn_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.01
      Round 1 - Avg Train Loss: 0.1000
      Round 1 - Avg Train Acc: 0.5321 - Time: 18.60s
      Round 2 - Avg Train Loss: 0.1000
      Round 2 - Avg Train Acc: 0.6605 - Time: 14.20s
      Round 3 - Avg Train Loss: 0.1000
      Round 3 - Avg Train Acc: 0.6770 - Time: 16.07s
      Round 4 - Avg Train Loss: 0.1000
      Round 4 - Avg Train Acc: 0.6853 - Time: 16.17s
      Round 5 - Avg Train Loss: 0.1000
      Round 5 - Avg Train Acc: 0.6908 - Time: 16.19s
      Round 6 - Avg Train Loss: 0.1000
      Round 6 - Avg Train Acc: 0.6968 - Time: 16.39s
      Round 7 - Avg Train Loss: 0.1000
      Round 7 - Avg Train Acc: 0.7048 - Time: 16.37s
      Round 8 - Avg Train Loss: 0.1000
      Round 8 - Avg Train Acc: 0.7091 - Time: 16.50s
      Round 9 - Avg Train Loss: 0.1000
      Round 9 - Avg Train Acc: 0.7188 - Time: 16.31s
      Round 10 - Avg Train Loss: 0.1000
      Round 10 - Avg Train Acc: 0.7274 - Time: 16.47s
      Round 11 - Avg Train Loss: 0.1000
      Round 11 - Avg Train Acc: 0.7379 - Time: 14.60s
      Round 12 - Avg Train Loss: 0.1000
      Round 12 - Avg Train Acc: 0.7472 - Time: 16.52s
      Round 13 - Avg Train Loss: 0.1000
      Round 13 - Avg Train Acc: 0.7493 - Time: 15.86s
      Round 14 - Avg Train Loss: 0.1000
      Round 14 - Avg Train Acc: 0.7552 - Time: 16.61s
      Round 15 - Avg Train Loss: 0.1000
      Round 15 - Avg Train Acc: 0.7638 - Time: 16.87s
      Round 16 - Avg Train Loss: 0.1000
      Round 16 - Avg Train Acc: 0.7645 - Time: 16.66s
      Round 17 - Avg Train Loss: 0.1000
      Round 17 - Avg Train Acc: 0.7695 - Time: 16.88s
      Round 18 - Avg Train Loss: 0.1000
      Round 18 - Avg Train Acc: 0.7711 - Time: 16.22s
      Round 19 - Avg Train Loss: 0.1000
      Round 19 - Avg Train Acc: 0.7752 - Time: 14.23s
      Round 20 - Avg Train Loss: 0.1000
      Round 20 - Avg Train Acc: 0.7767 - Time: 16.28s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 327.97s
   Captured 20 rounds of training metrics
   Avg time per round: 16.20s

Semua model berhasil dilatih dengan FedProx!

#### Model Evaluasi

2025-12-17 02:47:08.474884: I external/local_xla/xla/service/service.cc:163] XLA service 0x7fb924011480 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2025-12-17 02:47:08.474899: I external/local_xla/xla/service/service.cc:171]   StreamExecutor device (0): NVIDIA GeForce GTX 1650 SUPER, Compute Capability 7.5
2025-12-17 02:47:08.479594: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:269] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.

--- EVALUASI MODEL BINARY ---

[1/4] MLP Binary...
2025-12-17 02:47:08.512736: I external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:473] Loaded cuDNN version 91600
I0000 00:00:1765914428.776009  917959 device_compiler.h:196] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.

EVALUATION METRICS - MLP Binary (FedProx):

- Accuracy: 0.9569
- Precision: 0.9487
- Recall: 0.9974
- F1 Score: 0.9725
- AUC-ROC: 0.9933

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.83      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.96     42209

[2/4] CNN Binary...

EVALUATION METRICS - CNN Binary (FedProx):

- Accuracy: 0.9687
- Precision: 0.9928
- Recall: 0.9660
- F1 Score: 0.9792
- AUC-ROC: 0.9969

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.90      0.98      0.94     10000
      Attack       0.99      0.97      0.98     32209

    accuracy                           0.97     42209
   macro avg       0.95      0.97      0.96     42209
weighted avg       0.97      0.97      0.97     42209

--- EVALUASI MODEL MULTI-CLASS ---

[3/4] MLP Multi-class...

EVALUATION METRICS - MLP Multi (FedProx):

- Accuracy: 0.7027
- Precision: 0.7292
- Recall: 0.7027
- F1 Score: 0.6816
- AUC-ROC: 0.9647

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.45      0.99      0.62      4000
        ddos       0.95      0.90      0.92      4000
         dos       0.40      0.12      0.19      4000
   injection       0.66      0.18      0.28      4000
        mitm       0.00      0.00      0.00       209
      normal       0.98      0.83      0.90     10000
    password       0.48      0.72      0.58      4000
  ransomware       0.66      0.86      0.75      4000
    scanning       0.80      0.77      0.79      4000
         xss       0.85      0.80      0.82      4000

    accuracy                           0.70     42209
   macro avg       0.62      0.62      0.58     42209
weighted avg       0.73      0.70      0.68     42209

[4/4] CNN Multi-class...

EVALUATION METRICS - CNN Multi (FedProx):

- Accuracy: 0.7718
- Precision: 0.8083
- Recall: 0.7718
- F1 Score: 0.7649
- AUC-ROC: 0.9815

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.48      0.99      0.65      4000
        ddos       0.93      0.94      0.94      4000
         dos       0.56      0.28      0.37      4000
   injection       0.95      0.48      0.64      4000
        mitm       0.40      0.12      0.19       209
      normal       0.89      0.97      0.93     10000
    password       0.60      0.74      0.66      4000
  ransomware       0.98      0.66      0.79      4000
    scanning       0.84      0.77      0.81      4000
         xss       0.92      0.84      0.88      4000

    accuracy                           0.77     42209
   macro avg       0.76      0.68      0.69     42209
weighted avg       0.81      0.77      0.76     42209

---

#### 2. Batchsize 512 Epochs 1 Learning Rate 0.0005 Alpha Dirichlet 5 Mu 0.001

#### Round Result

MEMULAI PELATIHAN FEDERATED PROXIMAL (FEDPROX) DENGAN FLOWER
Proximal Term (μ) - Binary: 0.001, Multi-class: 0.001

--- PELATIHAN DETEKSI BINER DENGAN FEDPROX ---

Melatih Model MLP Binary...

[INFO] Starting Flower FedProx federated learning for mlp_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.001

I0000 00:00:1765916573.415830  977181 gpu_device.cc:2020] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 2211 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1650 SUPER, pci bus id: 0000:07:00.0, compute capability: 7.5
      Round 1 - Avg Train Loss: 0.7237
      Round 1 - Avg Train Acc: 0.9002 - Time: 8.96s
      Round 2 - Avg Train Loss: 0.7387
      Round 2 - Avg Train Acc: 0.9449 - Time: 3.66s
      Round 3 - Avg Train Loss: 0.7391
      Round 3 - Avg Train Acc: 0.9464 - Time: 3.64s
      Round 4 - Avg Train Loss: 0.7401
      Round 4 - Avg Train Acc: 0.9467 - Time: 4.08s
      Round 5 - Avg Train Loss: 0.7394
      Round 5 - Avg Train Acc: 0.9468 - Time: 3.79s
      Round 6 - Avg Train Loss: 0.7396
      Round 6 - Avg Train Acc: 0.9480 - Time: 3.76s
      Round 7 - Avg Train Loss: 0.7389
      Round 7 - Avg Train Acc: 0.9491 - Time: 4.24s
      Round 8 - Avg Train Loss: 0.7398
      Round 8 - Avg Train Acc: 0.9495 - Time: 3.84s
      Round 9 - Avg Train Loss: 0.7395
      Round 9 - Avg Train Acc: 0.9506 - Time: 3.89s
      Round 10 - Avg Train Loss: 0.7390
      Round 10 - Avg Train Acc: 0.9510 - Time: 3.86s
      Round 11 - Avg Train Loss: 0.7391
      Round 11 - Avg Train Acc: 0.9509 - Time: 3.97s
      Round 12 - Avg Train Loss: 0.7387
      Round 12 - Avg Train Acc: 0.9516 - Time: 3.80s
      Round 13 - Avg Train Loss: 0.7388
      Round 13 - Avg Train Acc: 0.9516 - Time: 4.05s
      Round 14 - Avg Train Loss: 0.7395
      Round 14 - Avg Train Acc: 0.9517 - Time: 4.03s
      Round 15 - Avg Train Loss: 0.7394
      Round 15 - Avg Train Acc: 0.9516 - Time: 4.12s
      Round 16 - Avg Train Loss: 0.7401
      Round 16 - Avg Train Acc: 0.9517 - Time: 4.38s
      Round 17 - Avg Train Loss: 0.7392
      Round 17 - Avg Train Acc: 0.9521 - Time: 4.16s
      Round 18 - Avg Train Loss: 0.7390
      Round 18 - Avg Train Acc: 0.9524 - Time: 4.20s
      Round 19 - Avg Train Loss: 0.7394
      Round 19 - Avg Train Acc: 0.9532 - Time: 4.22s
      Round 20 - Avg Train Loss: 0.7392
      Round 20 - Avg Train Acc: 0.9531 - Time: 4.27s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 86.39s
   Captured 20 rounds of training metrics
   Avg time per round: 4.25s

Melatih Model CNN Binary...

[INFO] Starting Flower FedProx federated learning for cnn_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.001
      Round 1 - Avg Train Loss: 0.7310
      Round 1 - Avg Train Acc: 0.8849 - Time: 15.80s
      Round 2 - Avg Train Loss: 0.7381
      Round 2 - Avg Train Acc: 0.9452 - Time: 7.45s
      Round 3 - Avg Train Loss: 0.7371
      Round 3 - Avg Train Acc: 0.9479 - Time: 7.44s
      Round 4 - Avg Train Loss: 0.7374
      Round 4 - Avg Train Acc: 0.9493 - Time: 7.59s
      Round 5 - Avg Train Loss: 0.7381
      Round 5 - Avg Train Acc: 0.9505 - Time: 9.36s
      Round 6 - Avg Train Loss: 0.7385
      Round 6 - Avg Train Acc: 0.9551 - Time: 7.67s
      Round 7 - Avg Train Loss: 0.7382
      Round 7 - Avg Train Acc: 0.9579 - Time: 9.41s
      Round 8 - Avg Train Loss: 0.7381
      Round 8 - Avg Train Acc: 0.9607 - Time: 8.03s
      Round 9 - Avg Train Loss: 0.7380
      Round 9 - Avg Train Acc: 0.9615 - Time: 8.97s
      Round 10 - Avg Train Loss: 0.7379
      Round 10 - Avg Train Acc: 0.9634 - Time: 7.71s
      Round 11 - Avg Train Loss: 0.7382
      Round 11 - Avg Train Acc: 0.9633 - Time: 9.70s
      Round 12 - Avg Train Loss: 0.7382
      Round 12 - Avg Train Acc: 0.9640 - Time: 8.34s
      Round 13 - Avg Train Loss: 0.7382
      Round 13 - Avg Train Acc: 0.9647 - Time: 9.68s
      Round 14 - Avg Train Loss: 0.7382
      Round 14 - Avg Train Acc: 0.9654 - Time: 9.77s
      Round 15 - Avg Train Loss: 0.7375
      Round 15 - Avg Train Acc: 0.9647 - Time: 9.79s
      Round 16 - Avg Train Loss: 0.7384
      Round 16 - Avg Train Acc: 0.9658 - Time: 9.76s
      Round 17 - Avg Train Loss: 0.7384
      Round 17 - Avg Train Acc: 0.9669 - Time: 9.73s
      Round 18 - Avg Train Loss: 0.7381
      Round 18 - Avg Train Acc: 0.9669 - Time: 8.41s
      Round 19 - Avg Train Loss: 0.7378
      Round 19 - Avg Train Acc: 0.9674 - Time: 9.80s
      Round 20 - Avg Train Loss: 0.7375
      Round 20 - Avg Train Acc: 0.9672 - Time: 8.32s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 185.18s
   Captured 20 rounds of training metrics
   Avg time per round: 9.14s

--- PELATIHAN KLASIFIKASI MULTI-KELAS DENGAN FEDPROX ---

Melatih Model MLP Multi-class...

[INFO] Starting Flower FedProx federated learning for mlp_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.001
      Round 1 - Avg Train Loss: 0.1000
      Round 1 - Avg Train Acc: 0.5632 - Time: 11.84s
      Round 2 - Avg Train Loss: 0.1000
      Round 2 - Avg Train Acc: 0.6700 - Time: 5.58s
      Round 3 - Avg Train Loss: 0.1000
      Round 3 - Avg Train Acc: 0.6824 - Time: 5.67s
      Round 4 - Avg Train Loss: 0.1000
      Round 4 - Avg Train Acc: 0.6878 - Time: 4.62s
      Round 5 - Avg Train Loss: 0.1000
      Round 5 - Avg Train Acc: 0.6922 - Time: 5.63s
      Round 6 - Avg Train Loss: 0.1000
      Round 6 - Avg Train Acc: 0.6945 - Time: 4.68s
      Round 7 - Avg Train Loss: 0.1000
      Round 7 - Avg Train Acc: 0.6960 - Time: 4.77s
      Round 8 - Avg Train Loss: 0.1000
      Round 8 - Avg Train Acc: 0.6980 - Time: 5.77s
      Round 9 - Avg Train Loss: 0.1000
      Round 9 - Avg Train Acc: 0.6985 - Time: 5.83s
      Round 10 - Avg Train Loss: 0.1000
      Round 10 - Avg Train Acc: 0.7004 - Time: 5.86s
      Round 11 - Avg Train Loss: 0.1000
      Round 11 - Avg Train Acc: 0.7011 - Time: 4.79s
      Round 12 - Avg Train Loss: 0.1000
      Round 12 - Avg Train Acc: 0.7040 - Time: 4.97s
      Round 13 - Avg Train Loss: 0.1000
      Round 13 - Avg Train Acc: 0.7055 - Time: 5.93s
      Round 14 - Avg Train Loss: 0.1000
      Round 14 - Avg Train Acc: 0.7067 - Time: 5.92s
      Round 15 - Avg Train Loss: 0.1000
      Round 15 - Avg Train Acc: 0.7086 - Time: 5.92s
      Round 16 - Avg Train Loss: 0.1000
      Round 16 - Avg Train Acc: 0.7102 - Time: 5.92s
      Round 17 - Avg Train Loss: 0.1000
      Round 17 - Avg Train Acc: 0.7145 - Time: 6.03s
      Round 18 - Avg Train Loss: 0.1000
      Round 18 - Avg Train Acc: 0.7177 - Time: 5.08s
      Round 19 - Avg Train Loss: 0.1000
      Round 19 - Avg Train Acc: 0.7203 - Time: 6.08s
      Round 20 - Avg Train Loss: 0.1000
      Round 20 - Avg Train Acc: 0.7234 - Time: 6.16s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 118.68s
   Captured 20 rounds of training metrics
   Avg time per round: 5.85s

 Melatih Model CNN Multi-class...

[INFO] Starting Flower FedProx federated learning for cnn_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.001
      Round 1 - Avg Train Loss: 0.1000
      Round 1 - Avg Train Acc: 0.5385 - Time: 20.39s
      Round 2 - Avg Train Loss: 0.1000
      Round 2 - Avg Train Acc: 0.6592 - Time: 14.30s
      Round 3 - Avg Train Loss: 0.1000
      Round 3 - Avg Train Acc: 0.6779 - Time: 16.11s
      Round 4 - Avg Train Loss: 0.1000
      Round 4 - Avg Train Acc: 0.6866 - Time: 16.33s
      Round 5 - Avg Train Loss: 0.1000
      Round 5 - Avg Train Acc: 0.6940 - Time: 15.56s
      Round 6 - Avg Train Loss: 0.1000
      Round 6 - Avg Train Acc: 0.6991 - Time: 15.49s
      Round 7 - Avg Train Loss: 0.1000
      Round 7 - Avg Train Acc: 0.7067 - Time: 14.44s
      Round 8 - Avg Train Loss: 0.1000
      Round 8 - Avg Train Acc: 0.7128 - Time: 16.53s
      Round 9 - Avg Train Loss: 0.1000
      Round 9 - Avg Train Acc: 0.7219 - Time: 15.78s
      Round 10 - Avg Train Loss: 0.1000
      Round 10 - Avg Train Acc: 0.7298 - Time: 16.45s
      Round 11 - Avg Train Loss: 0.1000
      Round 11 - Avg Train Acc: 0.7412 - Time: 15.79s
      Round 12 - Avg Train Loss: 0.1000
      Round 12 - Avg Train Acc: 0.7470 - Time: 16.61s
      Round 13 - Avg Train Loss: 0.1000
      Round 13 - Avg Train Acc: 0.7562 - Time: 16.62s
      Round 14 - Avg Train Loss: 0.1000
      Round 14 - Avg Train Acc: 0.7630 - Time: 16.65s
      Round 15 - Avg Train Loss: 0.1000
      Round 15 - Avg Train Acc: 0.7676 - Time: 16.75s
      Round 16 - Avg Train Loss: 0.1000
      Round 16 - Avg Train Acc: 0.7683 - Time: 16.69s
      Round 17 - Avg Train Loss: 0.1000
      Round 17 - Avg Train Acc: 0.7716 - Time: 16.78s
      Round 18 - Avg Train Loss: 0.1000
      Round 18 - Avg Train Acc: 0.7726 - Time: 16.89s
      Round 19 - Avg Train Loss: 0.1000
      Round 19 - Avg Train Acc: 0.7788 - Time: 17.08s
      Round 20 - Avg Train Loss: 0.1000
      Round 20 - Avg Train Acc: 0.7798 - Time: 15.04s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 330.25s
   Captured 20 rounds of training metrics
   Avg time per round: 16.31s

Semua model berhasil dilatih dengan FedProx!

#### Model Evaluasi

2025-12-17 03:34:55.019835: I external/local_xla/xla/service/service.cc:163] XLA service 0x7efca4003e00 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2025-12-17 03:34:55.019850: I external/local_xla/xla/service/service.cc:171]   StreamExecutor device (0): NVIDIA GeForce GTX 1650 SUPER, Compute Capability 7.5
2025-12-17 03:34:55.024002: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:269] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.

EVALUASI SEMUA MODEL

--- EVALUASI MODEL BINARY ---

[1/4] MLP Binary...
2025-12-17 03:34:55.058105: I external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:473] Loaded cuDNN version 91600
I0000 00:00:1765917295.335485  977327 device_compiler.h:196] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.

EVALUATION METRICS - MLP Binary (FedProx):

- Accuracy: 0.9569
- Precision: 0.9487
- Recall: 0.9974
- F1 Score: 0.9725
- AUC-ROC: 0.9931

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.83      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.96     42209

[2/4] CNN Binary...

EVALUATION METRICS - CNN Binary (FedProx):

- Accuracy: 0.9660
- Precision: 0.9918
- Recall: 0.9634
- F1 Score: 0.9774
- AUC-ROC: 0.9962

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.89      0.97      0.93     10000
      Attack       0.99      0.96      0.98     32209

    accuracy                           0.97     42209
   macro avg       0.94      0.97      0.95     42209
weighted avg       0.97      0.97      0.97     42209

--- EVALUASI MODEL MULTI-CLASS ---

[3/4] MLP Multi-class...

EVALUATION METRICS - MLP Multi (FedProx):

- Accuracy: 0.7036
- Precision: 0.7389
- Recall: 0.7036
- F1 Score: 0.6815
- AUC-ROC: 0.9745

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.45      0.99      0.62      4000
        ddos       0.94      0.90      0.92      4000
         dos       0.45      0.12      0.19      4000
   injection       0.67      0.18      0.29      4000
        mitm       1.00      0.01      0.02       209
      normal       0.98      0.83      0.90     10000
    password       0.48      0.74      0.59      4000
  ransomware       0.66      0.86      0.75      4000
    scanning       0.78      0.78      0.78      4000
         xss       0.85      0.79      0.82      4000

    accuracy                           0.70     42209
   macro avg       0.73      0.62      0.59     42209
weighted avg       0.74      0.70      0.68     42209

[4/4] CNN Multi-class...

EVALUATION METRICS - CNN Multi (FedProx):

- Accuracy: 0.7861
- Precision: 0.8192
- Recall: 0.7861
- F1 Score: 0.7802
- AUC-ROC: 0.9817

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.46      1.00      0.63      4000
        ddos       0.94      0.94      0.94      4000
         dos       0.59      0.24      0.34      4000
   injection       0.95      0.67      0.79      4000
        mitm       0.30      0.06      0.10       209
      normal       0.89      0.97      0.93     10000
    password       0.71      0.74      0.72      4000
  ransomware       0.98      0.66      0.79      4000
    scanning       0.83      0.77      0.80      4000
         xss       0.93      0.84      0.88      4000

    accuracy                           0.79     42209
   macro avg       0.76      0.69      0.69     42209
weighted avg       0.82      0.79      0.78     42209

---

### Non IID

#### 1. Batchsize 512 Epochs 1 Learning Rate 0.0005 Alpha Dirichlet 0.3 Mu 0.01

#### Round Result

MEMULAI PELATIHAN FEDERATED PROXIMAL (FEDPROX) DENGAN FLOWER
Proximal Term (μ) - Binary: 0.01, Multi-class: 0.01

--- PELATIHAN DETEKSI BINER DENGAN FEDPROX ---

Melatih Model MLP Binary...

[INFO] Starting Flower FedProx federated learning for mlp_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.01

I0000 00:00:1765920096.496809 1096747 gpu_device.cc:2020] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 2217 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1650 SUPER, pci bus id: 0000:07:00.0, compute capability: 7.5

      Round 1 - Avg Train Loss: 0.5834
      Round 1 - Avg Train Acc: 0.7300 - Time: 9.10s
      Round 2 - Avg Train Loss: 0.7971
      Round 2 - Avg Train Acc: 0.9652 - Time: 3.82s
      Round 3 - Avg Train Loss: 0.7952
      Round 3 - Avg Train Acc: 0.9676 - Time: 3.88s
      Round 4 - Avg Train Loss: 0.7960
      Round 4 - Avg Train Acc: 0.9681 - Time: 4.06s
      Round 5 - Avg Train Loss: 0.7963
      Round 5 - Avg Train Acc: 0.9688 - Time: 3.92s
      Round 6 - Avg Train Loss: 0.7954
      Round 6 - Avg Train Acc: 0.9696 - Time: 3.89s
      Round 7 - Avg Train Loss: 0.7979
      Round 7 - Avg Train Acc: 0.9709 - Time: 4.04s
      Round 8 - Avg Train Loss: 0.7995
      Round 8 - Avg Train Acc: 0.9708 - Time: 3.93s
      Round 9 - Avg Train Loss: 0.7984
      Round 9 - Avg Train Acc: 0.9718 - Time: 4.02s
      Round 10 - Avg Train Loss: 0.7951
      Round 10 - Avg Train Acc: 0.9715 - Time: 4.26s
      Round 11 - Avg Train Loss: 0.7997
      Round 11 - Avg Train Acc: 0.9715 - Time: 4.11s
      Round 12 - Avg Train Loss: 0.7983
      Round 12 - Avg Train Acc: 0.9719 - Time: 4.23s
      Round 13 - Avg Train Loss: 0.7995
      Round 13 - Avg Train Acc: 0.9720 - Time: 4.17s
      Round 14 - Avg Train Loss: 0.8003
      Round 14 - Avg Train Acc: 0.9723 - Time: 4.19s
      Round 15 - Avg Train Loss: 0.7998
      Round 15 - Avg Train Acc: 0.9724 - Time: 4.31s
      Round 16 - Avg Train Loss: 0.8011
      Round 16 - Avg Train Acc: 0.9723 - Time: 4.32s
      Round 17 - Avg Train Loss: 0.8001
      Round 17 - Avg Train Acc: 0.9722 - Time: 4.44s
      Round 18 - Avg Train Loss: 0.7992
      Round 18 - Avg Train Acc: 0.9726 - Time: 4.34s
      Round 19 - Avg Train Loss: 0.8003
      Round 19 - Avg Train Acc: 0.9728 - Time: 4.50s
      Round 20 - Avg Train Loss: 0.7994
      Round 20 - Avg Train Acc: 0.9724 - Time: 4.48s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 89.42s
   Captured 20 rounds of training metrics
   Avg time per round: 4.40s

Melatih Model CNN Binary...

[INFO] Starting Flower FedProx federated learning for cnn_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.01

      Round 1 - Avg Train Loss: 0.7438
      Round 1 - Avg Train Acc: 0.8876 - Time: 13.60s
      Round 2 - Avg Train Loss: 0.8018
      Round 2 - Avg Train Acc: 0.9679 - Time: 8.08s
      Round 3 - Avg Train Loss: 0.8006
      Round 3 - Avg Train Acc: 0.9699 - Time: 8.88s
      Round 4 - Avg Train Loss: 0.7991
      Round 4 - Avg Train Acc: 0.9705 - Time: 8.27s
      Round 5 - Avg Train Loss: 0.8010
      Round 5 - Avg Train Acc: 0.9710 - Time: 7.75s
      Round 6 - Avg Train Loss: 0.8017
      Round 6 - Avg Train Acc: 0.9749 - Time: 9.30s
      Round 7 - Avg Train Loss: 0.8012
      Round 7 - Avg Train Acc: 0.9743 - Time: 9.49s
      Round 8 - Avg Train Loss: 0.8008
      Round 8 - Avg Train Acc: 0.9740 - Time: 7.88s
      Round 9 - Avg Train Loss: 0.7998
      Round 9 - Avg Train Acc: 0.9764 - Time: 8.01s
      Round 10 - Avg Train Loss: 0.8007
      Round 10 - Avg Train Acc: 0.9778 - Time: 9.55s
      Round 11 - Avg Train Loss: 0.8000
      Round 11 - Avg Train Acc: 0.9777 - Time: 8.13s
      Round 12 - Avg Train Loss: 0.8020
      Round 12 - Avg Train Acc: 0.9782 - Time: 9.16s
      Round 13 - Avg Train Loss: 0.8008
      Round 13 - Avg Train Acc: 0.9799 - Time: 8.23s
      Round 14 - Avg Train Loss: 0.8038
      Round 14 - Avg Train Acc: 0.9788 - Time: 8.68s
      Round 15 - Avg Train Loss: 0.8026
      Round 15 - Avg Train Acc: 0.9799 - Time: 8.29s
      Round 16 - Avg Train Loss: 0.8011
      Round 16 - Avg Train Acc: 0.9789 - Time: 8.77s
      Round 17 - Avg Train Loss: 0.8026
      Round 17 - Avg Train Acc: 0.9803 - Time: 8.34s
      Round 18 - Avg Train Loss: 0.8023
      Round 18 - Avg Train Acc: 0.9800 - Time: 9.45s
      Round 19 - Avg Train Loss: 0.8033
      Round 19 - Avg Train Acc: 0.9805 - Time: 8.62s
      Round 20 - Avg Train Loss: 0.8042
      Round 20 - Avg Train Acc: 0.9806 - Time: 8.98s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 179.92s
   Captured 20 rounds of training metrics
   Avg time per round: 8.87s

--- PELATIHAN KLASIFIKASI MULTI-KELAS DENGAN FEDPROX ---

Melatih Model MLP Multi-class...

[INFO] Starting Flower FedProx federated learning for mlp_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.01

      Round 1 - Avg Train Loss: 0.1000
      Round 1 - Avg Train Acc: 0.6992 - Time: 12.07s
      Round 2 - Avg Train Loss: 0.1000
      Round 2 - Avg Train Acc: 0.7751 - Time: 4.59s
      Round 3 - Avg Train Loss: 0.1000
      Round 3 - Avg Train Acc: 0.7887 - Time: 4.57s
      Round 4 - Avg Train Loss: 0.1000
      Round 4 - Avg Train Acc: 0.7950 - Time: 4.71s
      Round 5 - Avg Train Loss: 0.1000
      Round 5 - Avg Train Acc: 0.7989 - Time: 4.80s
      Round 6 - Avg Train Loss: 0.1000
      Round 6 - Avg Train Acc: 0.8030 - Time: 4.84s
      Round 7 - Avg Train Loss: 0.1000
      Round 7 - Avg Train Acc: 0.8034 - Time: 4.78s
      Round 8 - Avg Train Loss: 0.1000
      Round 8 - Avg Train Acc: 0.8055 - Time: 4.75s
      Round 9 - Avg Train Loss: 0.1000
      Round 9 - Avg Train Acc: 0.8077 - Time: 4.86s
      Round 10 - Avg Train Loss: 0.1000
      Round 10 - Avg Train Acc: 0.8095 - Time: 4.96s
      Round 11 - Avg Train Loss: 0.1000
      Round 11 - Avg Train Acc: 0.8102 - Time: 4.93s
      Round 12 - Avg Train Loss: 0.1000
      Round 12 - Avg Train Acc: 0.8130 - Time: 5.06s
      Round 13 - Avg Train Loss: 0.1000
      Round 13 - Avg Train Acc: 0.8143 - Time: 5.05s
      Round 14 - Avg Train Loss: 0.1000
      Round 14 - Avg Train Acc: 0.8156 - Time: 5.05s
      Round 15 - Avg Train Loss: 0.1000
      Round 15 - Avg Train Acc: 0.8160 - Time: 5.14s
      Round 16 - Avg Train Loss: 0.1000
      Round 16 - Avg Train Acc: 0.8170 - Time: 5.21s
      Round 17 - Avg Train Loss: 0.1000
      Round 17 - Avg Train Acc: 0.8187 - Time: 5.18s
      Round 18 - Avg Train Loss: 0.1000
      Round 18 - Avg Train Acc: 0.8197 - Time: 5.19s
      Round 19 - Avg Train Loss: 0.1000
      Round 19 - Avg Train Acc: 0.8208 - Time: 5.34s
      Round 20 - Avg Train Loss: 0.1000
      Round 20 - Avg Train Acc: 0.8224 - Time: 5.97s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 108.77s
   Captured 20 rounds of training metrics
   Avg time per round: 5.35s

 Melatih Model CNN Multi-class...

[INFO] Starting Flower FedProx federated learning for cnn_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.01

      Round 1 - Avg Train Loss: 0.1000
      Round 1 - Avg Train Acc: 0.6794 - Time: 20.43s
      Round 2 - Avg Train Loss: 0.1000
      Round 2 - Avg Train Acc: 0.7597 - Time: 15.93s
      Round 3 - Avg Train Loss: 0.1000
      Round 3 - Avg Train Acc: 0.7860 - Time: 16.11s
      Round 4 - Avg Train Loss: 0.1000
      Round 4 - Avg Train Acc: 0.7960 - Time: 16.17s
      Round 5 - Avg Train Loss: 0.1000
      Round 5 - Avg Train Acc: 0.8011 - Time: 16.14s
      Round 6 - Avg Train Loss: 0.1000
      Round 6 - Avg Train Acc: 0.8078 - Time: 15.43s
      Round 7 - Avg Train Loss: 0.1000
      Round 7 - Avg Train Acc: 0.8130 - Time: 15.69s
      Round 8 - Avg Train Loss: 0.1000
      Round 8 - Avg Train Acc: 0.8146 - Time: 15.73s
      Round 9 - Avg Train Loss: 0.1000
      Round 9 - Avg Train Acc: 0.8172 - Time: 16.41s
      Round 10 - Avg Train Loss: 0.1000
      Round 10 - Avg Train Acc: 0.8192 - Time: 16.59s
      Round 11 - Avg Train Loss: 0.1000
      Round 11 - Avg Train Acc: 0.8239 - Time: 16.48s
      Round 12 - Avg Train Loss: 0.1000
      Round 12 - Avg Train Acc: 0.8267 - Time: 16.61s
      Round 13 - Avg Train Loss: 0.1000
      Round 13 - Avg Train Acc: 0.8321 - Time: 16.58s
      Round 14 - Avg Train Loss: 0.1000
      Round 14 - Avg Train Acc: 0.8304 - Time: 16.57s
      Round 15 - Avg Train Loss: 0.1000
      Round 15 - Avg Train Acc: 0.8358 - Time: 16.66s
      Round 16 - Avg Train Loss: 0.1000
      Round 16 - Avg Train Acc: 0.8394 - Time: 16.10s
      Round 17 - Avg Train Loss: 0.1000
      Round 17 - Avg Train Acc: 0.8402 - Time: 16.68s
      Round 18 - Avg Train Loss: 0.1000
      Round 18 - Avg Train Acc: 0.8429 - Time: 16.74s
      Round 19 - Avg Train Loss: 0.1000
      Round 19 - Avg Train Acc: 0.8443 - Time: 16.77s
      Round 20 - Avg Train Loss: 0.1000
      Round 20 - Avg Train Acc: 0.8447 - Time: 15.41s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 333.27s
   Captured 20 rounds of training metrics
   Avg time per round: 16.46s

Semua model berhasil dilatih dengan FedProx!

#### Evaluation Result

2025-12-17 04:33:28.992246: I external/local_xla/xla/service/service.cc:163] XLA service 0x7f462001bfb0 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2025-12-17 04:33:28.992259: I external/local_xla/xla/service/service.cc:171]   StreamExecutor device (0): NVIDIA GeForce GTX 1650 SUPER, Compute Capability 7.5
2025-12-17 04:33:28.996361: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:269] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.

EVALUASI SEMUA MODEL

--- EVALUASI MODEL BINARY ---

[1/4] MLP Binary...
2025-12-17 04:33:29.029315: I external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:473] Loaded cuDNN version 91600
I0000 00:00:1765920809.289537 1096826 device_compiler.h:196] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.

EVALUATION METRICS - MLP Binary (FedProx):

- Accuracy: 0.9561
- Precision: 0.9474
- Recall: 0.9978
- F1 Score: 0.9720
- AUC-ROC: 0.9934

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.82      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.95     42209

[2/4] CNN Binary...

EVALUATION METRICS - CNN Binary (FedProx):

- Accuracy: 0.9574
- Precision: 0.9486
- Recall: 0.9982
- F1 Score: 0.9728
- AUC-ROC: 0.9960

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.83      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.96     42209

--- EVALUASI MODEL MULTI-CLASS ---

[3/4] MLP Multi-class...

EVALUATION METRICS - MLP Multi (FedProx):

- Accuracy: 0.6976
- Precision: 0.7353
- Recall: 0.6976
- F1 Score: 0.6710
- AUC-ROC: 0.9614

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.48      0.99      0.65      4000
        ddos       0.95      0.90      0.92      4000
         dos       0.47      0.19      0.27      4000
   injection       0.73      0.08      0.14      4000
        mitm       0.00      0.00      0.00       209
      normal       0.97      0.82      0.89     10000
    password       0.45      0.74      0.56      4000
  ransomware       0.66      0.86      0.75      4000
    scanning       0.79      0.78      0.78      4000
         xss       0.81      0.77      0.79      4000

    accuracy                           0.70     42209
   macro avg       0.63      0.61      0.57     42209
weighted avg       0.74      0.70      0.67     42209

[4/4] CNN Multi-class...

EVALUATION METRICS - CNN Multi (FedProx):

- Accuracy: 0.7304
- Precision: 0.7724
- Recall: 0.7304
- F1 Score: 0.7143
- AUC-ROC: 0.9734

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.48      1.00      0.65      4000
        ddos       0.90      0.93      0.91      4000
         dos       0.51      0.21      0.30      4000
   injection       0.90      0.24      0.38      4000
        mitm       0.32      0.17      0.22       209
      normal       0.97      0.83      0.90     10000
    password       0.53      0.74      0.62      4000
  ransomware       0.68      0.91      0.78      4000
    scanning       0.83      0.77      0.80      4000
         xss       0.86      0.83      0.84      4000

    accuracy                           0.73     42209
   macro avg       0.70      0.66      0.64     42209
weighted avg       0.77      0.73      0.71     42209

---

#### 2. Batchsize 512 Epochs 1 Learning Rate 0.0005 Alpha Dirichlet 0.3 Mu 0.001

#### Round Result

MEMULAI PELATIHAN FEDERATED PROXIMAL (FEDPROX) DENGAN FLOWER
Proximal Term (μ) - Binary: 0.001, Multi-class: 0.001

--- PELATIHAN DETEKSI BINER DENGAN FEDPROX ---

Melatih Model MLP Binary...

[INFO] Starting Flower FedProx federated learning for mlp_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.001

I0000 00:00:1765918331.798499 1047538 gpu_device.cc:2020] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 2232 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1650 SUPER, pci bus id: 0000:07:00.0, compute capability: 7.5

      Round 1 - Avg Train Loss: 0.6526
      Round 1 - Avg Train Acc: 0.8408 - Time: 9.29s
      Round 2 - Avg Train Acc: 0.9666 - Time: 3.86s
      Round 3 - Avg Train Loss: 0.7965
      Round 3 - Avg Train Acc: 0.9676 - Time: 3.78s
      Round 4 - Avg Train Loss: 0.7953
      Round 4 - Avg Train Acc: 0.9682 - Time: 3.85s
      Round 5 - Avg Train Loss: 0.7950
      Round 5 - Avg Train Acc: 0.9695 - Time: 3.86s
      Round 6 - Avg Train Loss: 0.7964
      Round 6 - Avg Train Acc: 0.9705 - Time: 3.87s
      Round 7 - Avg Train Loss: 0.7954
      Round 7 - Avg Train Acc: 0.9712 - Time: 4.00s
      Round 8 - Avg Train Loss: 0.7991
      Round 8 - Avg Train Acc: 0.9710 - Time: 3.98s
      Round 9 - Avg Train Loss: 0.7998
      Round 9 - Avg Train Acc: 0.9708 - Time: 4.06s
      Round 10 - Avg Train Loss: 0.7980
      Round 10 - Avg Train Acc: 0.9718 - Time: 4.02s
      Round 11 - Avg Train Loss: 0.8000
      Round 11 - Avg Train Acc: 0.9720 - Time: 4.18s
      Round 12 - Avg Train Loss: 0.8001
      Round 12 - Avg Train Acc: 0.9720 - Time: 4.13s
      Round 13 - Avg Train Loss: 0.7987
      Round 13 - Avg Train Acc: 0.9720 - Time: 4.15s
      Round 14 - Avg Train Loss: 0.7986
      Round 14 - Avg Train Acc: 0.9720 - Time: 4.33s
      Round 15 - Avg Train Loss: 0.7984
      Round 15 - Avg Train Acc: 0.9723 - Time: 4.26s
      Round 16 - Avg Train Loss: 0.8000
      Round 16 - Avg Train Acc: 0.9722 - Time: 4.33s
      Round 17 - Avg Train Loss: 0.7993
      Round 17 - Avg Train Acc: 0.9722 - Time: 4.43s
      Round 18 - Avg Train Loss: 0.7984
      Round 18 - Avg Train Acc: 0.9723 - Time: 4.27s
      Round 19 - Avg Train Loss: 0.7993
      Round 19 - Avg Train Acc: 0.9723 - Time: 4.49s
      Round 20 - Avg Train Loss: 0.7996
      Round 20 - Avg Train Acc: 0.9725 - Time: 4.57s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 89.35s
   Captured 20 rounds of training metrics
   Avg time per round: 4.39s

Melatih Model CNN Binary...

[INFO] Starting Flower FedProx federated learning for cnn_binary...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.001

      Round 1 - Avg Train Loss: 0.5816
      Round 1 - Avg Train Acc: 0.7207 - Time: 15.51s
      Round 2 - Avg Train Loss: 0.8048
      Round 2 - Avg Train Acc: 0.9664 - Time: 8.01s
      Round 3 - Avg Train Loss: 0.8024
      Round 3 - Avg Train Acc: 0.9697 - Time: 9.46s
      Round 4 - Avg Train Loss: 0.8009
      Round 4 - Avg Train Acc: 0.9705 - Time: 7.90s
      Round 5 - Avg Train Loss: 0.7998
      Round 5 - Avg Train Acc: 0.9719 - Time: 8.38s
      Round 6 - Avg Train Loss: 0.8023
      Round 6 - Avg Train Acc: 0.9723 - Time: 8.01s
      Round 7 - Avg Train Loss: 0.8017
      Round 7 - Avg Train Acc: 0.9752 - Time: 8.03s
      Round 8 - Avg Train Loss: 0.8019
      Round 8 - Avg Train Acc: 0.9768 - Time: 8.34s
      Round 9 - Avg Train Loss: 0.8018
      Round 9 - Avg Train Acc: 0.9770 - Time: 9.57s
      Round 10 - Avg Train Loss: 0.8025
      Round 10 - Avg Train Acc: 0.9780 - Time: 8.24s
      Round 11 - Avg Train Loss: 0.8024
      Round 11 - Avg Train Acc: 0.9777 - Time: 8.47s
      Round 12 - Avg Train Loss: 0.8021
      Round 12 - Avg Train Acc: 0.9783 - Time: 8.39s
      Round 13 - Avg Train Loss: 0.8034
      Round 13 - Avg Train Acc: 0.9782 - Time: 8.73s
      Round 14 - Avg Train Loss: 0.8038
      Round 14 - Avg Train Acc: 0.9793 - Time: 8.71s
      Round 15 - Avg Train Loss: 0.8031
      Round 15 - Avg Train Acc: 0.9794 - Time: 8.39s
      Round 16 - Avg Train Loss: 0.8037
      Round 16 - Avg Train Acc: 0.9805 - Time: 8.49s
      Round 17 - Avg Train Loss: 0.8011
      Round 17 - Avg Train Acc: 0.9800 - Time: 8.48s
      Round 18 - Avg Train Loss: 0.8039
      Round 18 - Avg Train Acc: 0.9795 - Time: 9.02s
      Round 19 - Avg Train Loss: 0.8028
      Round 19 - Avg Train Acc: 0.9814 - Time: 8.74s
      Round 20 - Avg Train Loss: 0.8029
      Round 20 - Avg Train Acc: 0.9806 - Time: 8.60s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 179.98s
   Captured 20 rounds of training metrics
   Avg time per round: 8.87s

--- PELATIHAN KLASIFIKASI MULTI-KELAS DENGAN FEDPROX ---

Melatih Model MLP Multi-class...

[INFO] Starting Flower FedProx federated learning for mlp_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.001

      Round 1 - Avg Train Loss: 0.1000
      Round 1 - Avg Train Acc: 0.6833 - Time: 11.02s
      Round 2 - Avg Train Loss: 0.1000
      Round 2 - Avg Train Acc: 0.7750 - Time: 4.76s
      Round 3 - Avg Train Loss: 0.1000
      Round 3 - Avg Train Acc: 0.7873 - Time: 4.86s
      Round 4 - Avg Train Loss: 0.1000
      Round 4 - Avg Train Acc: 0.7941 - Time: 4.78s
      Round 5 - Avg Train Loss: 0.1000
      Round 5 - Avg Train Acc: 0.7988 - Time: 4.74s
      Round 6 - Avg Train Loss: 0.1000
      Round 6 - Avg Train Acc: 0.8014 - Time: 4.92s
      Round 7 - Avg Train Loss: 0.1000
      Round 7 - Avg Train Acc: 0.8042 - Time: 4.88s
      Round 8 - Avg Train Loss: 0.1000
      Round 8 - Avg Train Acc: 0.8050 - Time: 5.12s
      Round 9 - Avg Train Loss: 0.1000
      Round 9 - Avg Train Acc: 0.8065 - Time: 5.04s
      Round 10 - Avg Train Loss: 0.1000
      Round 10 - Avg Train Acc: 0.8077 - Time: 4.94s
      Round 11 - Avg Train Loss: 0.1000
      Round 11 - Avg Train Acc: 0.8097 - Time: 5.00s
      Round 12 - Avg Train Loss: 0.1000
      Round 12 - Avg Train Acc: 0.8123 - Time: 5.08s
      Round 13 - Avg Train Loss: 0.1000
      Round 13 - Avg Train Acc: 0.8121 - Time: 5.07s
      Round 14 - Avg Train Loss: 0.1000
      Round 14 - Avg Train Acc: 0.8121 - Time: 5.07s
      Round 15 - Avg Train Loss: 0.1000
      Round 15 - Avg Train Acc: 0.8146 - Time: 5.21s
      Round 16 - Avg Train Loss: 0.1000
      Round 16 - Avg Train Acc: 0.8161 - Time: 5.16s
      Round 17 - Avg Train Loss: 0.1000
      Round 17 - Avg Train Acc: 0.8157 - Time: 6.21s
      Round 18 - Avg Train Loss: 0.1000
      Round 18 - Avg Train Acc: 0.8178 - Time: 6.03s
      Round 19 - Avg Train Loss: 0.1000
      Round 19 - Avg Train Acc: 0.8187 - Time: 6.10s  
      Round 20 - Avg Train Loss: 0.1000
      Round 20 - Avg Train Acc: 0.8188 - Time: 6.24s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 111.97s
   Captured 20 rounds of training metrics
   Avg time per round: 5.51s

 Melatih Model CNN Multi-class...

[INFO] Starting Flower FedProx federated learning for cnn_multi...
   Clients: 5 | Rounds: 20 | Local epochs: 1
   Proximal term (μ): 0.001

      Round 1 - Avg Train Loss: 0.1000
      Round 1 - Avg Train Acc: 0.6901 - Time: 20.17s
      Round 2 - Avg Train Loss: 0.1000
      Round 2 - Avg Train Acc: 0.7547 - Time: 14.63s
      Round 3 - Avg Train Loss: 0.1000
      Round 3 - Avg Train Acc: 0.7778 - Time: 15.41s
      Round 4 - Avg Train Loss: 0.1000
      Round 4 - Avg Train Acc: 0.7883 - Time: 13.87s
      Round 5 - Avg Train Acc: 0.7937 - Time: 14.55s
      Round 6 - Avg Train Loss: 0.1000
      Round 6 - Avg Train Acc: 0.7981 - Time: 14.64s
      Round 7 - Avg Train Loss: 0.1000
      Round 7 - Avg Train Acc: 0.8017 - Time: 16.22s
      Round 8 - Avg Train Loss: 0.1000
      Round 8 - Avg Train Acc: 0.8071 - Time: 16.50s
      Round 9 - Avg Train Loss: 0.1000
      Round 9 - Avg Train Acc: 0.8118 - Time: 16.38s
      Round 10 - Avg Train Loss: 0.1000
      Round 10 - Avg Train Acc: 0.8161 - Time: 16.55s
      Round 11 - Avg Train Loss: 0.1000
      Round 11 - Avg Train Acc: 0.8219 - Time: 16.55s
      Round 12 - Avg Train Loss: 0.1000
      Round 12 - Avg Train Acc: 0.8269 - Time: 16.54s
      Round 13 - Avg Train Loss: 0.1000
      Round 13 - Avg Train Acc: 0.8271 - Time: 16.08s
      Round 14 - Avg Train Loss: 0.1000
      Round 14 - Avg Train Acc: 0.8277 - Time: 15.98s
      Round 15 - Avg Train Loss: 0.1000
      Round 15 - Avg Train Acc: 0.8342 - Time: 16.77s
      Round 16 - Avg Train Loss: 0.1000
      Round 16 - Avg Train Acc: 0.8380 - Time: 16.94s
      Round 17 - Avg Train Loss: 0.1000
      Round 17 - Avg Train Acc: 0.8404 - Time: 16.82s
      Round 18 - Avg Train Loss: 0.1000
      Round 18 - Avg Train Acc: 0.8433 - Time: 15.32s
      Round 19 - Avg Train Loss: 0.1000
      Round 19 - Avg Train Acc: 0.8453 - Time: 14.76s
      Round 20 - Avg Train Loss: 0.1000
      Round 20 - Avg Train Acc: 0.8474 - Time: 16.97s
   ✓ Model weights updated from FedProx training

FedProx federated learning completed in 325.66s
   Captured 20 rounds of training metrics
   Avg time per round: 16.08s

Semua model berhasil dilatih dengan FedProx!

#### Evaluation Result

2025-12-17 04:03:59.893671: I external/local_xla/xla/service/service.cc:163] XLA service 0x7fce440016d0 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2025-12-17 04:03:59.893685: I external/local_xla/xla/service/service.cc:171]   StreamExecutor device (0): NVIDIA GeForce GTX 1650 SUPER, Compute Capability 7.5
2025-12-17 04:03:59.897871: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:269] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.

EVALUASI SEMUA MODEL

--- EVALUASI MODEL BINARY ---

[1/4] MLP Binary...
2025-12-17 04:03:59.931021: I external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:473] Loaded cuDNN version 91600
I0000 00:00:1765919040.192349 1047726 device_compiler.h:196] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.

EVALUATION METRICS - MLP Binary (FedProx):

- Accuracy: 0.9562
- Precision: 0.9474
- Recall: 0.9980
- F1 Score: 0.9720
- AUC-ROC: 0.9932

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.82      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.95     42209

[2/4] CNN Binary...

EVALUATION METRICS - CNN Binary (FedProx):

- Accuracy: 0.9578
- Precision: 0.9491
- Recall: 0.9983
- F1 Score: 0.9731
- AUC-ROC: 0.9959

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

      Normal       0.99      0.83      0.90     10000
      Attack       0.95      1.00      0.97     32209

    accuracy                           0.96     42209
   macro avg       0.97      0.91      0.94     42209
weighted avg       0.96      0.96      0.96     42209

--- EVALUASI MODEL MULTI-CLASS ---

[3/4] MLP Multi-class...

EVALUATION METRICS - MLP Multi (FedProx):

- Accuracy: 0.6686
- Precision: 0.6868
- Recall: 0.6686
- F1 Score: 0.6317
- AUC-ROC: 0.9578

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.00      0.00      0.00      4000
        ddos       0.95      0.89      0.92      4000
         dos       0.35      0.89      0.51      4000
   injection       0.79      0.08      0.14      4000
        mitm       0.67      0.01      0.02       209
      normal       0.97      0.83      0.89     10000
    password       0.44      0.72      0.55      4000
  ransomware       0.66      0.86      0.75      4000
    scanning       0.78      0.78      0.78      4000
         xss       0.81      0.77      0.79      4000

    accuracy                           0.67     42209
   macro avg       0.64      0.58      0.53     42209
weighted avg       0.69      0.67      0.63     42209

[4/4] CNN Multi-class...

EVALUATION METRICS - CNN Multi (FedProx):

- Accuracy: 0.6937
- Precision: 0.7924
- Recall: 0.6937
- F1 Score: 0.6547
- AUC-ROC: 0.9760

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    backdoor       0.87      0.01      0.01      4000
        ddos       0.89      0.94      0.92      4000
         dos       0.37      0.95      0.54      4000
   injection       0.86      0.08      0.15      4000
        mitm       0.37      0.25      0.30       209
      normal       0.96      0.83      0.89     10000
    password       0.47      0.74      0.58      4000
  ransomware       0.72      0.91      0.80      4000
    scanning       0.83      0.78      0.80      4000
         xss       0.92      0.83      0.87      4000

    accuracy                           0.69     42209
   macro avg       0.73      0.63      0.59     42209
weighted avg       0.79      0.69      0.65     42209

---
