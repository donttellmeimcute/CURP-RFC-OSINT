import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QFileDialog

from calcule import CalculeRFC, CalculeCURP, CalculeGeneric

class GenerateDataFiscal(CalculeGeneric):
    generadores = (CalculeCURP, CalculeRFC)

class VentanaResultados(QWidget):
    def __init__(self, curps):
        super().__init__()

        self.curps = curps

        self.setWindowTitle("CURPs Generados")
        self.layout = QVBoxLayout()

        self.curps_textedit = QTextEdit()
        self.curps_textedit.setPlainText("\n".join(curps))

        self.boton_copiar = QPushButton("Copiar")
        self.boton_copiar.clicked.connect(self.copiar_curps)

        self.boton_guardar = QPushButton("Guardar en Archivo")
        self.boton_guardar.clicked.connect(self.guardar_curps)

        self.layout.addWidget(self.curps_textedit)
        self.layout.addWidget(self.boton_copiar)
        self.layout.addWidget(self.boton_guardar)

        self.setLayout(self.layout)

    def copiar_curps(self):
        self.curps_textedit.selectAll()
        self.curps_textedit.copy()

    def guardar_curps(self):
        ruta_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar CURPs en archivo", "", "Archivos de Texto (*.txt)")
        if ruta_archivo:
            with open(ruta_archivo, 'w') as archivo:
                archivo.write("\n".join(self.curps))

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generar Datos Fiscales")
        self.layout = QVBoxLayout()

        self.label_nombre = QLabel("Nombre:")
        self.input_nombre = QLineEdit()

        self.label_paterno = QLabel("Apellido Paterno:")
        self.input_paterno = QLineEdit()

        self.label_materno = QLabel("Apellido Materno:")
        self.input_materno = QLineEdit()

        self.label_genero = QLabel("Género:")
        self.input_genero = QComboBox()
        self.input_genero.addItems(["H", "M", "X"])

        self.label_fecha = QLabel("Fecha de nacimiento (dd-mm-aaaa):")
        self.input_fecha = QLineEdit()

        self.boton_curps = QPushButton("Solo CURPs")
        self.boton_curps.clicked.connect(self.generar_curps)

        self.boton_rfc = QPushButton("Solo RFC")
        self.boton_rfc.clicked.connect(self.generar_rfc)

        self.boton_lista = QPushButton("Lista Completa")
        self.boton_lista.clicked.connect(self.generar_lista)

        self.label_resultado = QLabel()

        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.input_nombre)

        self.layout.addWidget(self.label_paterno)
        self.layout.addWidget(self.input_paterno)

        self.layout.addWidget(self.label_materno)
        self.layout.addWidget(self.input_materno)

        self.layout.addWidget(self.label_genero)
        self.layout.addWidget(self.input_genero)

        self.layout.addWidget(self.label_fecha)
        self.layout.addWidget(self.input_fecha)

        self.layout.addWidget(self.boton_curps)
        self.layout.addWidget(self.boton_rfc)
        self.layout.addWidget(self.boton_lista)

        self.layout.addWidget(self.label_resultado)

        self.setLayout(self.layout)

    def generar_curps(self):
        nombre = self.input_nombre.text()
        paterno = self.input_paterno.text()
        materno = self.input_materno.text()
        genero = self.input_genero.currentText()
        fecha = self.input_fecha.text()

        estados = ['AGUASCALIENTES', 'BAJA CALIFORNIA', 'BAJA CALIFORNIA SUR', 'CAMPECHE', 'CHIAPAS', 'CHIHUAHUA', 'DISTRITO FEDERAL', 'COAHUILA', 'COLIMA', 'DURANGO', 'GUANAJUATO', 'GUERRERO', 'HIDALGO', 'JALISCO', 'MEXICO', 'MICHOACAN', 'MORELOS', 'NAYARIT', 'NUEVO LEON', 'OAXACA', 'PUEBLA', 'QUERETARO', 'QUINTANA ROO', 'SAN LUIS POTOSI', 'SINALOA', 'SONORA', 'TABASCO', 'TAMAULIPAS', 'TLAXCALA', 'VERACRUZ', 'YUCATÁN', 'ZACATECAS']

        curps = []
        for estado in estados:
            datos = {
                'fecha': fecha,
                'nombres': nombre,
                'paterno': paterno,
                'materno': materno,
                'genero': genero,
                'estado': estado
            }

            data_fiscal = GenerateDataFiscal(**datos).data
            curp = data_fiscal["curp"]
            curps.append(f"{curp}")

        self.mostrar_ventana_resultados(curps)

    def generar_rfc(self):
        nombre = self.input_nombre.text()
        paterno = self.input_paterno.text()
        materno = self.input_materno.text()
        genero = self.input_genero.currentText()
        fecha = self.input_fecha.text()



        rfcs = []
        
        datos = {
                'fecha': fecha,
                'nombres': nombre,
                'paterno': paterno,
                'materno': materno,
                'genero': genero,
                'estado': 'DISTRITO FEDERAL'
            }

        data_fiscal = GenerateDataFiscal(**datos).data
        rfc = data_fiscal["rfc"]
        rfcs.append(f"RFC: {rfc}")

        self.mostrar_ventana_resultados(rfcs)

    def generar_lista(self):
        nombre = self.input_nombre.text()
        paterno = self.input_paterno.text()
        materno = self.input_materno.text()
        genero = self.input_genero.currentText()
        fecha = self.input_fecha.text()

        estados = ['AGUASCALIENTES', 'BAJA CALIFORNIA', 'BAJA CALIFORNIA SUR', 'CAMPECHE', 'CHIAPAS', 'CHIHUAHUA', 'DISTRITO FEDERAL', 'COAHUILA', 'COLIMA', 'DURANGO', 'GUANAJUATO', 'GUERRERO', 'HIDALGO', 'JALISCO', 'MEXICO', 'MICHOACAN', 'MORELOS', 'NAYARIT', 'NUEVO LEON', 'OAXACA', 'PUEBLA', 'QUERETARO', 'QUINTANA ROO', 'SAN LUIS POTOSI', 'SINALOA', 'SONORA', 'TABASCO', 'TAMAULIPAS', 'TLAXCALA', 'VERACRUZ', 'YUCATÁN', 'ZACATECAS']

        curps = []
        for estado in estados:
            datos = {
                'fecha': fecha,
                'nombres': nombre,
                'paterno': paterno,
                'materno': materno,
                'genero': genero,
                'estado': estado
            }

            data_fiscal = GenerateDataFiscal(**datos).data
            curp = data_fiscal["curp"]
            curps.append(f"CURP: {curp}, Estado: {estado}")

        self.mostrar_ventana_resultados(curps)

    def mostrar_ventana_resultados(self, curps):
        self.ventana_resultados = VentanaResultados(curps)
        self.ventana_resultados.show()

def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
