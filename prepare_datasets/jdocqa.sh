#!/bin/bash

# 以下のデータセットを用意
# JDocQA

mkdir ./dataset/jdocqa

# Stage2
### キャプション準備
python tools/jdocqa/jdocqa_to_llava_format.py 

### 画像準備
mkdir -p ./dataset/jdocqa/pdf
wget -P ./dataset/jdocqa/pdf https://vlm-lab-fileshare.s3.ap-northeast-1.amazonaws.com/pdf_files.zip

unzip ./dataset/jdocqa/pdf/pdf_files.zip -d ./dataset/jdocqa/pdf

python tools/pdf_to_images.py ./dataset/jdocqa/pdf/pdf_files ./dataset/jdocqa/images

rm ./dataset/jdocqa/pdf/pdf_files.zip
rm -r ./dataset/jdocqa/pdf