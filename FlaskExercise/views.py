from flask import render_template, redirect, request
from FlaskExercise import app, db
from FlaskExercise.forms import PetForm
import FlaskExercise.models as models

imageSourceUrl = 'https://'+ app.config['BLOB_ACCOUNT']  + '.blob.core.windows.net/' + app.config['BLOB_CONTAINER']  + '/'


@app.route('/')
@app.route('/home')
def home():
    pets = models.Pet.query.all()
    return render_template(
        'index.html',
        imageSource=imageSourceUrl,
        pets=pets
    )


@app.route('/pet/<int:id>', methods=['GET', 'POST'])
def pet(id):
    pet = models.Pet.query.get(int(id))
    form = PetForm(formdata=request.form, obj=pet)
    if form.validate_on_submit():
        pet.save_changes(request.files['image_path'])
        return redirect('/')
    return render_template(
        'pet.html',
        imageSource=imageSourceUrl,
        form=form,
        pet=pet
    )
