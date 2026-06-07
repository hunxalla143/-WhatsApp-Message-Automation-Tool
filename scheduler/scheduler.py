import schedule
import time

class MessageScheduler:

    def schedule_message(
        self,
        send_function,
        schedule_time
    ):

        schedule.every().day.at(
            schedule_time
        ).do(send_function)

        print(
            f"Message Scheduled at {schedule_time}"
        )

        while True:
            schedule.run_pending()
            time.sleep(1)