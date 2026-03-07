import sys
import subprocess

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

def remove_white_bg(infile, outfile):
    img = Image.open(infile).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Check if the pixel is close to white
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            # Fully transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(outfile, "PNG")
    print(f"Saved {outfile}")

remove_white_bg("logo.png", "logo-transparent.png")
