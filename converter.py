import zipfile, pypdf, io
import xml.etree.ElementTree as ET
from PIL import Image

class CBZConverter():
    def __init__(self):
        self.convertion_table = {
            "Writer": "Author",
            "Penciller": "Author",
            "Genre": "Keywords",
            "Series": "Title",
            "Title": "Subject"
        }

    def __convert_xml_data_to_pdf_metadata(self, zip_file: zipfile.ZipFile) -> dict[str, str]:
        xml_file_name = [file for file in zip_file.namelist() if file.endswith(".xml")][0]
        manga_metadata = {
            "/Creator": "ItzCrynix"
        }
            
        # Gets the xml data and parses it to fit the pdf metadata
        with zip_file.open(xml_file_name, "r") as xml_file:
            parsed_xml_file = ET.parse(xml_file).getroot()

            for item in parsed_xml_file:
                if converted_key := self.convertion_table.get(item.tag):
                    manga_metadata[f"/{converted_key}"] = item.text
                else:
                    manga_metadata[f"/{item.tag}"] = item.text
        
        return manga_metadata

    def __get_images_from_zip(self, zip_file:zipfile.ZipFile) -> list[Image.Image]:
        image_extensions = (".jpg", ".jpeg", ".png", ".webp")

        # Take only the chapter images
        manga_chapters = [file_name for file_name in zip_file.namelist() if file_name.lower().endswith(image_extensions)]
        manga_chapters.sort()

        manga_images = []
        # Iterates through the file names and saves the binary of the image
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
                    images = self.__get_images_from_zip(zip_file)
                    
                    if not images:
                        raise FileNotFoundError
                    
                    images[0].save("temp.pdf", save_all=True, append_images=images[1:])

                    manga_images_pdf = pypdf.PdfReader("temp.pdf")
                    manga_final_pdf = pypdf.PdfWriter()

                    for page in manga_images_pdf.pages:
                        manga_final_pdf.add_page(page)

                    manga_metadata = self.__convert_xml_data_to_pdf_metadata(zip_file)
                    manga_final_pdf.add_metadata(manga_metadata)

                    manga_final_pdf.write(f"{manga_metadata.get("/Title")} - Capitulo {manga_metadata.get("/Number")}.pdf")

        except ValueError:
            print("Error: Invalid file type")
        except FileNotFoundError:
            print("Error: No images was found inside the zip file")
        except:
            print("Error: Unable to create the pdf file")