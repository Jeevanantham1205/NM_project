from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 1. Load example dataset (Iris dataset)
data = load_iris()
X = data.data          # features
y = data.target        # labels

# 2. Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Define a pipeline (scaling + SVM classifier)
pipe = Pipeline([
    ('scaler', StandardScaler()),  # feature scaling
    ('svc', SVC(kernel='linear', random_state=42))  # SVM classifier
])

# 4. Train the pipeline
pipe.fit(X_train, y_train)

# 5. Make predictions on the test set
y_pred = pipe.predict(X_test)

# 6. Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2f}")
