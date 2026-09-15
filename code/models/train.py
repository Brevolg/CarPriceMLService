import pandas as pd
import joblib
import mlflow

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

train = pd.read_csv("../../data/processed/train.csv")
test = pd.read_csv("../../data/processed/test.csv")

features = [
    "make_year",
    "engine_capacity(CC)",
    "km_driven"
]

target = "price"

X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]

models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
}

best_model = None
best_mae = float("inf")

mlflow.set_experiment("car_price_prediction")

for name, model in models.items():
    print("Training", name)
    
    with mlflow.start_run(run_name=name):
        model.fit(
            X_train,
            y_train
        )
        
        predictions = model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        print("MAE", mae)
        print("R2", r2)

        mlflow.log_metric("MAE",mae)
        mlflow.log_metric("R2",r2)
        mlflow.sklearn.log_model(model,name)

        if mae < best_mae:
            best_mae = mae
            best_model = model

joblib.dump(best_model,"../../models/model.pkl")
print("done")