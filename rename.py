import os

# directory = r'--PATH TO FILE--'

os.chdir(directory)

for img in os.listdir(directory):
    # Separates file name from file extension
    img_name, img_ext = os.path.splitext(img)

    # Split up file name by chosen delimiter and rename as needed.
    prefix, middle, suffix = img_name.split('_')

    add_on = "ETC"  # For example

    new_name = (f"{prefix}_{middle}_{add_on}_{suffix}{img_ext}")

    print(new_name)  # always print to check before renaming files.
    # os.rename(img, new_name)
