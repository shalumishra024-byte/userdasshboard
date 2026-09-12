import os
from PIL import Image

assets_dir = r"d:\SAMVEDNA\extracted_assets"

# 1. Crop Flow of Project (top diagram only, removing B2B model)
p3_flow = os.path.join(assets_dir, "p3_img5_110_1024x1536.jpeg")
if os.path.exists(p3_flow):
    with Image.open(p3_flow) as img:
        # Crop top 915 pixels
        cropped = img.crop((0, 0, img.width, 915))
        out_path = os.path.join(assets_dir, "p3_flow_clean.png")
        cropped.save(out_path)
        print(f"Saved: {out_path} ({cropped.size})")

print("Asset preparation complete!")
