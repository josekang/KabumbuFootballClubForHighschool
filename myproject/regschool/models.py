################################################################
#### CREATE THE NECCESSARY IMPORTS FOR THE REGSCHOOL MODEL #####
################################################################

from myproject import db

################################################
#### CREATE THE MODELS FOR THE REGSCHOOL #######
################################################

class RegisterSchool(db.Model):
    __tablename__ = "schools"

    id = db.Column(db.Integer, primary_key = True)
    schoolname = db.Column(db.Text(128))
    #teammembers = db.Column(db.Text(128))
    coachname = db.Column(db.Text(128))
    registrationfee = db.Column(db.Integer)
    regteam = db.relationship("RegTeam", backref = "regschool", uselist = False)


    def __init__(self, schoolname, coachname, registrationfee):
        self.schoolname = schoolname
        #self.teammembers = teammembers
        self.coachname = coachname
        self.registrationfee = registrationfee

    def __repr__(self):
        if self.regteam:
            return f"The team name is {self.schoolname} and our coach is {self.coachname} and we have paid a registration fee of {self.registrationfee}."
         # The team members include\ {self.teammembers}


class RegTeam(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key = True)
    member = db.Column(db.Text(128))
    sch_id = db.Column(db.Integer, db.ForeignKey("schools.id"))

    def __init__(self, member, sch_id):
        self.member = member
        self.sch_id = sch_id

    def __repr__(self):
        return f"Name: {self.member} || Team: {self.sch_id}"
