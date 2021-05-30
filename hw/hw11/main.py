from queue import Queue
from bs4 import BeautifulSoup as bs
import requests
import pickle
import re

# for i in soup.find_all('a'):
#     urls.put(i.text)
#     if urls.qsize() == 10:
#         break

# for i in range(urls.qsize()):
#     print(urls.get())

connects = []
domains = set()
data = Queue()
already = []

home = 'https://vc.ru/design/105158-20-krutyh-saytov-2020-goda-dlya-vdohnoveniya'
response = requests.get(home)
soup = bs(response.text, 'lxml')
pages = [elm['href'].replace('https://', '') for elm in soup.find_all('a', attrs={'href': True})]

# time = [re.findall(r"[\w*\W]*[?]|[\w*\W]*", i)[0]for i in pages if 'https' in i]
# #\w*\W*\w*\Wru\W|\w*\W*\w*\Wcom\W|\w*\W*\w*\Wnet\W"  #domains

for i in range(len(pages)):
    if re.findall(r"[\w*\W]*[?]|[\w*\W]*", pages[i])[0].replace('?', '') not in already:
        data.put(pages[i])
        already.append(re.findall(r"[\w*\W]*[?]|[\w*\W]*", pages[i])[0].replace('?', ''))
        domains.update(re.findall(r"[\w+\W]+ru\/|[\w+\W]+\net\/|[\w+\W]+com\/|[\w+\W]+co\/|[\w+\W]+net\/|[\w+\W]+world\/|[\w+\W]+jp\/", pages[i]))
    if data.qsize() == 10:
        break
# print(already)
# print(domains)

# now we can start

while data.qsize() < 1000:
    temp = data.get()
    print(home := 'https://' + temp)
    try:
        response = requests.get(home)
        soup = bs(response.text, 'lxml')
        pages = [elm['href'].replace('https://', '') for elm in soup.find_all('a', attrs={'href': True})]
        for i in range(len(pages)):
            if (now := re.findall(r"[\w*\W]*[?]|[\w*\W]*", pages[i])[0].replace('?', '')) not in already:
                data.put(pages[i])
                already.append(now)
                connects.append({re.findall(r"[\w*\W]*[?]|[\w*\W]*", temp)[0].replace('?', ''), now})
                domains.update(re.findall(r"[\w+\W]+ru\/|[\w+\W]+\net\/|[\w+\W]+com\/|[\w+\W]+co\/|[\w+\W]+net\/|[\w+\W]+world\/|[\w+\W]+jp\/", pages[i]))
            if data.qsize() > 999:
                break
    except Exception:
        pass
print(data.qsize())
print(domains)
print(connects)
pickle.dump(domains, open("domains.pickle", "wb"))
pickle.dump(connects, open("connects.pickle", "wb"))