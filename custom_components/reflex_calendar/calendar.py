"""Reflex custom component Calendar."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

from datetime import datetime
from typing import Literal

import reflex as rx
from reflex.utils import format

LiteralCalendarType = Literal["gregory", "hebrew", "islamic", "iso8601"]
LiteralDefaultView = Literal["month", "year", "decade", "century"]
LiteralReturnValue = Literal["start", "end", "range"]


def _on_active_start_date_change_spec(e0: dict):
    return [
        rx.Var(f"{{...{e0}, activeStartDate: {e0}.activeStartDate.toDateString()}}")
    ]


def _on_change_spec(date: str) -> list[rx.Var]:
    return [
        rx.cond(
            rx.Var(f"Array.isArray({date})"),
            rx.Var(f"{date}.map(d => d.toDateString())"),
            rx.Var(f"{date}.toDateString()"),
        ),
    ]


def _on_click_day_spec(date: str) -> list[rx.Var]:
    return [rx.Var(f"{date}.getDate()")]


def _on_click_month_spec(date: str) -> list[rx.Var]:
    return [rx.Var(f"{date}.getMonth()+1")]


def _on_click_week_number_spec(date: str) -> list[rx.Var]:
    return [rx.Var(f"{date}.getDay()")]


def _on_click_year_spec(date: str) -> list[rx.Var]:
    return [rx.Var(f"{date}.getFullYear()")]


def _on_click_decade_spec(date: str) -> list[rx.Var]:
    return [rx.Var(f"{date}.getFullYear()")]


def _on_drill_down_spec(e0: dict) -> list[rx.Var]:
    return [rx.Var(f"{e0}.view")]


def _on_drill_up_spec(e0: dict) -> list[rx.Var]:
    return [rx.Var(f"{e0}.view")]


def _on_view_change_spec(e0: dict) -> list[rx.Var]:
    return [e0]


class Calendar(rx.Component):
    """Calendar component."""

    # The React library to wrap.
    library: str = "react-calendar@5.1.0"

    # lib_dependencies: list[str] = []

    # The React component tag.
    tag = "Calendar"

    # If the tag is the default export from the module, you must set is_default = True.
    # This is normally used when components don't have curly braces around them when importing.
    is_default = True

    # If you are wrapping another components with the same tag as a component in your project
    # you can use aliases to differentiate between them and avoid naming conflicts.
    alias = "ReflexCalendar"

    # The props of the React component.

    # The active start date. (need serialization to new Date())
    # active_start_date: rx.Var[datetime]

    # Whether to allow partial range selections. (default: False)
    allow_partial_range: rx.Var[bool]

    # The calendar type.
    calendar_type: rx.Var[LiteralCalendarType]

    # The default value of the component. (need serialization to new Date())
    default_value: rx.Var[str]

    # The default view of the component. Does not disable navigation. (default: "month")
    default_view: rx.Var[LiteralDefaultView]

    # Formatting callbacks, need specific implementation.
    # format_day
    # format_long_date
    # format_month
    # format_month_year
    # format_short_weekday
    # format_weekday
    # format_year

    # Whether to go to the beginning of the range when selecting the end of the range.
    go_to_range_start_on_select: rx.Var[bool]

    # Locale that should be used by the calendar.
    locale: rx.Var[str]

    # Maximum date that the user can select. Periods partially overlapped by maxDate will also be selectable, although react-calendar will ensure that no later date is selected.
    max_date: rx.Var[str]

    # The most detailed view that the user shall see.
    max_detail: rx.Var[LiteralDefaultView]

    # Minimum date that the user can select. Periods partially overlapped by minDate will also be selectable, although react-calendar will ensure that no earlier date is selected.
    min_date: rx.Var[str]

    # The least detailed view that the user shall see.
    min_detail: rx.Var[LiteralDefaultView]

    # aria-label attribute of a label rendered on calendar navigation bar.
    navigation_aria_label: rx.Var[str]

    # aria-live attribute of a label rendered on calendar navigation bar.
    navigation_aria_live: rx.Var[str]

    # Content of a label rendered on calendar navigation bar.
    navigation_label: rx.Var[str]

    # aria-label attribute of the "next on higher level" button on the navigation pane.
    next_2_aria_label: rx.Var[str]

    # Content of the "next on higher level" button on the navigation pane. Setting the value explicitly to null will hide the icon.
    next_2_label: rx.Var[str]

    # aria-label attribute of the "next" button on the navigation pane.
    next_aria_label: rx.Var[str]

    # Content of the "next" button on the navigation pane. Setting the value explicitly to null will hide the icon.
    next_label: rx.Var[str]

    # aria-label attribute of the "previous on higher level" button on the navigation pane.
    prev_2_aria_label: rx.Var[str]

    # Content of the "previous on higher level" button on the navigation pane. Setting the value explicitly to null will hide the icon.
    prev_2_label: rx.Var[str]

    # aria-label attribute of the "previous" button on the navigation pane.
    prev_aria_label: rx.Var[str]

    # Content of the "previous" button on the navigation pane. Setting the value explicitly to null will hide the icon.
    prev_label: rx.Var[str]

    # Which date should be returned by on_change and on_click{Period}. (default: "start")
    return_value: rx.Var[LiteralReturnValue]

    # Whether the user shall select two dates forming a range instead of just one.
    select_range: rx.Var[bool]

    # Whether to show two months/years/… at a time instead of one. Defaults showFixedNumberOfWeeks prop to be true.
    show_double_view: rx.Var[bool]

    # Whether to always show fixed number of weeks (6). Forces showNeighboringMonth prop to be true. (default: False)
    show_fixed_number_of_weeks: rx.Var[bool]

    # Whether a navigation bar shall be rendered. (default: True)
    show_navigation: rx.Var[bool]

    # Whether decades from next century shall be rendered to fill the entire last row in. (default: False)
    show_neighouring_century: rx.Var[bool]

    # Whether the year of the next decade will be rendered to fill last line (default: False)
    show_neighbouring_decade: rx.Var[bool]

    # Whether to show the day of the previous/next months if the month doesn't start/end exactly on the beginning/end of a week. (default: True)
    show_neighbouring_month: rx.Var[bool]

    # Whether to show the week numbers. (default: False)
    show_week_numbers: rx.Var[bool]

    # The value of the component.
    value: rx.Var[str]

    # The view of the component. (default: the most detailed view allowed by min_detail and max_detail)
    view: rx.Var[LiteralDefaultView]

    # Triggered when the active start date changes.
    on_active_start_date_change: rx.EventHandler[_on_active_start_date_change_spec]

    # Triggered when the user changes the value.
    on_change: rx.EventHandler[_on_change_spec]

    # Triggered when the user clicks on a day.
    on_click_day: rx.EventHandler[_on_click_day_spec]

    # Triggered when the user clicks on a month.
    on_click_month: rx.EventHandler[_on_click_month_spec]

    # Triggered when the user clicks on a week number.
    on_click_week_number: rx.EventHandler[_on_click_week_number_spec]

    # Triggered when the user clicks on a year.
    on_click_year: rx.EventHandler[_on_click_year_spec]

    # Triggered when the user clicks on a decade.
    on_click_decade: rx.EventHandler[_on_click_decade_spec]

    # Triggered when the user navigates to a lower level view.
    on_drill_down: rx.EventHandler[_on_drill_down_spec]

    # Triggered when the user navigates to a higher level view.
    on_drill_up: rx.EventHandler[_on_drill_up_spec]

    # Use on_view_change to get the full event.
    on_view_change: rx.EventHandler[_on_view_change_spec]

    def add_imports(self) -> dict[str, rx.ImportVar]:
        """Add imports for the component."""
        return {
            "": rx.ImportVar(
                tag=f"{format.format_library_name(self.library)}/dist/Calendar.css"
            )
        }

    @classmethod
    def create(cls, *children, **props) -> "Calendar":
        """Create a Calendar component."""
        style = props.pop("style", {})
        style["color"] = props.pop("color", rx.color("accent", 11))
        style["background_color"] = props.pop("background_color", rx.color("accent", 1))
        props["style"] = style

        return cls(*children, **props)


calendar = Calendar.create


def reformat_date(date: str, output_format: str = "%Y-%m-%d") -> datetime:
    """Reformat a date."""
    return datetime.strptime(date, "%a %b %d %Y").strftime(output_format)
