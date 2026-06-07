import pywhatkit
import time

from utils.validator import (
    validate_phone,
    normalize_phone
)

from services.logger_service import (
    log_message
)


class WhatsAppService:

    def send_message(self, phone, message):

        try:

            phone = normalize_phone(phone)

            if not validate_phone(phone):
                raise ValueError(
                    f"Invalid Phone Number: {phone}"
                )

            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone,
                message=message,
                wait_time=15,
                tab_close=True,
                close_time=3
            )

            time.sleep(5)

            log_message(
                phone,
                message,
                "SENT"
            )

            return True

        except Exception as e:

            log_message(
                phone,
                message,
                f"FAILED: {e}"
            )

            raise