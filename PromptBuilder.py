import sys
import json
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QTextEdit, QLabel, 
                             QMessageBox, QTableWidget, QTableWidgetItem)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QClipboard

class RecipePromptGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.recipes = []
        self.recipes_file = 'recipes.json'
        self.load_recipes()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Generador de Prompts de Recetas')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Entrada para el nombre de la receta
        self.recipe_name_input = QLineEdit()
        self.recipe_name_input.setPlaceholderText("Nombre de la receta")
        layout.addWidget(self.recipe_name_input)

        # Botones
        button_layout = QHBoxLayout()
        
        self.generate_button = QPushButton('Generar Prompt')
        self.generate_button.clicked.connect(self.generate_prompt)
        button_layout.addWidget(self.generate_button)

        self.copy_button = QPushButton('Copiar al Portapapeles')
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(self.copy_button)

        layout.addLayout(button_layout)

        # Área para mostrar el prompt generado
        self.generated_prompt = QTextEdit()
        self.generated_prompt.setReadOnly(True)
        layout.addWidget(self.generated_prompt)

        # Tabla para mostrar las recetas guardadas
        self.recipe_table = QTableWidget()
        self.recipe_table.setColumnCount(1)
        self.recipe_table.setHorizontalHeaderLabels(["Recetas Guardadas"])
        self.recipe_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.recipe_table)

        self.setLayout(layout)
        self.update_recipe_table()

    def generate_prompt(self):
        recipe_name = self.recipe_name_input.text()
        
        if not recipe_name:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un nombre de receta.")
            return

        if recipe_name in self.recipes:
            QMessageBox.warning(self, "Advertencia", f"La receta '{recipe_name}' ya existe.")
            return

        prompt = f'''Genera una receta en formato JSON con la siguiente información:
- Nombre de la receta: {recipe_name}
- URL de la imagen: {{image_url}}
- Ingredientes: {{ingredients_list}}
- Pasos: {{steps_list}}
- Tiempo total: {{total_time}}

La receta debe tener el siguiente formato JSON:
{{
  "imageUrl": "{{image_url}}",
  "ingredients": [
    {{ingredients_list}}
  ],
  "name": "{recipe_name}",
  "steps": [
    {{steps_list}}
  ],
  "time": "{{total_time}}"
}}
Importante que todo esto sea en Español Chileno y en los steps no deben ir enumerados'''

        self.generated_prompt.setPlainText(prompt)
        self.save_recipe(recipe_name)

    def save_recipe(self, recipe_name):
        if recipe_name not in self.recipes:
            self.recipes.append(recipe_name)
            self.update_recipe_table()
            self.save_recipes()
            QMessageBox.information(self, "Guardado", f"Receta '{recipe_name}' guardada exitosamente.")

    def update_recipe_table(self):
        self.recipe_table.setRowCount(len(self.recipes))
        for i, recipe in enumerate(self.recipes):
            self.recipe_table.setItem(i, 0, QTableWidgetItem(recipe))

    def copy_to_clipboard(self):
        prompt = self.generated_prompt.toPlainText()
        if prompt:
            clipboard = QApplication.clipboard()
            clipboard.setText(prompt)
            QMessageBox.information(self, "Copiado", "Prompt copiado al portapapeles.")
        else:
            QMessageBox.warning(self, "Error", "No hay prompt para copiar.")

    def load_recipes(self):
        if os.path.exists(self.recipes_file):
            with open(self.recipes_file, 'r') as f:
                self.recipes = json.load(f)

    def save_recipes(self):
        with open(self.recipes_file, 'w') as f:
            json.dump(self.recipes, f)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecipePromptGenerator()
    ex.show()
    sys.exit(app.exec())