import pandas as pd
import random
from datetime import datetime, timedelta

# Number of responses to generate
num_responses = 124

# Possible answers
roles = [
    "Cosmetology specialist", "Massage professional", "Cosmetics brand owner",
    "Beauty studio manager/administrator", "Non professional"
]
brands = ["Brand A", "Brand B", "Brand C", "Brand D", "Brand E", "Brand F", "Brand G", "Brand H"]
discovery_methods = [
    "At exhibition", "From colleagues", "At workplace",
    "From clients", "From family member", "Own internet search",
    "Internet advertisement", "Social media advertisement", 
    "Email newsletter", "Word of mouth", "On the store shelf or poster", "School/college"
]
marketing_channels = [
    "Email", "Instagram", "Facebook", "TikTok", "By visiting Website", 
    "Call to sales manager", "Visit Physical store", "Seminars", 
    "Through colleagues/bosses", "I do not"
]
stop_causes = [
    "It’s products has become available in shops for customers", "Less support by sales manager", 
    "Apsense of new product lines", "New product lines lacking unique sales proposition", 
    "Apsense of educational seminars supporting new product lines", 
    "Clients not recognising the brand/preferring other brand", "Client open dissatisfaction with product", 
    "Product line based procedures become less profitable", 
    "Moving to other country where clients do not know the brand", 
    "Ethical or financial scandal linked with mentioned brand or personnel", 
    "Slow or bad delivery of products", "Spoiled product or damaged packaging with further replacement"
]

# Function to generate random responses with tendencies
def generate_responses(num):
    data = []
    for _ in range(num):
        role = random.choices(roles, weights=[30, 20, 0, 3, 20])[0]
        brand = random.choices(brands, weights=[2, 6, 3, 3, 1, 1, 1, 1])[0]
        years_using = max(0, min(30, int(random.gauss(7, 4))))
        discovery = random.choices(discovery_methods, weights=[20,45,5,2,4,14,5,6,12,8,17,10])[0]
        
        # Generate multiple channels and join them as a single string
        num_channels = max(1, min(9, int(random.gauss(2, 3))))
        channels_followed = ', '.join(random.choices(marketing_channels, weights=[15, 45, 55, 5, 60, 20, 10, 13, 0], k=num_channels))

        personal_use = random.choices(["Yes", "No"], weights=[3, 1])[0]

        familiar_product_line = f"Product Line {random.randint(1, 5)}"

        # Randomly generate causes to stop using
        causes_to_stop = ', '.join(random.choices(stop_causes, weights=[5, 10, 3, 5, 7, 1, 14, 9, 8, 12, 6, 8], k=max(1, min(12, int(random.gauss(5, 4))))))
        
        issues_encountered = max(0, min(5, int(random.gauss(0, 1))))
        loyalty = max(0, min(10, int(random.gauss(7, 3))))
        online_store_usage = random.choices(["Yes", "No"], weights=[20, 15])[0]
        quarterly_spend = max(50, min(1000, int(random.gauss(300, 100))))

        row = {
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


responses = generate_responses(num_responses)
df = pd.DataFrame(responses)

df.to_csv("biased_fake_responses.csv", index=False)
