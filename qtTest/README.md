Ejemplo utilizando qt4

Compilado con PyInstaller v3.1.1. La version de PyInstaller 3.2 se tilda en Looking for dynamic libraries cuando se genera el spec file.

Agrego el dosisV1.spec donde incluyo como se agrega el ui al proyecto.

Compila corriendo:

python -m PyInstaller --name dosisV1 dosisTest/dosisV1.py

python -m PyInstaller --name dosisV1 dosisTest/dosisV1.py