from PIL import Image


class Picture:

    def __init__(self, path: str) -> None:
        self.path = path
        self._image = None

    def load(self) -> bool:
        try:
            self._image = Image.open(self.path)
            return True
        except Exception as e:
            print(f"Failed to load image {e}")
            return False
