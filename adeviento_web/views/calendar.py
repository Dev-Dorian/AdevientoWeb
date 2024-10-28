import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day


def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "heart", "Advent Calendar"
        ),
        rx.vstack(
            rx.hstack(
                rx.text("The event starts in"),
                rx.text(id="countdown"),
                align_items="start"
            ),
            button("Remember", constants.ADEVIENTO_HASHTAG_URL),
            rx.chakra.span(
                "The gifts are a surprise, they remain hidden until the day of publication."
            ),
            class_name="nes-container is-dark",
            align_items="start",
            width="100%"
        ),
        rx.chakra.responsive_grid(
            rx.foreach(list(range(1, 25)),
                       lambda number:
                       day(number)
                       ),
            columns=[3, 3, 4, 5, 6],
            width="100%"
        ),
        rx.script(src="/js/countdown.js"),
        style=styles.max_width_style
    )
