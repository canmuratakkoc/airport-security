from ultralytics import YOLO

# 1. Eğitilmiş modelinizi yükleyin
model = YOLO('weights/best.pt')

# 2. Validasyon isteğini gönderin; bu hem confusion matrix
#    hem de per-class metrikleri oluşturacaktır
res = model.val(
    data='data.yaml',   # kendi data.yaml yolun
    batch=16,           # istersen batch boyutunu da belirle
    imgsz=640,          # istersen resim boyutunu da
    save_conf=True,     # confusion matrix’i kaydet
    save_json=True      # per-class metrikleri metrics.json’a yaz
)

# 3. Sonuç objesinden sınıf bazlı metrikleri çekin
names = res.names          # {0:'Gun', 1:'Knife', …}
metrics = res.metrics      # shape = (n_metrics, n_classes)
# metrics[0] = precision per class
# metrics[1] = recall per class
# metrics[2] = mAP@0.5 per class
# metrics[3] = F1 per class  (versiyona göre değişebilir)

# 4. Basit bir tablo çıktısı almak istersen:
print("Class\tPrecision\tRecall\tF1")
for i, cls in names.items():
    p = metrics[0][i]
    r = metrics[1][i]
    f1= metrics[3][i]
    print(f"{cls}\t{p:.3f}\t\t{r:.3f}\t{f1:.3f}")
