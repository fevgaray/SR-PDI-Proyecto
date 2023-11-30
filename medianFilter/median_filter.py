import os
import cv2
import glob

def apply_median_filter(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    image_files = glob.glob(os.path.join(input_dir, '*.png'))
    for image_file in image_files:
        image = cv2.imread(image_file)

        if image is not None:
            filtered_image = cv2.medianBlur(image, 3)
            filename = os.path.splitext(os.path.basename(image_file))[0]

            output_file = os.path.join(output_dir, f'{filename}_median.jpg')
            cv2.imwrite(output_file, filtered_image)
            print(f"Saved {output_file}")

if __name__ == '__main__':
    input_directory = './input'
    output_directory = './output'

    apply_median_filter(input_directory, output_directory)