import pdfkit

WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)


def generate_pdf_from_html(html: str):

    options = {
        "page-size": "A4",
        "encoding": "UTF-8",
        "enable-local-file-access": None,
        "no-outline": None,
        "margin-top": "10mm",
        "margin-bottom": "5mm",
        "margin-left": "10mm",
        "margin-right": "10mm",
        "zoom": "1.0",
        "print-media-type": None
    }

    pdf = pdfkit.from_string(
        html,
        False,
        configuration=config,
        options=options
    )

    return pdf
