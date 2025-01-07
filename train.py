import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load your dataset
data = pd.read_csv("data/fetal_health.csv")
X = data.drop("fetal_health", axis=1)
y = data["fetal_health"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a new model
model = RandomForestClassifier(n_estimators=200, max_depth=None, random_state=42)
model.fit(X_train, y_train)

# Save the model
# joblib.dump(model, "models/optimized_fetal_health_model2.pkl")
joblib.dump({"model": model, "feature_names": X.columns.tolist()}, "models/optimized_fetal_health_model.pkl")
