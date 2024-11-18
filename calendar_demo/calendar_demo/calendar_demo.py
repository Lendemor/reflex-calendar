"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from reflex_calendar import calendar

import reflex as rx


class Foo(rx.State):
    selected_date: str = ""
    logs: list[str] = []

    def change_handler(self, var):
        self.selected_date = var
        return self.add_log(f"Changed selected date: {var}")

    def active_start_date_change_handler(self, var):
        if "drill" in var["action"]:
            return

        action = var["action"]
        start_date = var["activeStartDate"]
        return self.add_log(f"Changed active start date to {start_date} ({action})")

    def click_day_handler(self, day):
        return self.add_log(f"Clicked day {day}")

    def click_month_handler(self, month):
        return self.add_log(f"Clicked month {month}")

    def click_decade_handler(self, var):
        return self.add_log(f"Clicked decade {var}")

    def click_year_handler(self, year):
        return self.add_log(f"Clicked year {year}")

    def click_week_number_handler(self, var):
        return self.add_log(f"Clicked week number {var['week_number']}")

    def drill_down_handler(self, view):
        return self.add_log(f"Drilled down to: {view} view")

    def drill_up_handler(self, view):
        return self.add_log(f"Drilled up to: {view} view")

    def view_change_handler(self, event):
        return self.add_log(f"View changed to: {event['view']}")

    def clear_logs(self):
        self.logs = []

    def add_log(self, log):
        self.logs.append(log)
        if len(self.logs) > 20:
            self.logs.pop(0)
        return rx.toast(log, position="top-center")


def logs():
    return rx.vstack(
        rx.heading("Logs", size="6"),
        rx.foreach(
            Foo.logs,
            lambda log: rx.text(log, color="gray", size="3"),
        ),
        rx.spacer(),
        rx.button("Clear Logs", on_click=Foo.clear_logs, size="3", color_scheme="ruby"),
        align="center",
        width="50%",
        height="100%",
        spacing="1",
    )


def demo():
    return rx.vstack(
        rx.heading("Calendar Demo", size="6"),
        rx.moment(Foo.selected_date, format="MMMM D, YYYY", size="4"),
        calendar(
            go_to_range_start_on_select=True,
            locale="fr-FR",
            on_active_start_date_change=Foo.active_start_date_change_handler,
            on_change=Foo.change_handler,
            on_click_day=Foo.click_day_handler,
            on_click_month=Foo.click_month_handler,
            on_click_decade=Foo.click_decade_handler,
            on_click_year=Foo.click_year_handler,
            on_click_week_number=Foo.click_week_number_handler,
            on_drill_down=Foo.drill_down_handler,
            on_drill_up=Foo.drill_up_handler,
            # on_view_change=Foo.view_change_handler,
        ),
        align="center",
        width="50%",
    )


@rx.page()
def index() -> rx.Component:
    return rx.center(
        rx.hstack(
            demo(),
            logs(),
            align="center",
            spacing="7",
            width="100vw",
            height="70vh",
        ),
        width="100vw",
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
