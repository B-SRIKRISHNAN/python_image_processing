import img2pdf

def convert_img_to_pdf(file_path):
    with open("./resources/test_pdf.pdf","wb") as f:
        f.write(img2pdf.convert(file_path))
convert_img_to_pdf("./resources/Tables.png")

