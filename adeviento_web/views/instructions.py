import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import TextColor
from adeviento_web.components.button import button
import adeviento_web.constants as constants


def instructions() -> rx.Component():
    return rx.box(
        rx.vstack(
            rx.text("¿How does the event work?", class_name="title",
                    color=TextColor.ACCENT.value),
            rx.chakra.span(
                "• From December 1st to 24th I will discover a new gift on the calendar every day."),
            rx.chakra.span(
                "• You can participate from anywhere in the world."),
            rx.chakra.span(
                "• You will only have to retweet the post that I will link from this website. Your X account must be public."),
            button("Twitter", constants.TWITCH_URL),
            rx.chakra.span(
                "• The next day I will make the draw public and share the winner on the website and on X."),
            button("Twitter", constants.TWITCH_URL),
            rx.chakra.span(
                "• ¡Back to the drawing board! I will post a new gift and the process will start over."),
            class_name="nes-container is-dark with-title",
            width="100%",
            align_items="start"
        ),
        style=styles.max_width_style
    )
