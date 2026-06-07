import pywhatkit

class MediaSender:

    def send_image(self, phone, image_path, caption=""):

        pywhatkit.sendwhats_image(
            receiver=phone,
            img_path=image_path,
            caption=caption
        )