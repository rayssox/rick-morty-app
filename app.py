import os
import repli:contentReference[oaicite:0]{index=0}─────────────────────────────
# This will let the Replicate client authenticate.:contentReference[oaicite:1]{index=1}EL MAP ──────────────────────────────────────────────────
# You can extend this with other pu:contentReference[oaicite:2]{index=2}"Cartoon Diffusion":     "lambdalabs/cartoon-diffusion"
}

def generate_style(image_path, style):
    """
 :contentReference[oaicite:3]{index=3}rns the URL of the transformed image.
    """
    model_id = STYLE_MODEL_MAP.get(style)
    if not m:contentReference[oaicite:4]{index=4} file for you
    output = replicate.run(
        model_id,
        input={"image": image_path}
    )
    return output  # usually a URL or direct image bytes, depending :contentReference[oaicite:5]{index=5}) as demo:
    gr.Markdown("## 🎨 Cartoonize Your Photo")
    with g:contentReference[oaicite:6]{index=6}                choices=list(STYLE_MODEL_MAP.keys()),
                value="A:contentReference[oaicite:7]{index=7}= gr.Image(type="filepath", label="Upload Your Photo")
            submit = gr.Button("Generate")
        with gr.Column():
            resu:contentReference[oaicite:8]{index=8}s=[image, style],
        outputs=result
    )

# ─── LAUNCH ───────────────────────────────────────────────────────────────────
if __name__ == ":contentReference[oaicite:9]{index=9}or local dev
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
