import os
import pandas as pd
import numpy as np

os.makedirs('datasets', exist_ok=True)

# 1. Housing Prices (Regression)
np.random.seed(42)
size = 200
sqft = np.random.normal(1500, 500, size)
beds = np.random.randint(1, 6, size)
baths = np.random.randint(1, 4, size)
# Price = 150*sqft + 10000*beds + 5000*baths + noise
price = 150 * sqft + 10000 * beds + 5000 * baths + np.random.normal(0, 20000, size)
df_housing = pd.DataFrame({'SqFt': sqft, 'Bedrooms': beds, 'Bathrooms': baths, 'Price': price})
df_housing.to_csv('datasets/housing.csv', index=False)

# 2. Medical Records (KNN Classification)
heart_rate = np.random.normal(75, 15, size)
blood_pressure = np.random.normal(120, 20, size)
disease = (heart_rate + blood_pressure > 200).astype(int)
df_medical = pd.DataFrame({'HeartRate': heart_rate, 'BloodPressure': blood_pressure, 'Disease': disease})
df_medical.to_csv('datasets/medical.csv', index=False)

# 3. Emails (Naive Bayes Text Classification)
emails = [
    "Win a million dollars now!",
    "Meeting agenda for tomorrow",
    "URGENT: Account locked, please click here",
    "Can we reschedule our lunch?",
    "Buy cheap pills online",
    "Here is the project report you requested",
    "Claim your free vacation today",
    "Happy birthday! Hope you have a great day"
]
labels = [1, 0, 1, 0, 1, 0, 1, 0] # 1 = Spam, 0 = Ham
df_emails = pd.DataFrame({'Text': emails * 25, 'Spam': labels * 25})
df_emails.to_csv('datasets/emails.csv', index=False)

print("Generated toy datasets in datasets/ directory.")