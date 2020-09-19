# -*- encoding: utf-8 -*-

import argparse
from pathlib import Path
from PIL import Image, GifImagePlugin

parser = argparse.ArgumentParser()
parser.add_argument('giffile', metavar='file', type=str, nargs='+', help='GIF files to get processed')

def main():
    args = parser.parse_args()
    for gif in args.giffile:
        # Determine file path
        gifpath = Path(gif)
        if not gifpath.exists():
            print('File {} does not exist'.format(gif))
            continue
        gifpath = gifpath.resolve()

        # Generate output folder
        outputpath = gifpath.parent / gifpath.stem
        if outputpath.exists() and not outputpath.is_dir():
            print('Cannot create output folder {}'.format(outputpath))
            continue
        outputpath.mkdir(exist_ok=True)

        # Process file
        gifim = Image.open(str(gifpath))
        if not gifim.is_animated:
            print('GIF file {} is not animated'.format(gifpath))
            continue
        frame = 0
        gifim.seek(0)
        last_duration = None
        timelinefile = outputpath / (gifpath.stem + '.txt')
        timeline = open(str(timelinefile), 'w+')
        while True:
            try:
                duration = gifim.info['duration']
                if duration == last_duration:
                    timeline.write('::{}\n'.format(frame))
                else:
                    timeline.write(':{}:{}\n'.format(1000 / duration, frame))
                last_duration = duration

                outputfile = outputpath / (gifpath.stem + '-{}.png'.format(frame))
                gifim.save(str(outputfile), optimize=True)

                gifim.seek(gifim.tell() + 1)
                frame += 1
            except EOFError:
                break

        timeline.close()
        print('{}: Ok'.format(gifpath))


if __name__ == '__main__':
    main()
