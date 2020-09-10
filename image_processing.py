from PIL import Image,ImageFilter

new_image=Image.open("A:\Front_end\HTML_basics\Front_end_basics\img4.jpg")
black=new_image.convert('L')
test=black.rotate(90)
test.save('black.jpg')
test.show()

