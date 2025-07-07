import pandas as pd
from datetime import datetime, timedelta

# Step 1: Define start date and total days
start_date = datetime.today()
days = 30

# Step 2: Create placeholder content
calendar_data = []
for i in range(days):
    day = start_date + timedelta(days=i)
    calendar_data.append({
        "Date": day.strftime('%Y-%m-%d'),
        "Post Idea": f"Post idea for day {i+1}",
        "Caption": f"This is the caption for day {i+1}",
        "Hashtags": "#brand #socialmedia #day" + str(i+1),
        "Image Idea": f"Image related to topic {i+1}"
    })

# Step 3: Create DataFrame
df = pd.DataFrame(calendar_data)

# Step 4: Save to Excel
df.to_excel("social_media_calendar.xlsx", index=False)
print("✅ Calendar created as 'social_media_calendar.xlsx'")