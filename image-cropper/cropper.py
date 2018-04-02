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


if __name__ == "__main__":
    img_input_path = sys.argv[1]
    img_output_path = sys.argv[2]

    image_cropper = ImageCropper()
    if len(sys.argv) >= 5:
        img_x_pieces = int(sys.argv[3])
        img_y_pieces = int(sys.argv[4])
        if len(sys.argv) >= 6 :
            img_suffix = sys.argv[5]
            image_cropper.crop_image(img_input_path, img_output_path, img_x_pieces, img_y_pieces, img_suffix)
        else:
            image_cropper.crop_image(img_input_path, img_output_path, img_x_pieces, img_y_pieces)
    else:
        image_cropper.crop_image(img_input_path, img_output_path)
