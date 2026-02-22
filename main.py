import os
from converter import CBZConverter

if __name__ == "__main__":
    response = input("Please, write the file/directory you want to convert: ")

    converter = CBZConverter()

    # Should i make this part of the Converter object? Maybe...
    if os.path.isdir(response):
        files = []
        for _, _, filenames in os.walk(response):
            files.extend(filenames)
            break

        converted_files = 0
        total_files = len(files)
        for file in files:
            print(f'Converting: {file}', end="")

            if converter.convert_zip_to_pdf(f'{response}/{file}'):
                print(" -> Success")
                converted_files += 1
            else:
                print(" -> Failed")
        
        print(f"Converted: {converted_files}/{total_files} ({(converted_files / total_files) * 100}%)")
  
    else:
        if converter.convert_zip_to_pdf(response):
            print(f"Converted: {response}")