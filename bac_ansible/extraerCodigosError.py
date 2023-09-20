import re

def extraerCodigosError(path_File_CodError, path_File_Log, path_File_Output):
    # Leer los códigos de error desde el archivo "codigos de error.txt"
    with open(path_File_CodError, 'r') as file:
        cods_errores = file.read()

    # Eliminar líneas que comienzan con '#' del contenido
    cods_errores = re.sub(r'#.*\n', '', cods_errores)

    # Reemplazar comas y saltos de línea con el operador de alternancia '|'
    cods_errores = re.sub(r'[,\n]', '|', cods_errores)

    # Remover posibles duplicados de |
    cods_errores = re.sub(r'\|+', '|', cods_errores)

    # Leer el contenido del archivo log
    with open(path_File_Log, 'r') as file:
        texto = file.read()

    ##Solo Separa cada parrafo de error entre separadores
    resultados = re.findall(r'^-{5,}\s(?:.+?)\s-{5,}\n([\s\S]*?)(?=^-{5,}|\Z)', texto, re.MULTILINE)

    # Filtrar resultados que contienen los códigos de error
    resultados_con_errores = [contenido for contenido in resultados if re.search(cods_errores, contenido)]

    # Guardar los resultados en un archivo
    with open(path_File_Output, 'w') as file:
        for contenido in resultados_con_errores:
            file.write(contenido.strip() + "\n")