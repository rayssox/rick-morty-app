import gradio as gr
import replicate
import os

client = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

def generate_anime_style(image):
    output = client.run(
        "fofr/anything-to-anime:4b14dc403b4ca44aa657f9261b31e923b32ec8c30b8e896c703b71eabfcd4dfb",
        input={"image": open(image.name, "rb")}
    )
    return output

gr.Interface(fn=generate_anime_style, 
             inputs=gr.Image(type="file"), 
             outputs="image").launch(server_port=int(os.environ.get('PORT', 7860)))
