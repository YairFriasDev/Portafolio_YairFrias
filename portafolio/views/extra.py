# portafolio/views/extra.py

import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.data import Extra
from portafolio.styles.styles import Size

def extra(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        # Título actualizado
        heading("Upcoming Certifications"),

        # Vista móvil: lista vertical
        rx.mobile_only(
            rx.vstack(
                *[card_detail(extra) for extra in extras],
                spacing=Size.DEFAULT.value
            ),
            width="100%"
        ),

        # Vista tablet/escritorio: grid de 3 columnas
        rx.tablet_and_desktop(
            rx.grid(
                *[card_detail(extra) for extra in extras],
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),

        spacing=Size.DEFAULT.value,
        width="100%"
    )
