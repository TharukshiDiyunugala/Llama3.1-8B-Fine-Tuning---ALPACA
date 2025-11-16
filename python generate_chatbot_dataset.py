import json
import random

# Define products and attributes
products = {
    "earbuds": {"price": 5000, "colors": ["black", "white"], "warranty": "6 months"},
    "headphones": {"price": 2500, "colors": ["black", "silver", "red"], "warranty": "1 year"},
    "smartphones": {"price": 60000, "colors": ["black", "blue", "white"], "warranty": "1 year"},
    "chargers": {"price": 800, "colors": ["black", "white"], "warranty": "6 months"},
    "power banks": {"price": 1500, "colors": ["black", "grey"], "warranty": "6 months"},
    "laptops": {"price": 70000, "colors": ["silver", "black"], "warranty": "1 year"},
    "washing machines": {"price": 55000, "colors": ["white", "silver"], "warranty": "2 years"},
    "TVs": {"price": 40000, "colors": ["black"], "warranty": "2 years"},
    "printers": {"price": 12000, "colors": ["white", "black"], "warranty": "1 year"},
    "fridges": {"price": 65000, "colors": ["silver", "white"], "warranty": "2 years"},
    "smartwatches": {"price": 12000, "colors": ["black", "silver"], "warranty": "1 year"},
    "rice cookers": {"price": 2500, "colors": ["white"], "warranty": "6 months"},
    "air conditioners": {"price": 80000, "colors": ["white"], "warranty": "2 years"},
    "dresses": {"price": 3000, "colors": ["red", "blue", "black"], "warranty": "N/A"},
    "shoes": {"price": 4000, "colors": ["black", "brown", "white"], "warranty": "N/A"},
    "bags": {"price": 2500, "colors": ["black", "brown"], "warranty": "6 months"}
}

# Possible questions
questions = [
    "how much {}?",
    "is {} available?",
    "what colors does {} come in?",
    "tell me about {} warranty",
    "how long will {} take for delivery?",
    "do you have {} in stock?",
    "can you tell me the features of {}?"
]

# Number of samples
num_samples = 2000

# Generate dataset
samples = []
for _ in range(num_samples):
    product = random.choice(list(products.keys()))
    question = random.choice(questions).format(product)
    
    if "how much" in question:
        answer = f"The {product} costs {products[product]['price']} rupees. Do you want me to check availability?"
    elif "available" in question or "in stock" in question:
        answer = f"Yes, the {product} is in stock in {', '.join(products[product]['colors'])}."
    elif "colors" in question:
        answer = f"The {product} comes in {', '.join(products[product]['colors'])}."
    elif "warranty" in question:
        answer = f"The {product} has a warranty of {products[product]['warranty']}."
    elif "delivery" in question:
        answer = f"The {product} can be delivered within 3-5 business days."
    elif "features" in question:
        answer = f"The {product} has high quality and reliable features suitable for daily use."
    else:
        answer = f"I can check about the {product} for you."
    
    samples.append({"messages":[{"role":"user","content":question},{"role":"assistant","content":answer}]})

# Save to JSONL file
with open("chatbot_conversational_dataset_2000.jsonl", "w", encoding="utf-8") as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

print("✅ Dataset generated and saved as 'chatbot_conversational_dataset_2000.jsonl'")
