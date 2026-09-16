import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("data/raw/pre-owned cars.csv")
print(df.columns)
df = df.dropna()

df = df[df["price"] > 0]
df = df[df["make_year"] >= 1990]


features = [
    "make_year",
    "engine_capacity(CC)",
    "km_driven"
]

target = "price"
data = df[features + [target]]

train, test = train_test_split(
    data,
    test_size=0.2,
    random_state=42
)

print("Train size", train.shape)
print("Test size", test.shape)

train.to_csv("data/processed/train.csv", index=False)
test.to_csv("data/processed/test.csv", index=False)