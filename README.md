# working - 2 forms on a route

## roadblocks:
 - must be a` <form> </form>` on the rendered html

 - form must include this line : 

`<input type="hidden" name="form-name" value="my_form_name_here">`

 - form validalas route-on 

 ``` python 
 
Exchange_Form = ExchangeForm()
Login_Form = LoginForm()

    if request.method == 'POST':
        form_name = request.form['form-name']
	
        if form_name == 'Login_Form':
            if Login_Form.validate_on_submit():
                #dothis
        if form_name == 'Exchange_Form':
            if Exchange_Form.validate_on_submit():
	    	#dothis



