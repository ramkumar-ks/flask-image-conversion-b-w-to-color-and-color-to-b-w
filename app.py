from flask import Flask,render_template,request
import cv2
import os
app=Flask(__name__)
app.config['Upload_folder']="static/images"
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/index', methods=['GET', 'POST'])
def data():
    if request.method=='POST':
        f=request.form['img_file']
        if request.form['Convert B&W']=='Convert B&W1':
            global img
            global gray_image
            img=cv2.imread(f)
            img=cv2.resize(img,(400,400))
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_image=cv2.imwrite('b&wimage.png',gray_image)
            return render_template('index.html',img=img,gray_image=gray_image)            
        if gray_image.filename!='':
            filepath=os.path.join(app.config['Upload_folder'],gray_image.filename)
            gray_image.save(filepath)
            path=filepath
            return render_template('index.html',data=path)
    return render_template('index.html')
@app.route('/color_image', methods=['GET', 'POST'])
def data1():
    if request.form['Convert Color']=='Convert Color1':
        f=request.form['img_file']
        global image
        global image_rgb
        image=cv2.imread(f)
        image=cv2.resize(image,(400,400))
        image_rgb = cv2.cvtColor(image,cv2.COLOR_LAB2BGR)
        image_rgb=cv2.imwrite('color.png',image_rgb) 
        return render_template('index.html',image=image,image_rgb=image_rgb)
        if image_rgb.filename!='':
            filepath=os.path.join(app.config['Upload_folder'],image_rgb.filename)
            image_rgb.save(filepath)
            path=filepath
            return render_template('index.html',data=path)
    return render_template('index.html',msg="Hello world")
if __name__ == '__main__':
    app.run(debug=True)
