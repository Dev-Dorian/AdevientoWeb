import reflex as rx
from adeviento_web.styles.styles import Size, Color
from adeviento_web.components.link_icon import link_icon
import adeviento_web.constants as constants


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="AdventCalendar.jpg",
                alt="Pixel art image of DevDorian with Christmas style",
                width="3em",
                height="3em"
            ),
            rx.text("Advent Calendar 2024"),
            rx.spacer(),
            # rx.tablet_and_desktop(
            link_icon("github", constants.GITHUB_URL),
            link_icon("youtube", constants.YOUTUBE_URL),
            link_icon("twitch", constants.TWITCH_URL),
            # ),
            width="100%",
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )
