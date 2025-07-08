# portafolio/views/header.py

import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import Size

def header(data: Data) -> rx.Component:
    return rx.hstack(
        # Avatar con halo luminoso
        rx.avatar(
    src=data.avatar,
    size=Size.BIG.value,
    class_name="halo-effect",
    style={
        # sombra inicial suave
        "filter": "drop-shadow(0 0 8px #22C55E)",
        # animación que alterna entre sombra pequeña y sombra grande
        "animation": "glow 1.5s ease-in-out infinite alternate"
        }
        ),

        # Nombre, skill, ubicación y redes
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            media(data.media),
            spacing=Size.SMALL.value,
        ),

        # Empuja los botones al extremo derecho
        rx.spacer(),

        # Botón lunita para alternar tema
        rx.link(
            rx.icon("moon"),
            href="javascript:toggleTheme()",
            class_name="circle-button"
        ),

        spacing=Size.DEFAULT.value,
        class_name="items-center py-4 px-6"
    )
