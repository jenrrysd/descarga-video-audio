#!/bin/bash
#
if [[ "$(which python3 )" = "/usr/bin/python3" && "$(which yt-dlp)" = '/usr/bin/yt-dlp' ]]; then
echo -e "SE COMPRUEBA QUE:
         -----------------
         python3-tkinter
         tk
         yt-dlp
         -----------------
         SÍ ESTÁ INSTALADO,
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
echo -e "PORFAVOR INSTALAR:
         ------------------
         python3-tkinter
         tk
         yt-dlp
         ------------------
         Y LUEGO VOLVER A EJECUTAR ESTE SCRIPT"
fi
