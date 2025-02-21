from pathlib import Path
import cv2


def video_create(path="img"):
    path = Path(path)
    img = path.glob('*.jpg')
    img_sorted = sorted(img, key=lambda x: int(x.stem.split('_')[-1]))
    img_sorted = [cv2.imread(str(f)) for f in img_sorted]

    height, width, layers = img_sorted[0].shape
    output_name = path.parent / f'{path.name}.avi'
    output_name = r'' + str(output_name)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 1
    video = cv2.VideoWriter(output_name, fourcc, fps, (width, height))

    for img in img_sorted:
        image = cv2.resize(img, (width, height))
        video.write(image)

    video.release()
