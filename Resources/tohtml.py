import pandas as pd
columns = ["City_ID","City","Cloudiness","Country","Date","Humidity","Lat","Lng","Max Temp","Wind Speed"]
df = pd.read_csv('cities.csv', names=columns)
print(df.to_html())