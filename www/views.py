from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def test(request):
    return render(request, 'template.html', {})


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

if __name__ == '__main__':
    app.run(debug=True)