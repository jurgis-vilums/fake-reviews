import pandas as pd
import random
from datetime import datetime, timedelta
from plot_data_fn import plot_data

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
        role = random.choices(roles, weights=[1, 1, 1, 1, 4, 1])[0]
        brand = random.choices(brands, weights=[4, 1, 1, 1, 1])[0]
        years_using = max(0, min(30, int(random.gauss(6, 4))))
        discovery = random.choices(discovery_methods, weights=[1,2,3,4,5,14,5,6,12,8,5,10,4,14,3])[0]
        
        # Generate multiple channels and join them as a single string
        num_channels = max(1, min(9, int(random.gauss(6, 4))))
        channels_followed = ', '.join(random.choices(marketing_channels, weights=[1, 1, 1, 1, 4, 1, 1, 1, 1], k=num_channels))

        personal_use = random.choices(["Yes", "No"], weights=[3, 1])[0]

        familiar_product_line = f"Product Line {random.randint(1, 5)}"

        # Randomly generate causes to stop using
        causes_to_stop = ', '.join(random.choices(stop_causes, weights=[1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1], k=max(1, min(12, int(random.gauss(6, 4))))))
        
        issues_encountered = max(0, min(5, int(random.gauss(3, 1))))
        loyalty = max(0, min(10, int(random.gauss(7, 2))))
        online_store_usage = random.choices(["Yes", "No"], weights=[4, 1])[0]
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

plot_data(df, 'Role in Cosmetics Industry')  # To plot only the 'Years Using Brand'
# plot_data(df, 'all') 

df.to_csv("biased_fake_responses.csv", index=False)
