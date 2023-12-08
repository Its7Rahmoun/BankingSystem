from faker import Faker
import random
import string
import pandas as pd

# Set up Faker for human usernames
fake = Faker()

# Function to generate human usernames
def generate_human_username():
    return fake.user_name()

# Function to generate AI-generated usernames
def generate_ai_username(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Number of samples for each class
num_samples = 10000

# Generate human usernames
human_usernames = [generate_human_username() for _ in range(num_samples)]

# Generate AI-generated usernames
ai_usernames = [generate_ai_username() for _ in range(num_samples)]

# Create a DataFrame
data = pd.DataFrame({
    'Username': human_usernames + ai_usernames,
    'Label': [0] * num_samples + [1] * num_samples  # 0 for human, 1 for AI
})

# Shuffle the DataFrame
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the dataset to a CSV file
data.to_csv('username_dataset.csv', index=False)
