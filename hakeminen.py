import requests as re
import pandas as pd

r = re.get("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=74")
print(r.text)

url = "http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=74"
csv = pd.read_csv(url, delimiter=';')
csv.to_csv('groupid74data.csv')
