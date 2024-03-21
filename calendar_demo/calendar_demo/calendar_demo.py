"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx
from reflex_calendar import calendar


class Foo(rx.State):

    def active_start_date_change_handler(self, var):
        print("active start date change handler:", var)

    def change_handler(self, var):
        print("change handler:", var)

    def click_day_handler(self, var):
        print("click day handler:", var)

    def click_month_handler(self, var):
        print("click month handler:", var)

    def click_decade_handler(self, var):
        print("click decade handler:", var)

    def click_year_handler(self, var):
        print("click year handler:", var)

    def click_week_number_handler(self, var):
        print("click week number handler:", var)

    def drill_down_handler(self, var):
        print("drill down handler:", var)

    def drill_up_handler(self, var):
        print("drill up handler:", var)

    def view_change_handler(self, var):
        print("view change handler:", var)


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            calendar(
                go_to_range_start_on_select=True,
                on_active_start_date_change=Foo.active_start_date_change_handler,
                on_change=Foo.change_handler,
                on_click_day=Foo.click_day_handler,
                on_click_month=Foo.click_month_handler,
                on_click_decade=Foo.click_decade_handler,
                on_click_year=Foo.click_year_handler,
                on_click_week_number=Foo.click_week_number_handler,
                on_drill_down=Foo.drill_down_handler,
                on_drill_up=Foo.drill_up_handler,
                on_view_change=Foo.view_change_handler,
                # color=rx.color("jade", 10),
            ),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        theme_panel=True,
        # appearance="light",
    )
)
app.add_page(index)
