# install 
`sudo apt-get update`
`sudo apt-install build-essential cmake sox`
`pip install pyopenjtalk jaconv`

`chmod +x run.sh segmentation-kit-4.3.1/segment_julius.pl segmentation-kit-4.3.1/bin/julius-4.3.1.exe`


soxが必要です。

このフォルダに「voice」というwavファイルがすべて入っているフォルダと、
voice_text.txtという「wavファイル名:セリフ」の形式で書かれたテキストファイルを置いてください。

中でpythonが動きます。
pyopenjtalk
jaconv
が必要ですのでpip install pyopenjtalk jaconvしてください。


これらの準備が出来たら「./run.sh」で同階層のlabフォルダに、duration付きのフルコンテキストラベルのファイルが生成されます。