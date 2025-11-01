import pandas as pd
import requests
response = requests.get("http://localhost:8000/logs")
logs = response.json()

# Create a DataFrame to analyze results
df = pd.DataFrame(logs)
print(df)
# Filter only entries with true_label
df = df[df['true_label'].notnull()]

# Compute accuracy per model
accuracy = df.groupby('model').apply(lambda x: (x['prediction'] == x['true_label']).mean())

print(accuracy)
