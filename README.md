# Generador de Prompts de Recetas

Este software es una herramienta para generar prompts de recetas y mantener un registro de las recetas creadas.

## Uso del Software

1. Ejecute el archivo `PromptBuilder.exe`.
2. En la ventana principal, ingrese el nombre de la receta en el campo de texto.
3. Haga clic en el botón "Generar Prompt" para crear un prompt basado en el nombre de la receta.
4. El prompt generado aparecerá en el área de texto grande.
5. Para copiar el prompt al portapapeles, haga clic en el botón "Copiar al Portapapeles".
6. Las recetas guardadas se mostrarán en la tabla en la parte inferior de la ventana.
7. El software guardará automáticamente las recetas en un archivo `recipes.json` en el mismo directorio que el ejecutable.

## Características

- Genera prompts de recetas en formato JSON.
- Guarda automáticamente las recetas para evitar duplicados.
- Mantiene un registro permanente de las recetas en un archivo JSON.
- Interfaz gráfica fácil de usar.

## Creación del Archivo Ejecutable

Si necesita crear el archivo ejecutable (.exe) a partir del código fuente, siga estos pasos:

1. Asegúrese de tener Python y PyInstaller instalados en su sistema.
2. Abra una ventana de comando (CMD) o PowerShell.
3. Navegue hasta el directorio donde se encuentra el archivo `PromptBuilder.py`.
4. Ejecute el siguiente comando:

   ```
   python -m PyInstaller --onefile --windowed .\PromptBuilder.py
   ```

5. Una vez completado el proceso, encontrará el archivo `PromptBuilder.exe` en la carpeta `dist`.

## Notas

- Asegúrese de que el archivo `recipes.json` esté en el mismo directorio que el ejecutable para mantener el registro de recetas.
- La primera vez que ejecute el .exe, Windows puede mostrar una advertencia de seguridad. Esto es normal para aplicaciones no firmadas. Puede hacer clic en "Más información" y luego en "Ejecutar de todas formas" para abrir la aplicación.

Para cualquier problema o sugerencia, por favor contacte al desarrollador.
