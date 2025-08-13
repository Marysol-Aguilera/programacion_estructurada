from fpdf import FPDF

def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("\n\t 🕒... Oprima cualquier tecla para continuar ...🕒")


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Inventario ", ln=True, align="C")
        self.ln(5)

    def tabla_inventario(self, datos):
        self.set_font("Arial", "B", 10)
        headers = ["ID", "Marca", "Tipo", "Talla", "Precio", "Color" ]
        col_widths = [15, 30, 30, 20, 20, 25]

        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C")
        self.ln()

        self.set_font("Arial", "", 9)
        for fila in datos:
            for i, item in enumerate(fila):
                self.cell(col_widths[i], 8, str(item), border=1, align="C")
            self.ln()    