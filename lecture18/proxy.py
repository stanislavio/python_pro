class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image from file: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")


class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def display(self):
        if self.image is None:
            self.image = RealImage(self.filename)
        self.image.display()


proxy1 = ImageProxy("image1.jpg")
proxy2 = ImageProxy("image2.jpg")

proxy1.display()

proxy1.display()

proxy2.display()
