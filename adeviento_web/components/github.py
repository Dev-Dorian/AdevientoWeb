import reflex as rx
import adeviento_web.constants as constants
from adeviento_web.styles.styles import Size, Color


def github() -> rx.Component:
    return rx.chakra.link(
        rx.hstack(
            rx.vstack(
                rx.vstack(

                    rx.chakra.span("Proyect"),
                    rx.chakra.span("on GitHub"),
                    align_items="start",
                    class_name="nes-balloon from-right is-dark",
                    margin_bottom=Size.BIG.value
                ),
                rx.box(
                    rx.chakra.span(
                        constants.VERSION,
                        class_name="is-error"
                    ),
                    class_name="nes-badge"
                ),
                # width="50%",
            ),
            rx.box(
                class_name="nes-octocat animate"
            ),
            href=constants.GITHUB_URL,
            is_external=True,
            align_items="end",
            display="flex",
            margin_top=Size.ZERO.value,
        ),
        width="100%",
        align_items="end",
        justify_content="center",
        display="flex",
    )
