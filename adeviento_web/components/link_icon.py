import reflex as rx
from adeviento_web.styles.styles import Size


def link_icon(icon: str, url: str) -> rx.Component:
    return rx.chakra.link(
        "",
        class_name=f"nes-icon {icon} is-medium",
        href=url,
        is_external=True,
        margin_top=Size.ZERO.value,
        margin_left=Size.MEDIUM.value
    )
