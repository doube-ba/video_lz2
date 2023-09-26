from flask import Flask,request,render_template,jsonify
import lz
app = Flask(__name__)
@app.route('/')
def index1():
    return render_template('centent.html')
@app.route('/datas')
def index2():
    x = request.args.get('data_x')
    y = request.args.get('data_y')
    z = request.args.get('data_z')
    print(x,y,z)
    data = lz.data_lists(x,y,z)
    return data
@app.route('/playvideo')
def index3():
    return render_template('centent1.html')
@app.route('/video_playlist')
def index4():
    play_url = request.args.get('play_url')
    data = lz.data_url(play_url)
    return data
if __name__ == '__main__':
    app.run()