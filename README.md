# working 2 form on a route

## roadblocks:
 - must be a` <form> </form>` on the rendered html

 - form must include this line : 

`<input type="hidden" name="form-name" value="my_form_name_here">`

 - form validalas route-on 

 ``` python 
Form_1 = Form1()
Form_2 = Form2()
if request.method == 'POST':
	if Form_1.validate_on_submit():
		#dothis
	if Form_2.validate_on_submit():
		#dothis
```

 


