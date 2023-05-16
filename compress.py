from PIL import Image
import os
import csv

input_dir = 'pictures' # directory containing the images to be compressed
output_dir = 'output_images' # directory where the compressed images will be saved
csv_file = 'compression_results.csv' # CSV file where the compression results will be saved

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(csv_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Image', 'Original Size (bytes)', 'Compressed Size (bytes)', 'Compression Ratio'])

    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            original_size = os.stat(input_path).st_size

            image = Image.open(input_path)
            image.save(output_path, 'PNG')

            compressed_size = os.stat(output_path).st_size
            compression_ratio = compressed_size / original_size

            writer.writerow([filename, original_size, compressed_size, compression_ratio])
