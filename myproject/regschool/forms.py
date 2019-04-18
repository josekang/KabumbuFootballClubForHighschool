#################################################################
#### CREATE THE NECCESSARY IMPORTS FOR THE REGSCHOOL FORMS ######
#################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError

###############################################
#### CREATE THE FORMS FOR THE REGSCHOOL #######
###############################################

class RegSchoolForm(FlaskForm):
    schoolname = StringField("Enter the name of the school: ", validators = [DataRequired("Please ensure to enter the correct information")])
    coachname = StringField("Enter the name of the head Coach: ", validators = [DataRequired("Please ensure to enter the correct information")])
    registrationfee = FloatField("Enter the registration amount: ", validators = [DataRequired("Please ensure to enter the correct information")])
    submit = SubmitField("REGISTER")

    def check_school(self, field):
        if RegisterSchool.query.filter_by(schoolname = field.data).first():
            raise ValidationError("The school has already been registered")

class RegMemberForm(FlaskForm):
    member = StringField("Enter the name of the player: ")
    sch_id = IntegerField("ID of the school: ")
    submit = SubmitField("ENTER")
