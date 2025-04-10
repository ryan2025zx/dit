from fpdf import FPDF

def create_refined_grid_notebook(page_count=10, filename="grid_notebook.pdf"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    
    for page_number in range(page_count):
        pdf.add_page()
        print(f"Creating page {page_number+1}")
        
        # 白色背景
        pdf.set_fill_color(255, 255, 255)
        pdf.rect(0, 0, 210, 297, 'F')
        
        small_grid_size = 2   # 小格：2mm
        big_grid_interval = 10  # 大格：每10mm

        # 浅灰色小格线
        pdf.set_draw_color(186, 186, 186)
        for i in range(0, 297 + small_grid_size, small_grid_size):  # 横线
            pdf.line(0, i, 210, i)
        for i in range(0, 210 + small_grid_size, small_grid_size):  # 竖线
            pdf.line(i, 0, i, 297)

        # 黑色粗大格线
        pdf.set_draw_color(100, 100, 100)
        for i in range(0, 297 + big_grid_interval, big_grid_interval):  # 横向大格
            pdf.line(0, i, 210, i)
        for i in range(0, 210 + big_grid_interval, big_grid_interval):  # 纵向大格
            pdf.line(i, 0, i, 297)
    
    pdf.output(filename)
    print("PDF generation complete.")

# 生成带小格和大格的笔记纸 PDF
create_refined_grid_notebook()
