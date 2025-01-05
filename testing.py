import app
import numpy as np

def test1():
    img_paths = app.getImgs('cards/test1')
    resized = [app.resizeImg(img_paths[0])]
    print(resized)

def test2():
    img_paths = app.getImgs()
    resized = [app.resizeImg(path) for path in img_paths]
    print(resized)

def test3():
    img_paths = app.getImgs()
    resized = [app.resizeImg(path) for path in img_paths]
    edged = resized[1]
    perim = app.getPerimeter(edged)
    print(np.linalg.norm(perim, axis=1) <= np.linalg.norm(np.array([255,255,255])*0.1))

def test4():
    app.main()
# test1()
# print("test1 complete.")
# test2()
# print("test2 complete.")
# test3()
# print("test3 complete")
test4()