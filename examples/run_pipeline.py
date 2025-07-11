from pluxtools import process_plux_file, process_images

input_file = "/path/to/your/file.plux"
output_img_dir = "/path/to/output"

# Convert PLUX to image
png_path = process_plux_file(input_file, output_img_dir)

# Compute metrics
df = process_images(output_img_dir)
print(df.head())
