import reflex as rx
from adeviento_web.styles.styles import Size, Color


def day(number: int, text: str = "", url: str = "", finished=False) -> rx.Component:
    return rx.box(
        rx.cond(
            url != "",
            rx.chakra.link(
                rx.image(
                   src=f"calendar/{number}.png",
                    alt=text,
                    padding=Size.SMALL.value
                ),
                href=url,
                is_external=True,
                position="absolute"
            )
        ),
        rx.cond(
            url == "",
            rx.image(
                src="gift.png",
                alt=f"Regalo asociado al dia {number}.",
                position="absolute",
                padding=Size.SMALL.value
            )
        ),
        rx.text(
            number,
            padding=Size.DEFAULT.value,
            position="absolute"
        ),
        bg=Color.ACCENT.value if finished else Color.TERTIARY.value if url != "" else Color.SECONDARY.value,
        # width="100%",
        aspect_ratio="1",
        position="relative"
    )
