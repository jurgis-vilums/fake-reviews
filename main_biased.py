import pandas as pd
import random
from datetime import datetime, timedelta

# Number of responses to generate
num_responses = 100

# Possible answers
roles = [
    "Cosmetology specialist", "Massage professional", "Cosmetics brand owner",
    "Beauty studio manager/administrator", "Individual consumer", "Other, please specify"
]
brands = ["Brand A", "Brand B", "Brand C", "Brand D", "Brand E"]
discovery_methods = [
    "At an exhibition", "At educational courses", "From colleagues", "At your workplace",
    "From clients", "From a family member", "Through an internet search",
    "Via an internet advertisement", "Via a social media advertisement", 
    "Through an email newsletter", "Word of mouth", "Shelf or poster ad at the shop",
    "Friends", "School/college", "Other, please specify"
]
marketing_channels = [
    "Email", "Instagram", "Linkedin", "TikTok", "Visiting the website", 
    "Phone calls to the sales manager", "Visits to a physical store", 
    "Through colleagues/bosses", "I do not follow any"
]
stop_causes = [
    "Products becoming widely available in shops", "Reduced support from sales manager", 
    "Absence of new product lines", "New product lines lacking a unique sales proposition", 
    "Lack of educational seminars supporting new products", 
    "Brand not recognized or preferred by clients", "Dissatisfaction with products among clients", 
    "Product-based procedures becoming less profitable", 
    "Moving to another country where the brand is unknown", 
    "Ethical or financial scandals associated with the brand or personnel", 
    "Slow or poor product delivery", "Receiving spoiled or damaged products"
]

# Function to generate random responses with tendencies
def generate_responses(num):
    data = []
    for _ in range(num):
        timestamp = datetime.now() - timedelta(days=random.randint(0, 365))
        role = random.choices(roles, weights=[1, 1, 1, 1, 4, 1])[0]  # Bias toward "Individual consumer"
        brand = random.choices(brands, weights=[4, 1, 1, 1, 1])[0]  # Bias toward "Brand A"
        years_using = random.randint(0, 30)
        discovery = random.choice(discovery_methods)
        channels_followed = ', '.join(random.sample(marketing_channels, random.randint(1, len(marketing_channels))))
        personal_use = random.choice(["Yes", "No"])
        familiar_product_line = f"Product Line {random.randint(1, 5)}"
        causes_to_stop = ', '.join(random.sample(stop_causes, random.randint(1, len(stop_causes))))
        issues_encountered = random.randint(0, 5)
        loyalty = random.randint(1, 10)
        online_store_usage = random.choice(["Yes", "No"])
        quarterly_spend = random.randint(50, 1000)
        
        row = {
            "Timestamp": timestamp.strftime("%d/%m/%Y %H:%M:%S"),
            "Role in Cosmetics Industry": role,
            "Cosmetic Brand Used Most Frequently": brand,
            "Years Using Brand": years_using,
            "Learned About Brand": discovery,
            "Marketing Channels Followed": channels_followed,
            "Personal Use at Home": personal_use,
            "Most Familiar Product Line": familiar_product_line,
            "Potential Causes to Stop Using Brand": causes_to_stop,
            "Issues Encountered": issues_encountered,
            "Loyalty": loyalty,
            "Use Online Store": online_store_usage,
            "Average Quarterly Spend": quarterly_spend
        }
        
        data.append(row)
    
    return data

# Generate responses and create a DataFrame
responses = generate_responses(num_responses)
df = pd.DataFrame(responses)
# print(df.to_string())


# Save the DataFrame to a CSV file
df.to_csv("biased_fake_responses.csv", index=False)
