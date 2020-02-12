import pandas as pd
import io
import requests

url="https://download.geonames.org/export/dump/timeZones.txt"
s=requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), sep='\t')

df_renamed = df.rename(
    columns={
        "CountryCode": "country_code",
        "TimeZoneId": "timezone_id",
        "GMT offset 1. Jan 2020": "gmt_offset",
        "DST offset 1. Jul 2020": "dst_offset",
        "rawOffset (independant of DST)": "raw_offset"
    }
)

df_renamed.to_csv("geonames_timezone.csv", index=False)
df_renamed.to_json("geonames_timezone.json", orient="records")

print(df_renamed.country_code.nunique())