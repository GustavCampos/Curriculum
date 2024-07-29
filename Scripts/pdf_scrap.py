import pymupdf

doc = pymupdf.open("README.pdf")

with open("scrap_content.txt", "w", encoding="utf-8") as file:
    for page in doc:
        file.write(page.get_text())
