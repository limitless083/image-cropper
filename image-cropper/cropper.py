import os
import sys
from PIL import Image


class ImageCropper:
    def crop_image(self, img_input_path, img_output_path, x=1, y=2, img_suffix='jpg'):
        img = Image.open(img_input_path)
        w, h = img.size
        width_piece = w / x
        height_piece = h / y
        for i in range(y):
            for j in range(x):
                img.crop((width_piece * j, height_piece * i, width_piece * (j + 1), height_piece * (i + 1))).save('{}{}{}.{}'.format(img_output_path, i, j, img_suffix))

    def crop_image_in_dir(self, img_input_path, img_output_path, x=1,y=2):
        for path, dir_list, file_list in os.walk(img_input_path):
            for file in file_list:
                print(os.path.join(path, file))
                [file_prefix, file_suffix] = str.split(file, '.')
                self.crop_image(
                    os.path.join(path, file),
                    os.path.join(img_output_path, file_prefix),
                    x,
                    y,
                    file_suffix
                )


if __name__ == "__main__":
    img_input_path = sys.argv[1]
    img_output_path = sys.argv[2]

    image_cropper = ImageCropper()
    if len(sys.argv) >= 5:
        img_x_pieces = int(sys.argv[3])
        img_y_pieces = int(sys.argv[4])
        image_cropper.crop_image_in_dir(img_input_path, img_output_path, img_x_pieces, img_y_pieces)
    else:
        image_cropper.crop_image_in_dir(img_input_path, img_output_path)
