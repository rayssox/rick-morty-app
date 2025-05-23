import os
import gradio as gr
import replicate

# Replicate client token'ı environment değişkeninden al
client = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

def generate_anime_style(image):
    with open(image.name, "rb") as img_file:
        output = client.run(
            "fofr/anything-to-anime:4b14dc403b4ca44aa657f9261b31e923b32ec8c30b8e896c703b71eabfcd4dfb",
            input={"image": img_file}
        )
    return output

# Gradio arayüzü
demo = gr.Interface(
    fn=generate_anime_style,
    inputs=gr.Image(type="file", label="Fotoğrafını Yükle"),
    outputs="image",
    title="AI Anime Karaktere Dönüştürücü"
)

# Render ortamında çalışması için özel port ayarı
demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
