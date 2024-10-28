import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, TextColor
import adeviento_web.constants as constants


def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Advent Calendar 2024",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value

            ),
            rx.chakra.link(
                "Create with ",
                rx.box(class_name="nes-icon is-small heart"),
                " (and thanks to you) por < Dev. Dorian /> by Dorian Hidalgo",
                href=constants.DEVDORIAN_URL,
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.TERTIARY.value
            ),
            align_items="start",
            spacing=Size.MEDIUM.value
        ),
        rx.spacer(),
        rx.image(
            src="logo.png",
            class_name="nes-avatar is-large"
        ),
        padding_bottom=Size.BIG.value,
        style=styles.max_width_style,
        align_items="center"
    )
