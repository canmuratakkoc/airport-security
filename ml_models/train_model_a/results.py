import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")
plt.plot(df.epoch, df["metrics/mAP50(B)"], label="mAP@50")
plt.plot(df.epoch, df["metrics/mAP50-95(B)"], label="mAP@50-95")
plt.legend(), plt.xlabel("Epoch"), plt.ylabel("mAP")
plt.show()
