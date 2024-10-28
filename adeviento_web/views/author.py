import reflex as rx
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
import adeviento_web.constants as constants
from adeviento_web.styles.styles import Size, Color
from adeviento_web.styles.colors import TextColor
import adeviento_web.styles.styles as styles
import datetime


def author() -> rx.Component:
    return rx.vstack(
        header_text(
            "like",
            "Hello, my name is Dorian Hidalgo"
        ),
        rx.flex(
            rx.avatar(
                name="Dorian Hidalgo",
                size="2xl",
                src="AdventCalendar.jpg",
                bg=Color.PRIMARY.value,
                padding="2px",
                border="4px",
                border_color=Color.SECONDARY.value,
                margin_right=Size.SMALL.value,
                margin_bottom=Size.SMALL.value
            ),
            rx.vstack(
                rx.chakra.span(
                    f"I have been a software engineer for more than {
                        experience()} años."
                ),
                rx.chakra.span(
                    "In 2019 I started to spread content about programming and software development on social networks such as ",
                    rx.chakra.span(
                        "@< Dev. Dorian />",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                ),
                # rx.mobile_only(
                #    rx.vstack(
                #        _author_buttons()
                #    )
                # ),
                # rx.tablet_and_desktop(
                #   rx.hstack(
                _author_buttons(),
                #    )
                # ),
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing=Size.BIG.value,
            flex_direction=["column", "column", "column", "row", "row"]
        ),
        style=styles.max_width_style
    )


def _author_buttons() -> rx.Component:
    return rx.stack(
        button("GitHub.", constants.GITHUB_URL),
        button("YouTube", constants.YOUTUBE_URL),
        button("Twitch", constants.TWITCH_URL),

        align_items="start",
    )


def experience() -> int:
    return datetime.date.today().year - 2017
