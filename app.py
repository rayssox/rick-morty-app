import os
import cv2
import numpy as np
import gradio as gr

def cartoonify(image: np.ndarray) -> np.ndarray:
    """
    OpenCV’nin stylization filtresiyle çizgi film efekti uygular.
    """
    # Gradio’dan gelen RGB’yi BGR’ye çevir
    img_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # stylization: sigma_s uzaysal yumuşatma, sigma_r renk aralığı yumuşatma
    cartoon_bgr = cv2.stylization(img_bgr, sigma_s=150, sigma_r=0.25)
    # tekrar RGB’ye çevir ve döndür
    return cv2.cvtColor(cartoon_bgr, cv2.COLOR_BGR2RGB)

with gr.Blocks() as demo:
    gr.Markdown("## 🖼️ Fotoğrafını Yükle – Çizgi Filme Dönüştürelim!")
    with gr.Row():
        inp = gr.Image(source="upload", type="numpy", label="Fotoğraf Yükle")
        out = gr.Image(type="numpy", label="Çizgi Film Versiyonu")
    btn = gr.Button("Çizgi Filme Dönüştür!")
    btn.click(fn=cartoonify, inputs=inp, outputs=out)

if __name__ == "__main__":
    # Render’ın verdiği PORT’u ya da lokalde 7860’ı kullan
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
