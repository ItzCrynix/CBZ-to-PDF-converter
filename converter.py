import zipfile
import xml.etree.ElementTree as ET
import pypdf

class CBZConverter():
    def __init__(self):
        pass

    def convert_xml_data_to_pdf_metadata(self, zip_file: zipfile.ZipFile) -> dict[str, str]:
        xml_file_name = [file for file in zip_file.namelist() if file.endswith(".xml")][0]
            
        # Gets the xml data and parses it to fit the pdf metadata
        with zip_file.open(xml_file_name) as xml_file:
            parsed_xml_file = ET.parse(xml_file).getroot()
        
        return

    def get_images_from_zip(self, zip_file:zipfile.ZipFile):
        image_extensions = (".jpg", ".jpeg", ".png", ".webp")
        manga_chapters = [file_name for file_name in zip_file.namelist() if file_name.lower().endswith(image_extensions)]

        manga_images = []
    
    def convert_zip_to_pdf(self, file_name: str) -> None:
        # checks if the file extension is a compressed folder
        if not (file_name.endswith(".zip") or file_name.endswith(".cbz")):
            return

        # Opens the zip file in read mode
        with zipfile.ZipFile(file_name, "r") as zip_file:
            try:
                manga_pdf = pypdf.PdfWriter()

                manga_pdf.add_metadata(self.convert_xml_data_to_pdf_metadata(zip_file))

                images = self.get_images_from_zip()

                manga_pdf.write("test.pdf")
            except:
                print("Error while creating the pdf file")


if __name__ == "__main__":
    new_file = "ProxyONE Scanlator_Vol.6 Ch.30.5 - A História de F. Valentine.cbz"

    CBZConverter.convert_zip_to_pdf(new_file)