from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import os
import subprocess
from android.permissions import request_permissions, Permission

# एन्ड्रोइडमा फाइल सेभ गर्न पर्मिसन माग्ने
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

class AVToolApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # शीर्षक
        self.label = Label(
            text="NARESH AV MULTI-TOOLBOX\nMade by Naresh Kushmi", 
            size_hint=(1, 0.2),
            halign="center"
        )
        self.root_layout.add_widget(self.label)

        # स्क्रोल गर्न मिल्ने मेनु
        scroll = ScrollView()
        menu = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        menu.bind(minimum_height=menu.setter('height'))

        # बटनहरू थप्ने
        actions = [
            ("Video Compressor (H.265)", self.run_compressor),
            ("Audio to Video (Visualizer)", self.run_visualizer),
            ("Quick Audio Converter (MP3)", self.run_converter),
            ("FM Radio Mixer", self.run_mixer),
            ("Audio Trimmer", self.run_trimmer)
        ]

        for text, func in actions:
            btn = Button(text=text, size_hint_y=None, height=100)
            btn.bind(on_press=func)
            menu.add_widget(btn)

        scroll.add_widget(menu)
        self.root_layout.add_widget(scroll)
        return self.root_layout

    # यहाँ तपाईँको पुराना logic हरूलाई function भित्र राख्नुहोस्
    def run_compressor(self, instance):
        self.label.text = "Status: Compressing Video..."
        # तपाईँको AVTool.py को Compressor logic यहाँ राख्ने

    def run_visualizer(self, instance):
        self.label.text = "Status: Generating Visualizer..."

    def run_converter(self, instance):
        self.label.text = "Status: Converting to MP3..."

    def run_mixer(self, instance):
        self.label.text = "Status: Mixing FM Audio..."

    def run_trimmer(self, instance):
        self.label.text = "Status: Opening Trimmer..."

if __name__ == "__main__":
    AVToolApp().run()
