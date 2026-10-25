este proyecto monitorea la estabilidad de la conexion de internet, cada 5 segundos hace un ping a 8.8.8.8 (Google DNS) y si falla, lo guarda en un archivo de bitacora_caidas.txt que se puede descargar y revisar 
#como usar
ejecuta en python monitor.py
para detener CTRL + C
revisar: bitacora_caidas.txt

#tecnologias usadas
python
libreria subprocess para ping
manejo de archivos y fecha/hora

autor : jose joaquin lemus gomez 
