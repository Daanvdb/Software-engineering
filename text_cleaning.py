michael_txt = []
dwight_txt = []

with open('michael.txt', encoding = 'utf-8') as fp:
    while True:
        buffer = fp.readline()
        if buffer == '':
            break
        else:
            try:
                dwight_txt.append(buffer)
            except:
                print('too long')

dwight_txt.remove('\n')
dwight_txt.remove(dwight_txt[0])

for i in dwight_txt:
    if len(i) == 1:
        dwight_txt.remove(i)
        
for i, j in enumerate(dwight_txt):
    j = j.replace('"', '')
    j = j.replace('“','')
    j = j.replace('”','')
    dwight_txt[i] = j
        
for i, j in enumerate(dwight_txt):
    if ':' in j:
        dwight_txt[i] = j.split(':')[1]

fp = open('clean_michael.txt', 'a+')

for i in dwight_txt:
    fp.write(i)
    
fp.close()