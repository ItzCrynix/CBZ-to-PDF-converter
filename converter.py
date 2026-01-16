import zipfile, pypdf, io
import xml.etree.ElementTree as ET
from PIL import Image

class CBZConverter():
    def __init__(self):
        pass

    def convert_xml_data_to_pdf_metadata(self, zip_file: zipfile.ZipFile) -> dict[str, str]:
        xml_file_name = [file for file in zip_file.namelist() if file.endswith(".xml")][0]
            
        # Gets the xml data and parses it to fit the pdf metadata
        with zip_file.open(xml_file_name) as xml_file:
            parsed_xml_file = ET.parse(xml_file).getroot()
        
        return

    def get_images_from_zip(self, zip_file:zipfile.ZipFile) -> list[Image.Image]:
        image_extensions = (".jpg", ".jpeg", ".png", ".webp")
        manga_chapters = [file_name for file_name in zip_file.namelist() if file_name.lower().endswith(image_extensions)]

        manga_images = []
        for chapter in manga_chapters:
            with zip_file.open(chapter) as image:
                image_bytes = io.BytesIO(image.read())

                converted_image = Image.open(image_bytes).convert("RGB")
                manga_images.append(converted_image)

        return manga_images
                
    
    def convert_zip_to_pdf(self, file_name: str) -> None:
        try:
            # checks if the file extension is a compressed folder
            if not (file_name.endswith(".zip") or file_name.endswith(".cbz")):
                raise ValueError

            # Opens the zip file in read mode
            with zipfile.ZipFile(file_name, "r") as zip_file:
                    images = self.get_images_from_zip(zip_file)
                    
                    if not images:
                        raise FileNotFoundError
                    
                    images[0].save("temp.pdf", save_all=True, append_images=images[1:])

                    manga_images_pdf = pypdf.PdfReader("temp.pdf")
                    manga_final_pdf = pypdf.PdfWriter()

                    for page in manga_images_pdf.pages:
                        manga_final_pdf.add_page(page)

                    manga_metadata = self.convert_xml_data_to_pdf_metadata(zip_file)
                    manga_final_pdf.add_metadata(manga_metadata)

                    manga_final_pdf.write(f"{manga_metadata.get("Series")} - Capitulo {manga_metadata.get("Number")}.pdf")

        except ValueError:
            print("Error: Invalid file type")
        except FileNotFoundError:
            print("Error: No images was found inside the zip file")
        except:
            print("Error: Unable to create the pdf file")


if __name__ == "__main__":
    new_file = "ProxyONE Scanlator_Vol.6 Ch.30.5 - A História de F. Valentine.cbz"

    CBZConverter.convert_zip_to_pdf(new_file)