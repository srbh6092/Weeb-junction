from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/animes')
def animelist():
    return render_template('list.html')




@app.route('/about_us')
def about_us():
    return render_template('about.html')


@app.route('/community')
def goals():
    return render_template('community.html')



@app.route('/contact')
def contact_us():
    return render_template('contact.html')






if __name__=="__main__":
    app.run(debug=True)