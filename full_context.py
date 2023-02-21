import pyopenjtalk
import jaconv
import os
from pathlib import Path

with open('voice_text.txt','r') as tsf:
    for line in tsf.readlines():
        name = line.split(':')[0]
        text = line.split(':')[1]
        fulcon = pyopenjtalk.extract_fullcontext(text)
        dur=[]
        with open('segmentation-kit-4.3.1/lab/'+name+'.lab','r') as labf:
            for l in labf.readlines():
                start = l.split(' ')[0]
                end = l.split(' ')[1]
                dur.append(start+' '+end)
        
        fulcon = [x.replace('.','')+' '+y for (x,y) in zip(dur,fulcon)]
        full_context_label = '\n'.join(fulcon)
        print(full_context_label)
        Path("lab").mkdir(exist_ok=True,parents=True)
        with open('lab/'+name+'.lab','w') as outf:
            outf.write(full_context_label)