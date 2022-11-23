import requests as re
import pandas as pd

r = re.get("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=74")
print(r.text) [:200] #printtaa ensimmäiset 200 sanaa ylemmästä sivusta

kantatieto = pd.DataFrame(r.text)
kantatieto.to_csv

#http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=XXX

#"https://tl.oamk.fi/tietoliikenteen_sovellusprojekti/" tää toimii