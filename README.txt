soxが必要です。

このフォルダに「voice」というwavファイルがすべて入っているフォルダと、
voice_text.txtという「wavファイル名:セリフ」の形式で書かれたテキストファイルを置いてください。

中でpythonが動きます。
pyopenjtalk
jaconv
が必要ですのでpip install pyopenjtalk jaconvしてください。


これらの準備が出来たら「./run.sh」で同階層のlabフォルダに、duration付きのフルコンテキストラベルのファイルが生成されます。