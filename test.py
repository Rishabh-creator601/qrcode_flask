from flask import Flask ,render_template
import qrcode 
import os


print('part 1')


IMAGE_FOLDER = os.path.join('static')

app = Flask(__name__,template_folder='templates')
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

content = qrcode.make('hello world ')
content.save('static/make.jpg')



@app.route('/')
@app.route('/uploads')
def main():
	tag = "<a href='/qrimg'> img </a> "
	return tag

@app.route('/qrimg')
def render_img():
	filename = os.path.join(app.config['IMAGE_FOLDER'],'make.jpg')
	return render_template('index.html',user_img=filename)





if __name__ == '__main__':
	app.run(debug=True)
