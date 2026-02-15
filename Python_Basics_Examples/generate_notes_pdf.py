from fpdf import FPDF
import os

class PythonNotesPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Python Programming Notes', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, content):
        self.set_font('Courier', '', 10)
        # Handle unicode characters that fpdf might not like in core fonts
        # For simplicity in this env, we'll replace non-ascii if any
        safe_content = content.encode('ascii', 'ignore').decode('ascii')
        self.multi_cell(0, 5, safe_content)
        self.ln()

def generate_notes():
    pdf = PythonNotesPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    files = [
        ('1. Simple Calculator', 'calculator.py'),
        ('2. Basic While Loops', 'while_loop_examples.py'),
        ('3. Advanced While Loops', 'more_while_loop_examples.py'),
        ('4. Function Examples', 'function_examples.py'),
        ('5. Basic Arithmetic (Sum/Sub)', 'sum_of_two_numbers.py'),
        ('6. Multiplication Table', 'multiplication_table.py'),
        ('7. Python Data Types', 'data_types_examples.py'),
        ('8. Dynamic Typing Demo', 'dynamic_typing_demo.py')
    ]
    
    for title, filename in files:
        if os.path.exists(filename):
            pdf.add_page()
            pdf.chapter_title(title)
            with open(filename, 'r') as f:
                content = f.read()
            pdf.chapter_body(content)
    
    pdf.output('Python_Examples_Notes.pdf')
    print("Successfully generated Python_Examples_Notes.pdf")

if __name__ == "__main__":
    generate_notes()
