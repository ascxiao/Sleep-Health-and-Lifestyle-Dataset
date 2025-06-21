from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from modules import dataset
import pandas as pd

df = dataset.sleep_transformed

sleep_encoded = pd.get_dummies(df, drop_first=True)

corr_matrix = df.select_dtypes(include='number').corr()

# Prepare data
X = sleep_encoded.drop(columns=['Quality of Sleep (scale: 1-10)'])
y = sleep_encoded['Quality of Sleep (scale: 1-10)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Get feature importance

def importance(x):
    importances = pd.Series(model.feature_importances_, index=X.columns)
    importances = importances.sort_values(ascending=False).head(x)
    return importances