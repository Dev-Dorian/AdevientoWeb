import reflex as rx
import adeviento_web.constants as constants
from adeviento_web.styles.styles import Size, Color
from adeviento_web.styles.colors import TextColor
import adeviento_web.styles.styles as styles
from adeviento_web.components.header_text import header_text


def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text(
                "star",
                "Sponsored by",
                False
            ),
            rx.text(
                "With the support of the community and sponsors I will cover the cost of the 24 gifts. Imagine your logo here and in all daily communications during the event."
            ),
            rx.chakra.span(
                "¿Do you want to support this initiative? Write to me..."
            ),
            spacing=Size.BIG.value,
            padding_y=Size.VERY_BIG.value,
            style=styles.max_width_style
        ),
        bg=Color.ACCENT.value,
        width="100%"
    )
