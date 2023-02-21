mkdir -p 16kHz
cd voice
ls | while read file;do sox $file -r 16000 -c 1 -b 16 ../16kHz/$file;echo "${file} is converted."; done
cd ../
python convert.py
cd segmentation-kit-4.3.1
mkdir -p dfa_dict
mkdir -p lab
mkdir -p log
./segment_julius.pl
cd ../
python full_context.py