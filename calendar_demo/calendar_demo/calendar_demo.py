"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from reflex_calendar import calendar, fix_timezone

import reflex as rx


class Foo(rx.State):
    selected_date: str = ""
    logs: list[str] = []

    def remove_hours(self, var):
        var = fix_timezone(var)
        return var.split("T")[0]

    def change_handler(self, var):
        self.selected_date = self.remove_hours(var)

    def active_start_date_change_handler(self, var):
        if "drill" in var["action"]:
            return

        action = var["action"]
        start_date = self.remove_hours(var["activeStartDate"])
        self.add_log(f"Changed active start date to {start_date} ({action})")

    def click_day_handler(self, var):
        self.add_log(f"Clicked day {self.remove_hours(var).split('-')[-1]}")

    def click_month_handler(self, var):
        self.add_log(f"Clicked month {self.remove_hours(var).split('-')[1]}")

    def click_decade_handler(self, var):
        self.add_log(f"Clicked decade {self.remove_hours(var).split('-')[0]}")

    def click_year_handler(self, var):
        self.add_log(f"Clicked year {self.remove_hours(var).split('-')[0]}")

    def click_week_number_handler(self, var):
        self.add_log(f"Clicked week number {var['week_number']}")

    def drill_down_handler(self, var):
        self.add_log(f"Drilled down to: {var['view']} view")

    def drill_up_handler(self, var):
        self.add_log(f"Drilled up to: {var['view']} view")

    def view_change_handler(self, var):
        self.add_log(f"View changed to: {var['view']}")

    def clear_logs(self):
        self.logs = []

    def add_log(self, log):
        self.logs.append(log)
        if len(self.logs) > 20:
            self.logs.pop(0)


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
        rx.text(Foo.selected_date, size="3"),
        calendar(
            go_to_range_start_on_select=False,
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
app = rx.App(
    theme=rx.theme(
        # theme_panel=True,
        appearance="dark",
    )
)
app.add_page(index)
