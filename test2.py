import requests
import re
import sys

args = sys.argv

r = requests.get(args[1])

title = re.findall('<title>.+</title>', r.text)
title = title[0].replace('<title>', '').replace('</title>', '').split()
title = ''.join(title[:-3])

sfen_list = re.findall('"sfen":"\S+\s[b|w]\s\S+\s[0-9]+"', r.text)
sfen_list = [x.replace('"', '').replace('sfen:', '') for x in sfen_list]
new_list = list(dict.fromkeys(sfen_list))

with open(title + '.txt', "w") as f:
    f.write('\n'.join(new_list))