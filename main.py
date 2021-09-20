import cv2 
import qrcode 
from flask import Flask ,render_template,request ,flash
import os
from werkzeug.utils import secure_filename

def decode(image):
	try :
		img = cv2.imread(image)
		decoder = cv2.QRCodeDetector()
		text,_,_ = decoder.detectAndDecode(img)
		return text
	except:
		return 'IMAGE IS NOT VALID OR SOMETHING ELSE'
	    
	    



IMAGE_FOLDER = os.path.join('static')
FILES_FOLDER = os.path.join('files')
app = Flask(__name__,template_folder='templates')
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER 
app.config['FILES'] = FILES_FOLDER



img = None

@app.route('/',methods=['GET','POST'])
def main():
	if request.method == 'POST':
		if 'textsubmit' in request.form:
			val = request.form['cont']
			if val is not None:
				img = qrcode.make(val)
				img.save('static/twenty.jpeg')
			return render_template('main.html',path='static/ten.jpeg')

		if 'imagesubmit' in request.form:
			file = request.files['imagefile']
			file_saved_path = os.path.join(app.config['FILES'],file.filename)
			file.save(file_saved_path)
			decoded = decode(file_saved_path)
			print('file saved ')
			return render_template('main.html',text=decoded)
			

			


	return render_template('main.html')



 
