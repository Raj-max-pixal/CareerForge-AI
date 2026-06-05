from fpdf import FPDF
import tempfile

def create_report(content):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    content = content.encode(
        "latin-1",
        "replace"
    ).decode("latin-1")

    pdf.multi_cell(
        0,
        10,
        txt=content
    )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    pdf.output(temp_file.name)

    return temp_file.name