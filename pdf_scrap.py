import pymupdf

doc = pymupdf.open("README.pdf")

with open("scrap_content.txt", "w") as file:
    for page in doc:
        file.write(page.get_text())
        file.write("\n")
