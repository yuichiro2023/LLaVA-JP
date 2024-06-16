"""
python tools/resize_images.py ./image_test/origin ./image_test/resize 768
"""

import argparse
import os

from PIL import Image
from tqdm import tqdm


def resize_image(image, max_size):
    # 元の解像度を取得
    original_width, original_height = image.size

    # 比率を計算
    aspect_ratio = original_width / original_height

    # 新しいサイズを計算
    if original_width > original_height:
        if original_width > max_size:
            new_width = max_size
            new_height = int(new_width / aspect_ratio)
        else:
            new_width = original_width
            new_height = original_height
    else:
        if original_height > max_size:
            new_height = max_size
            new_width = int(new_height * aspect_ratio)
        else:
            new_width = original_width
            new_height = original_height

    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)


def resize_images_in_directory(input_directory, output_directory, max_size):
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 入力ディレクトリ内のすべてのファイルを取得
    for filename in tqdm(os.listdir(input_directory)):
        # ファイルが.jpgで終わる場合
        if filename.lower().endswith(".jpg"):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename)

            # 画像を開く
            with Image.open(input_file_path) as img:
                # 画像をリサイズ
                resized_img = resize_image(img, max_size)

                # リサイズした画像を出力ディレクトリに保存
                resized_img.save(output_file_path)


def main():
    parser = argparse.ArgumentParser(
        description="Resize .jpg images in a directory to a max size while maintaining aspect ratio."
    )
    parser.add_argument("input_directory", type=str, help="Path to the input directory")
    parser.add_argument(
        "output_directory", type=str, help="Path to the output directory"
    )
    parser.add_argument(
        "image_size", type=int, help="Max size for the longest edge of the image"
    )

    args = parser.parse_args()

    resize_images_in_directory(
        args.input_directory, args.output_directory, args.image_size
    )


if __name__ == "__main__":
    main()
