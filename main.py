from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route('/family')
def family():
    return render_template("family.html")


@app.route('/lions')
def lions():
    return render_template("lions_demo.html")


@app.route('/AA')
def aa():
    return render_template("AAKenya.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/author')
def author():
    return render_template("author.html")


@app.route('/book')
def book():
    return render_template("book.html")


@app.route('/contact')
def contact(): 
    return render_template("contact.html")


@app.route('/currents')
def currents():    
    return render_template("currents.html")


@app.route('/gallery')
def gallery(): 
    return render_template("gallery.html")


@app.route('/kilimanjaro')
def kilimanjaro():    
    return render_template("kilimanjaroTrust.html")


@app.route('/kingsway')
def kingsway():
    return render_template("kingsway.html")


@app.route('/mpShah')
def mpShah():
    return render_template("mpShah.html")


@app.route('/others')
def others():
    return render_template("others.html")




@app.route('/specialOlympics')
def special(): 
    return render_template("specialOlympics.html")


@app.route('/stJones')
def stjones():  
    return render_template("stJones.html")


@app.route('/videos')
def videos():  
    return render_template("videos.html")


@app.route('/membership')
def membership():
    return render_template("membership.html")


@app.route('/leadership')
def leadership():
    return render_template("leadership.html")


@app.route('/areaforums')
def areaforum():
    return render_template("areaforums.html")


@app.route('/leadershiprole')
def leadershiprole():
    return render_template("leadership_role.html")


@app.route('/partnership')
def partnership():
    return render_template("partnership.html")


@app.route('/achievements')
def achievement():
    return render_template("achievements.html")


@app.route('/lionservice')
def service():
    return render_template("service.html")


@app.route('/vision')
def vision():
    return render_template("vision.html")


@app.route('/youth')
def youth():
    return render_template("youth.html")


@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")


@app.route('/environment')
def environment():
    return render_template("environment.html")


@app.route('/hunger')
def hunger():
    return render_template("hunger.html")
@app.route('/brochures')
def brochures():
    return render_template("brochures.html")
@app.route('/philanthropy')
def phila():
    return render_template("philanthropy.html")
@app.route('/lcif')
def lcif():
    return render_template("lcif.html")
@app.route('/ntsa')
def ntsa():
    return render_template("ntsa.html")
@app.route('/lsfeh')
def lsfeh():
    return render_template("lsfeh.html")

if __name__ == "__main__":
    app.run()