from PIL import Image, ImageChops
import base64
import io
from appium.webdriver.webdriver import WebDriver


class ImageUtils:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def take_screenshot_as_image(self) -> Image.Image:
        base64_screenshot = self.driver.get_screenshot_as_base64()
        screenshot_bytes = base64.b64decode(base64_screenshot)
        return Image.open(io.BytesIO(screenshot_bytes))

    def compare_images(self, img1: Image.Image, img2: Image.Image, tolerance: int = 50):
        diff = ImageChops.difference(img1, img2).convert('L')
        diff_pixels = sum(1 for pixel in diff.getdata() if pixel > 0)
        return diff_pixels <= tolerance, diff
