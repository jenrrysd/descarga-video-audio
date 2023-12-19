#!/bin/bash
#
if [[ "$(which python3 )" = "/usr/bin/python3" && "$(which yt-dlp)" = '/usr/bin/yt-dlp' ]]; then
echo -e "SE COMPRUEBA QUE python3-tkinter y yt-dlp SÍ ESTÁ INSTALDO, 
         SE PROCEDE CON LA INSTALCIÓN "

icono=$PWD/dva.png
ruta=$PWD/dva.py
sudo bash -c  'cat > /usr/share/applications/dva.desktop << EOF
[Desktop Entry]
Type=Application
Categories=Utilitario
Name=DVA
Comment=Descarga Video Audio
Icon='$icono'
Exec=/usr/bin/python '$ruta'
MimeType=image/jpeg;image/png;image/svg;
Terminal=false
EOF'

else
	echo -e "NO TIENES INSTALADO python3-tkinder y yt-dlp PORFAVOR INSTALAR
                 LO QUE SE PIDE Y LUEGO VOLVER A EJECUTAR ESTE SCRIPT"
fi
