from datetime import datetime

from tools.decorator import tool


class DateTimeTools:

    @staticmethod
    @tool(
        name="current_time",
        description="Return the current local time"
    )
    def current_time():

        return datetime.now().strftime(
            "🕒 %I:%M:%S %p"
        )

    @staticmethod
    @tool(
        name="current_date",
        description="Return today's date"
    )
    def current_date():

        return datetime.now().strftime(
            "📅 %d %B %Y"
        )