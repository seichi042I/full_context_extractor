import pyopenjtalk
import jaconv
import os
from pathlib import Path

with open('voice_text.txt','r') as in_file:
    for line in in_file.readlines():
        name = line.split(':')[0]
        text = line.split(':')[1]

        #kata=pyopenjtalk.g2p(text,kana=False)
        # kata = kata.replace('。','')
        # kata = kata.replace('?','')
        # kata = kata.replace('？','')
        # kata = kata.replace('!','')
        # kata = kata.replace('！','')

        # hira = jaconv.kata2hira(kata)
        # hira = hira.replace('、',' ')
        # hira = hira.replace('\n','')

        phoneme = pyopenjtalk.g2p(text,kana=False)
        phoneme = phoneme.lower()
        phoneme = phoneme.replace('pau','sp')
        phoneme = phoneme.replace('cl','q')
        print(phoneme)
        Path("text").mkdir(exist_ok=True,parents=True)
        with open('text/'+name+'.txt','w') as out_file:
            out_file.write(phoneme)