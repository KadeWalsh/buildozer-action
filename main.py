from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import random

# Load the KV file
Builder.load_file("main.kv")


class RootWidget(BoxLayout):
    def on_button_press(self, value):
        if not self.answer:
            return
        print(self.ids.status_message.text)
        if value == self.answer:
            self.ids.status_message.text = "Correct!"
        else:
            self.ids.status_message.text = "Please try again!!"

    def generate_problem(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        total = num1 * num2
        self.answer = num2
        self.ids.total.text = f'{total}'
        self.ids.num1.text = f'{num1}'
        self.ids.status = 'Please select an answer from below'


class MyApp(App):
    title = "The DIVISION app"

    def build(self):
        # Return the root widget, which is defined in the KV file
        return RootWidget()


# Run the application
if __name__ == "__main__":
    MyApp().run()
