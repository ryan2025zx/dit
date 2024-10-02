from fpdf import FPDF

# Function to create a PDF with a refined grid pattern, a light green background, and a cross-shaped darker central area
def create_refined_grid_notebook(page_count=10, filename="grid_notebook.pdf"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    
    # Adding pages with a refined grid and varied background colors
    for page_number in range(page_count):
        pdf.add_page()
        print(f"Creating page {page_number+1}")  # Debug output
        
        # Set the background color to light green
        pdf.set_fill_color(236, 255, 236)  # Light green
        pdf.rect(0, 0, 210, 297, 'F')  # Fill the entire page
        
        # Darken the central cross-shaped area
        cross_width = 10  # Width of the cross arms
        vertical_start = (297 - cross_width) / 2
        horizontal_start = (210 - cross_width) / 2
        
        # Vertical arm of the cross
        pdf.set_fill_color(170, 255, 170)  # Darker green
        pdf.rect(horizontal_start, 0, cross_width, 297, 'F')
        
        # Horizontal arm of the cross
        pdf.rect(0, vertical_start, 210, cross_width, 'F')
        
        # Draw smaller grid cells
        small_grid_size = 2  # 5mm small grid cells

        # Set light gray for normal grid lines
        pdf.set_draw_color(200, 200, 200)  # Light gray color
        for i in range(0, 297 + small_grid_size, small_grid_size):  # Horizontal grid lines
            pdf.line(0, i, 210, i)
        for i in range(0, 210 + small_grid_size, small_grid_size):  # Vertical grid lines
            pdf.line(i, 0, i, 297)
        
        # Set black for thick grid lines
        pdf.set_draw_color(127, 127, 127)
        thick_line_interval = 4  # Every 4 small cells, there's a thicker line
        for i in range(0, 297 + small_grid_size, small_grid_size * thick_line_interval):  # Horizontal thick lines
            pdf.line(0, i, 210, i)
        for i in range(0, 210 + small_grid_size, small_grid_size * thick_line_interval):  # Vertical thick lines
            pdf.line(i, 0, i, 297)
        
    # Output the PDF to a file
    pdf.output(filename)
    print("PDF generation complete.")  # Confirm completion

# Example: Create a PDF with 10 pages of refined grid pattern with a light green background
create_refined_grid_notebook()