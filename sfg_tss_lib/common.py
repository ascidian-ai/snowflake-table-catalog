import os
from pathlib import Path

class common:
    os.chdir(Path(__file__).parent.parent)
    cwd = os.getcwd()

    app_name = "Snowflake Table Catalog (PoC)"
    app_description = "Platform to test chatGPT powered search of the snowflake table catalog."
    app_version = "0.1.20230831-alpha"
    app_copyright = ("Copyright(c)2022-2023. Steadfast Technologies Pty Ltd. All Rights Reserved. \n\n"
                     "This application is a proof of concept and is not intended for production use. \n\n"
                     "This application is a derivative implementation of the following github project:\n\n"
                     "https://github.com/mydgd/snowflake-table-catalog \n\n"
                     "Portions Copyright (c) 2022 Mustafa Aydogdu under an MIT Licence.")
    app_initial_sidebar_state = "expanded"

    logo_image=os.path.join('images', 'steadfast-logo.png')
    logo_size=128

    from PIL import Image
    page_icon = Image.open(os.path.join(cwd, 'images', 'steadfast-icon.ico'))
    page_layout = "wide"
