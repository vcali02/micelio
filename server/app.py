#!/usr/bin/env python3


# Remote library imports
import traceback
from flask import make_response, request, session
from flask_migrate import Migrate
from flask_restful import Resource
from models import User, CompletedPrompt, NudgePrompt, Nudge, JournalPrompt, Journal, Pillar, Recommendation
# Local imports
from config import app, db, api, bcrypt, CORS
# importing LoginManager class
# contains the code that lets your application and Flask-Login work together
# from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# #instance
# login_manager = LoginManager()
# #configure the instance for login
# login_manager.init_app(app)
# flask login
# Flask-Login uses sessions for authentication
#!!!!!MUST SET A SECRET KEY!!!!
app.secret_key = b'\x99\xbc@p\xfd\x83;\x1e\xda9\xd7\xb2\x82\x90\xdfy'


# ------------------SIGNUP--------------------#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.filter_by(id=user_id).first()


class Signup(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(
            name=data['name'],
            email=data['email'],
            username=data['username'],
            bio=data['bio'],
            image=data['image'],
        )
        new_user.password_hash = data.get('password')
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        # login_user(new_user, remember=True)
        return new_user.to_dict(), 201


api.add_resource(Signup, '/signup')

# ------------------SIGNUP--------------------#
# -------------------LOGIN--------------------#


class Login(Resource):
    def post(self):
        try:
            data = request.get_json()
            user = User.query.filter_by(username=data.get('username')).first()
            # import ipdb; ipdb.set_trace()
            if user.authenticate(data.get('password')):
                session['user_id'] = user.id
                return user.to_dict(), 200
        # except:
        #     raise Unauthorized("invalid credentials")
        except Exception as e:
            traceback.print_exc()
            return {"error": "hi", "message": str(e)}, 500


api.add_resource(Login, '/login')

# -------------------LOGIN--------------------#
# ------------------LOGOUT--------------------#


class Logout(Resource):
    def post(self):
        session["user_id"] = None
        return "You have logged out of micelio", 204


api.add_resource(Logout, '/logout')

# ------------------LOGOUT--------------------#
# ----------------AUTHORIZE-------------------#


class AuthorizeSession(Resource):
    def get(self):
        
        try:
            user_id = session.get("user_id")
            if user_id is None:
                return {"error": "User not logged in.", "message": "User ID not found in session."}, 401

            user = User.query.filter_by(id=user_id).first()
            if user is None:
                return {"error": "User not found.", "message": "User with the provided ID does not exist."}, 404

            return make_response(user.to_dict(), 200)

        except Exception as e:
            traceback.print_exc()
            return {"error": "Internal Server Error.", "message": str(e)}, 500


api.add_resource(AuthorizeSession, '/authorize_session')

# ----------------AUTHORIZE-------------------#
# --------------------USER--------------------#
# GET /user


class Users(Resource):
    def get(self):
        # 1. query
        users = User.query.all()
        if not users:
            return {"error": "User not found."}, 404
        # 2. dict
        users_dict = [u.to_dict() for u in users]
        # 3. res
        res = make_response(
            users_dict,
            200
        )
        return res


# 4.route
api.add_resource(Users, "/users")

# GET /user/<int:id>


class OneUser(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return {"error": "User not found."}, 404
        user_dict = user.to_dict()
        res = make_response(
            user_dict,
            200
        )
        return res

# PATCH /user/<int:id>
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        data = request.to_json()
        if not user:
            return {"error": "User not found."}, 404
        else:
            try:
                for attr in data:
                    setattr(user, attr, data.get(attr))
                db.session.add(user)
                db.session.commit()
                return make_response(
                    user.to_dict(),
                    202
                )
            except:
                return make_response({"400": "User update unsuccessful."}, 400)

# DELETE /user/<int:id>
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return {"error": "User not found."}, 404
        db.session.delete(user)
        db.session.commit()
        return make_response({}, 204)


api.add_resource(OneUser, "/users/<int:id>")

# --------------------USER--------------------#
# --------------COMPLETED PROMPTS-------------#

# GET /completed_prompts
class CompletedPrompts(Resource):
    def get(self):
        cps = CompletedPrompt.query.all()
        if not cps:
            return {"error": "Progress not found."}, 404
        cps_dict = [c.to_dict() for c in cps]
        res = make_response(
            cps_dict,
            200
        )
        return res



api.add_resource(CompletedPrompts, "/completed_prompts")

# GET /completed_prompts/<int:id>


class OneCompletedPrompt(Resource):
    def get(self, id):
        cp = CompletedPrompt.query.filter_by(id=id).first()
        if not cp:
            return {"error": "User not found."}, 404
        cp_dict = cp.to_dict()
        res = make_response(
            cp_dict,
            200
        )
        return res

# DELETE /completed_prompts/<int:id>
    def delete(self, id):
        cp = CompletedPrompt.query.filter_by(id=id).first()
        if not cp:
            return {"error": "Progress not found."}, 404
        db.session.delete(cp)
        db.session.commit()
        return make_response({}, 204)


api.add_resource(OneCompletedPrompt, "/completed_prompts/<int:id>")

# Completed prompts by USER ID


@app.route("/completed_by_user/<int:id>", methods=["GET"])
def completed_by_user(id):
    completed = (
        CompletedPrompt.query.join(
            User, CompletedPrompt.user_id == User.id)
        .filter(User.id == id)
        .all()
    )
    cp_dict = [cp.to_dict() for cp in completed]
    return make_response(cp_dict, 200)

# POST??????? maybe not
# front end even listener will trigger a GET request to display the data
class AddCompletedToUser(Resource):
    # def get

    def post(self, id):
        #this gives us whatever is sent to the backend
        #data is an object
        #how can we go through the data obj to get the adventurer username key
        #THIS IS WHAT I SEND IN THE FE POST
        data = CompletedPrompt.query.all()
        # try:
            #instance
        new_cp = CompletedPrompt(
            # journal_prompt= data.get("journal_prompt"),
            journal_prompt_id= data.get("journal_prompt_id"),
            # nudge_prompt = data.get("nudge_prompt"),
            nudge_prompt_id= data.get("nudge_prompt_id"),
            # user = data.get("user"),
            user_id = data.get("user_id")
        )
            #add/commit
        db.session.add(new_cp)
        db.session.commit()
            #dict
        new_cp_dict = new_cp.to_dict()
            #res
        res = make_response(
            new_cp_dict,
            201
        )
        return res
        # except:
        #     return {"400" : "Prompt completion unsuccessful."}, 400
api.add_resource(AddCompletedToUser, "/add_completed_to_user/<int:id>")



# --------------COMPLETED PROMPTS-------------#
# ----------------NUDGE PROMPTS---------------#
# GET /nudge_prompt
class NudgePrompts(Resource):
    def get(self):
        nps = NudgePrompt.query.all()
        if not nps:
            return {"error": "Nudge prompt not found."}, 404
        nps_dict = [n.to_dict() for n in nps]
        res = make_response(
            nps_dict,
            200
        )
        return res


api.add_resource(NudgePrompts, "/nudge_prompts")

# GET /nudge_prompt/<int:id>


class OneNudgePrompt(Resource):
    def get(self, id):
        np = NudgePrompt.query.filter_by(id=id).first()
        if not np:
            return {"error": "Nudge prompt not found."}, 404
        np_dict = np.to_dict()
        res = make_response(
            np_dict,
            200
        )
        return res


api.add_resource(OneNudgePrompt, "/nudge_prompts/<int:id>")

# ----------------NUDGE PROMPTS---------------#
# ---------------JOURNAL PROMPTS--------------#
# GET /journal_prompt


class JournalPrompts(Resource):
    def get(self):
        jps = JournalPrompt.query.all()
        if not jps:
            return {"error": "Journal prompt not found."}, 404
        jps_dict = [j.to_dict() for j in jps]
        res = make_response(
            jps_dict,
            200
        )
        return res


api.add_resource(JournalPrompts, "/journal_prompts")

# GET /journal_prompt/<int:id>


class OneJournalPrompt(Resource):
    def get(self, id):
        jp = JournalPrompt.query.filter_by(id=id).first()
        if not jp:
            return {"error": "Nudge prompt not found."}, 404
        jp_dict = jp.to_dict()
        res = make_response(
            jp_dict,
            200
        )
        return res


api.add_resource(OneJournalPrompt, "/journal_prompts/<int:id>")

# ---------------JOURNAL PROMPTS--------------#
# --------------------NUDGE-------------------#
# GET /nudges


class Nudges(Resource):
    def get(self):
        ns = Nudge.query.all()
        if not ns:
            return {"error": "Journal prompt not found."}, 404
        ns_dict = [n.to_dict(only=("image", "action_type",
                             "description", "pillar_id")) for n in ns]
        res = make_response(
            ns_dict,
            200
        )
        return res


api.add_resource(Nudges, "/nudges")

# GET /nudges/<int:id>


class OneNudge(Resource):
    def get(self, id):
        n = Nudge.query.filter_by(id=id).first()
        if not n:
            return {"error": "Nudge prompt not found."}, 404
        n_dict = n.to_dict(only=("image", "action_type",
                           "description", "pillar_id", "id"))
        res = make_response(
            n_dict,
            200
        )
        return res


api.add_resource(OneNudge, "/nudges/<int:id>")


# --------------------NUDGE-------------------#
# -------------------JOURNAL------------------#
# GET /journals
class Journals(Resource):
    def get(self):
        js = Journal.query.all()
        if not js:
            return {"error": "Journal prompt not found."}, 404
        js_dict = [j.to_dict(only=("image", "action_type",
                             "description", "pillar_id")) for j in js]
        res = make_response(
            js_dict,
            200
        )
        return res


api.add_resource(Journals, "/journals")

# GET /journals/<int:id>


class OneJournal(Resource):
    def get(self, id):
        j = Journal.query.filter_by(id=id).first()
        if not j:
            return {"error": "Nudge prompt not found."}, 404
        j_dict = j.to_dict(only=("image", "action_type",
                           "description", "pillar_id"))
        res = make_response(
            j_dict,
            200
        )
        return res


api.add_resource(OneJournal, "/journals/<int:id>")


# -------------------JOURNAL------------------#
# -------------------PILLAR-------------------#
# GET /pillars
class Pillars(Resource):
    def get(self):
        ps = Pillar.query.all()
        if not ps:
            return {"error": "Journal prompt not found."}, 404
        ps_dict = [p.to_dict() for p in ps]
        res = make_response(
            ps_dict,
            200
        )
        return res


api.add_resource(Pillars, "/pillars")

# GET /pillars/<int:id>


class OnePillar(Resource):
    def get(self, id):
        p = Pillar.query.filter_by(id=id).first()
        if not p:
            return {"error": "Nudge prompt not found."}, 404
        p_dict = p.to_dict()
        res = make_response(
            p_dict,
            200
        )
        return res


api.add_resource(OnePillar, "/pillars/<int:id>")


# -------------------PILLAR-------------------#
# --------------PILLAR PROMPTS----------------#

# Nudges by PILLAR ID
@app.route("/nudge_by_pillar/<int:id>", methods=["GET"])
def nudge_by_pillar(id):
    nudges = (
        Nudge.query.join(
            Pillar, Nudge.pillar_id == Pillar.id)
        .filter(Pillar.id == id)
        .all()
    )
    ns_dict = [ns.to_dict(
        only=("action_type", "description", "id", "image",)) for ns in nudges]
    return make_response(ns_dict, 200)

# Journals by PILLAR ID


@app.route("/journal_by_pillar/<int:id>", methods=["GET"])
def journal_by_pillar(id):
    journals = (
        Journal.query.join(
            Pillar, Journal.pillar_id == Pillar.id)
        .filter(Pillar.id == id)
        .all()
    )
    js_dict = [js.to_dict(
        only=("action_type", "description", "id", "image",)) for js in journals]
    return make_response(js_dict, 200)

# Nudge prompts by PILLAR ID


@app.route("/nprompts/<int:id>", methods=["GET"])
def nprompts(id):
    nudge_prompts = (
        NudgePrompt.query.join(
            Nudge, NudgePrompt.nudges_id == Nudge.id
        )
        .join(Pillar, Nudge.pillar_id == Pillar.id)
        .filter(Pillar.id == id)
        .all()
    )
    np_dict = [n.to_dict(only=("action_prompt",)) for n in nudge_prompts]
    return make_response(np_dict, 200)

# Journal prompts by PILLAR ID


@app.route("/jprompts/<int:id>", methods=["GET"])
def jprompts(id):
    journal_prompts = (
        JournalPrompt.query.join(
            Journal, JournalPrompt.journals_id == Journal.id
        )
        .join(Pillar, Journal.pillar_id == Pillar.id)
        .filter(Pillar.id == id)
        .all()
    )
    jp_dict = [j.to_dict(only=("action_prompt",)) for j in journal_prompts]
    return make_response(jp_dict, 200)


# --------------PILLAR PROMPTS----------------#
# -----------------RECOMMENDED----------------#
# GET /recommendations
class Recommendations(Resource):
    def get(self):
        rs = Recommendation.query.all()
        if not rs:
            return {"error": "Journal prompt not found."}, 404
        rs_dict = [r.to_dict() for r in rs]
        res = make_response(
            rs_dict,
            200
        )
        return res


api.add_resource(Recommendations, "/recommendations")

# GET /recommended/<int:id>


class OneRecommendation(Resource):
    def get(self, id):
        r = Recommendation.query.filter_by(id=id).first()
        if not r:
            return {"error": "Nudge prompt not found."}, 404
        r_dict = r.to_dict()
        res = make_response(
            r_dict,
            200
        )
        return res


api.add_resource(OneRecommendation, "/recommendations/<int:id>")


# -----------------RECOMMENDED----------------#

if __name__ == '__main__':
    app.run(port=5555, debug=True)
