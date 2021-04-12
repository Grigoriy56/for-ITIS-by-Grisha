def do(text):
    text = text.lower()
    text = text.split(' ')
    fin = []
    for i in text:
        if len(i) > 5 and 'w' in i and 'a' in i and 'z' in i and 'u' in i and 'p' in i:
            fin.append(i)
    fin[0] = fin[0].capitalize()
    print(' '.join(fin))
a= 'Wazzzzzuuuup bro haw ware youuuozw Zupppawazup ooo www zuuuppzup wupaz wupaz zoooo wzauuuuuppp ppppuz waz zaw upppzwaa uu zwa zwa'
do(a)