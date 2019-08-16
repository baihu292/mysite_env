import os
from PIL import Image


def img_deal(file, path, color_data):
    try:
        # 颜色转换
        im = Image.open(os.path.join(path, file.name + '_no_bg.png'))
        # im = Image.open(os.path.join(path, file.name))
        x, y = im.size
        try:
            p = Image.new('RGBA', im.size, color=color_data)
            p.paste(im, (0, 0, x, y), im)
            p.save(os.path.join(path, file.name + '_bh.png'))

        except:
            pass
    except Exception:
        return ('出错了')

    return 'http://127.0.0.1:8000/download/' + file.name + '_bh.png'