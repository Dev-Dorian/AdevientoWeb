import reflex as rx
from adeviento_web.styles.styles import Size, TextColor
import adeviento_web.styles.styles as styles
import adeviento_web.constants as constants


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Advent Calendar 2024",
            size="lg",
            padding_bottom=Size.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src="AdventCalendar.jpg",
                alt="Pixel art image of DevDorian with Christmas style",
                width="16em",
                height="16em",
                margin_right=Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("24 days. 24 gifts"),
                    rx.text("From December 1st to 24th"),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.chakra.span("For the third year, !here is our surprise advent calendar",
                               rx.chakra.span(" developer community",
                                              color=TextColor.ACCENT.value,
                                              font_size=Size.DEFAULT.value),
                               "!"
                               ),

                rx.chakra.span(
                    "An activity in which every day I will raffle a gift related to programming and software development (books, courses...)."),
                rx.chakra.span(
                    "Its purpose is to help share knowledge and promote community learning."),
                rx.chakra.link("#Advent2024",
                               href=constants.ADEVIENTO_HASHTAG_URL,
                               is_external=True,
                               color=TextColor.TERTIARY.value,
                               # padding_top=Size.BIG.value,
                               # font_size=Size.MEDIUM.value
                               ),
                align_items="start",
            ),
            flex_direction=["column", "column", "column", "row", "row"]
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style
    )
