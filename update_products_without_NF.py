import utils.get_file_path.get_file_path as file_path
import utils.img_to_text.img_to_text as img_to_text

file_path = file_path.get_file_path()

print(file_path)

text = img_to_text.extract_text_from_image(image_path=file_path)

print(text)

