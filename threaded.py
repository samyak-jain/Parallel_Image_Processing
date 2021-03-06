# Processing images by Doing The Simplest Thing
from pathlib import Path
from PIL import Image
from PIL import ImageFilter
import sys
import concurrent.futures

def start(algo):
    in_path = Path.cwd() / "images"
    out_path = Path.cwd() / "processed_thread"

    if not in_path.exists():
        print(f"Cannot find {in_path.name} directory")
        sys.exit(1)

    if not out_path.exists():
        out_path.mkdir()

    def process_one_file(filename):
        outfile = out_path / filename.name
        try:
            image = Image.open(filename)
            image = image.filter(algo)
            image.save(outfile, "JPEG")
        except IOError:
            print(f"Cannot create thumbnail for {filename.name}")

    names = list(in_path.glob("*")) #* 4

    import time
    start = time.time()
    executor = concurrent.futures.ThreadPoolExecutor(99)
    list(executor.map(process_one_file, names))
    return time.time() - start

# for image_file in in_path.glob("*"):
#     process_one_file(image_file)
