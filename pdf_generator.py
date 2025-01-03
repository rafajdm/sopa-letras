from fpdf import FPDF

def create_pdf(puzzles, words_list):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    cell_size = 8  # Tamaño de cada celda en el grid
    page_width = 210  # Ancho de la página A4 en mm
    grid_size = 20 * cell_size  # Tamaño total del grid
    margin = (page_width - grid_size) / 2  # Calcular el margen para centrar el grid
    
    for puzzle, words in zip(puzzles, words_list):
        pdf.add_page()
        start_x = margin
        start_y = margin
        
        # Dibujar los bordes exteriores del grid
        pdf.line(start_x, start_y, start_x + 20 * cell_size, start_y)  # Borde superior
        pdf.line(start_x, start_y + 20 * cell_size, start_x + 20 * cell_size, start_y + 20 * cell_size)  # Borde inferior
        pdf.line(start_x, start_y, start_x, start_y + 20 * cell_size)  # Borde izquierdo
        pdf.line(start_x + 20 * cell_size, start_y, start_x + 20 * cell_size, start_y + 20 * cell_size)  # Borde derecho
        
        # Colocar las letras en el grid
        for row in range(20):
            for col in range(20):
                pdf.text(start_x + col * cell_size + 2, start_y + row * cell_size + 6, puzzle[row][col])
        
        pdf.ln(10)
        
        # Dibujar la tabla de palabras
        table_start_y = start_y + 20 * cell_size + 20  # Posición Y después del grid con espacio adicional
        pdf.set_xy(start_x, table_start_y)
        
        words_per_column = len(words) // 4
        for i in range(words_per_column):
            pdf.set_x(start_x)  # Reiniciar la posición X al inicio de cada fila
            for j in range(4):
                word_index = i + j * words_per_column
                if word_index < len(words):
                    pdf.cell(40, 10, words[word_index], 0, 0, 'L')
            pdf.ln(10)
    
    pdf.output("sopas_de_letras.pdf")