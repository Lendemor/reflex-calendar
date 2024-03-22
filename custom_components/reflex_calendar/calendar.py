"""Reflex custom component Calendar."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

from datetime import datetime, timezone, tzinfo
from typing import Any, Literal

import pytz

import reflex as rx
from reflex.utils import format, imports

LiteralCalendarType = Literal["gregory", "hebrew", "islamic", "iso8601"]
LiteralDefaultView = Literal["month", "year", "decade", "century"]
LiteralReturnValue = Literal["start", "end", "range"]


class Calendar(rx.Component):
    """Calendar component."""

    # The React library to wrap.
    library = "react-calendar@4.8.0"

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

    def _get_imports(self) -> imports.ImportDict:
        return imports.merge_imports(
            super()._get_imports(),
            {
                "": {
                    imports.ImportVar(
                        tag=f"{format.format_library_name(self.library)}/dist/Calendar.css"
                    )
                },
            },
        )

    @classmethod
    def create(cls, *children, **props) -> "Calendar":
        """Create a Calendar component."""
        style = props.pop("style", {})
        style["color"] = props.pop("color", rx.color("accent", 11))
        style["background_color"] = props.pop("background_color", rx.color("accent", 1))
        props["style"] = style

        return cls(*children, **props)

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_active_start_date_change": lambda e0: [e0],
            "on_change": lambda e0: [e0],
            "on_click_day": lambda e0: [e0],
            "on_click_decade": lambda e0: [e0],
            "on_click_month": lambda e0: [e0],
            "on_click_week_number": lambda e0: [e0],
            "on_click_year": lambda e0: [e0],
            "on_drill_down": lambda e0: [e0],
            "on_drill_up": lambda e0: [e0],
            "on_view_change": lambda e0: [e0],
        }

    # To add custom code to your component
    # def _get_custom_code(self) -> str:
    # return f"const customCode = 'customCode';"


def fix_timezone(date: str, tz: tzinfo | str | None = None):
    """Small helper to fix the timezone of date return by Calendar."""
    tz = tz or datetime.now(timezone.utc).astimezone().tzinfo
    if isinstance(tz, str):
        tz = pytz.timezone("Europe/Berlin")
    print(tz)
    return datetime.fromisoformat(date).astimezone(tz).isoformat()


calendar = Calendar.create
