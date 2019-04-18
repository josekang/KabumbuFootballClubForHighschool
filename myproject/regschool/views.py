##################################################################
##### CREATE THE NECCESSARY IMPORTS FOR THE REGSCHOOL VIEWS ######
##################################################################

from flask import Blueprint, render_template, request, flash, redirect, url_for
from myproject import db
from myproject.regschool.forms import RegSchoolForm, RegMemberForm
from myproject.regschool.models import RegisterSchool, RegTeam

###################################################
### CREATE THE VIEWS FOR THE REGSCHOOL ############
###################################################

regschool_blueprints = Blueprint("regschool", __name__, template_folder = "templates/regschool")

@regschool_blueprints.route("/regschool", methods = ["GET", "POST"])
def regschool():
    form = RegSchoolForm()
    if form.validate_on_submit():
        schoolname = form.schoolname.data
        coachname = form.coachname.data
        registrationfee = form.registrationfee.data

        new_school = RegisterSchool(schoolname, coachname, registrationfee)
        db.session.add(new_school)
        db.session.commit()

        return redirect (url_for("thankyou"))

    return render_template("regschool.html", form = form)

@regschool_blueprints.route("/regmembers", methods = ["GET", "POST"])
def regmembers():
    form = RegMemberForm()
    if form.validate_on_submit():
        member = form.member.data
        sch_id = form.sch_id.data
        new_member = RegTeam(member, sch_id)
        db.session.add(new_member)
        db.session.commit()

        return redirect(url_for("thankyou"))

    return render_template("regschool.html", form = form)
