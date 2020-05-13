# working 2 form on a route

## roadblocks:
 - must be a` <form> </form>` on the rendered html

 - form must include this line : 

`<input type="hidden" name="form-name" value="my_form_name_here">`

 - form validalas route-on 

 ``` python 
if form_name == 'my_form_name_here':

	    if form_name_here.validate_on_submit():
```

 


