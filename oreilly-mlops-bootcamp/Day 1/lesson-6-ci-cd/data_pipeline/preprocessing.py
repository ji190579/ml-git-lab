import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import seaborn as sns 
import matplotlib.pyplot as plt

def load_and_preprocess_data():
    columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race",
        "sex", "capital-gain", "capital-loss", "hours-per-week",
        "native-country", "income"
    ]

    # Load datasets
    data = pd.read_csv("data/adult.data", header=None, names=columns, na_values=" ?")
    # print(data.head)
    
    # Remove duplicates
    data.drop_duplicates(inplace=True)
    # print(f"Number of rows after removing duplicates: {data.shape[0]}")
    
    # Impute missing values
    missing_cols = ["workclass", "occupation", "native-country"]
    imputer = SimpleImputer(strategy="most_frequent")
    data[missing_cols] = imputer.fit_transform(data[missing_cols])
    
    # Verify missing values are handled
    # print("\nMissing Values After Imputation:")
    # print(data.isnull().sum())
    
    # Encode target variables
    data["income"] = data["income"].map({" <=50K": 0, " >50K": 1})
    
    #Visualize class distribution
    # plt.figure(figsize=(8, 5))
    # sns.countplot(data=data, x="income", palette="viridis")
    # plt.title("Class Distribution")
    # plt.show()

    # Features and target
    X = data.drop("income", axis=1)
    y = data["income"]

    # Identify numerical and categorical columns
    num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = ["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "native-country"]

    # Preprocessing pipeline
    num_transformer = Pipeline(steps=[("scaler", StandardScaler())])
    cat_transformer = Pipeline(steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))])
    preprocessor = ColumnTransformer(transformers=[
        ("num", num_transformer, num_cols),
        ("cat", cat_transformer, cat_cols)
    ])

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

    # Apply transformations
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # Balance the dataset using SMOTE
    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    
    # Verify that the class distribution is balanced in the training data
    # print(f"Class distribution in training data after SMOTE: {y_train_res.value_counts()}")

    # Visualize class distribution after SMOTE (in the resampled training set)
    # plt.figure(figsize=(8, 5))
    # sns.countplot(x=y_train_res)
    # plt.title("Class Distribution After SMOTE")
    # plt.xlabel("Class")
    # plt.ylabel("Count")
    # plt.tight_layout()
    # plt.show()

    return X_train_res, X_test, y_train_res, y_test, preprocessor

# Run the preprocessing function

if __name__ == "__main__":
    load_and_preprocess_data()
