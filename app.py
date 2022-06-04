from flask import Flask, render_template, request, flash
from converter import input_is_valid, convert

app = Flask(__name__)
app.config["SECRET_KEY"] = '123456'


@app.route('/')
def show_empty_form ():
    """ Display the input form for the user to fill out """
    return render_template ('input_form.html', title="Currency converter")

@app.route('/convert')
def process_form():
    """ Check the user's input for validity, informing them if any of the input is invalid. 
        If valid, execute the currency conversion.
    """
    result=''
    if input_is_valid():
        try:
            result = convert()
        except:
            flash("The conversion has failed")
        else:
            return render_template('/conversion_result.html', result=result, title='Result') 
    return render_template('input_form.html')
    

    
        




