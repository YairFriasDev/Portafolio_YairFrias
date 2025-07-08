import reflex as rx
from portafolio.styles.styles import Size


def heading(text: str, h1=False) -> rx.Component:
    # Si no es h1, aplica la clase typing-effect para el efecto de máquina de escribir
    return rx.heading(
        text,
        as_="h1" if h1 else "h2",
        size=Size.BIG.value if h1 else Size.MEDIUM.value,
        class_name="" if h1 else "typing-effect",
        style={"color": "#4E635B"}
    )