
import gradio as gr
from PIL import Image

def fake_rick_and_morty_style(image):
    image = image.resize((512, 512))
    return image

iface = gr.Interface(
    fn=fake_rick_and_morty_style,
    inputs=gr.Image(type="pil"),
    outputs="image",
    title="Rick and Morty Avatar Dönüştürücü",
    description="Fotoğrafını yükle, Rick and Morty stiline dönüşsün!"
)

iface.launch()
