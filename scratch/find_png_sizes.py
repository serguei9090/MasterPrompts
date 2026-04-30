import os
import struct

def get_png_info():
    matches = []
    for root, dirs, files in os.walk('.'):
        if '.venv' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.png'):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'rb') as f:
                        f.seek(16)
                        data = f.read(8)
                        if len(data) == 8:
                            w, h = struct.unpack('>II', data)
                            matches.append((full_path, w, h))
                except Exception:
                    continue
    return matches

if __name__ == '__main__':
    for path, w, h in get_png_info():
        print(f"{w}x{h} - {path}")
