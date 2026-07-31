from langchain_google_genai import ChatGoogleGenerativeAI
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import base64
def create_pdf(text):
    pdf_path = "generated_content.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter  # Get page size

    # Set font
    c.setFont("Helvetica", 12)

    # Set margins
    left_margin = 50
    top_margin = height - 50  # Start from near the top

    # Wrap text to fit within page width
    max_width = width - 100  # Leave margin on both sides
    lines = simpleSplit(text, "Helvetica", 12, max_width)

    # Print each line, adjusting Y position
    y = top_margin
    line_height = 14  # Space between lines

    for line in lines:
        if y < 50:  # Move to new page if reaching bottom margin
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50  # Reset Y position

        c.drawString(left_margin, y, line)
        y -= line_height  # Move to next line

    c.save()
    return pdf_path

    #pdf_path = "generated_content.pdf"
    #c = canvas.Canvas(pdf_path, pagesize=letter)
    #c.setFont("Helvetica", 12)  # Helvetica supports Unicode
    #c.drawString(1, 50, text)  # Adjust position as needed
    #c.save()
    #return pdf_path


# Function to get PDF download link
def get_pdf_download_link(pdf_path, filename="download.pdf"):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_link = f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="{filename}">📥 Download PDF</a>'
    return pdf_link

from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

def get_gemini_response_pdf(prompt_template):
    model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0.3)
    prompt=PromptTemplate(template=prompt_template, input_variables=["context","question"])
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain
