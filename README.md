# calendar

A Reflex custom component calendar wrapping the [react-calendar](https://www.npmjs.com/package/react-calendar) component.

## Installation

```bash
pip install reflex-calendar
```

## Usage

```python
from reflex_calendar import calendar

def index():
    return calendar()
```

### Props:
- `go_to_range_start_on_select`: Go to the start of the range when selecting a range.
- `value`: The date value.
- `locale`: The locale.
- `min_date`: The minimum date.
- `max_date`: The maximum date.
- `min_detail`: The minimum detail.
- `max_detail`: The maximum detail.
- `navigation_label`: The navigation label.
- `next2_label`: The next2 label.
- `next_label`: The next label.
- `prev2_label`: The prev2 label.
- `prev_label`: The prev label.
- `select_range`: The select range.
- `show_double_view`: Show double view.
- `show_fixed_number_of_weeks`: Show fixed number of weeks.
- `show_navigation`: Show navigation.
- `show_neighboring_month`: Show neighboring month.
- `show_neighboring_century`: Show neighboring century.
- `show_neighboring_decade`: Show neighboring decade.
- `show_week_numbers`: Show week numbers.

### Event triggers:

- `on_change`: Triggered when the date is changed. (return the date)
- `on_click_day`: Triggered when a day is clicked. (return the full date)
- `on_click_month`: Triggered when a month is clicked. (return a date at start/end of the month)
- `on_click_year`: Triggered when a year is clicked. (return a date at start/end of the year)
- `on_click_decade`: Triggered when a decade is clicked. (return a date at start/end of the decade)
- `on_click_week_number`: Triggered when a week number is clicked. (return a date at start/end of the week)
- `on_drill_down`: Triggered when the calendar is drilled down. (return the event)
- `on_drill_up`: Triggered when the calendar is drilled up. (return the event)
- `on_view_change`: Triggered when the view is changed. (return the event)

When returning an event, it's a dictionary with the following keys:
- `action`: The action.
- `activeStartDate`: The start date in the resulting view.
- `value`: The value.
- `view`: The view where the event happened.
