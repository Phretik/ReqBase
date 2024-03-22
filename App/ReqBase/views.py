from flask import Blueprint, jsonify, render_template, request, jsonify,  redirect, url_for
from flask_login import login_required, current_user
from .models import Req, Log
from . import db
from flask import flash
import json
from auth import logout

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def requests():
    if request.method == 'POST':
        app_name = request.form.get('appName')
        app_vendor = request.form.get('appVendor')   ##Captures form data
        req_name = request.form.get('reqName')
        arch_num = request.form.get('archNum')
        note = request.form.get('note')

        
        if len(app_name) < 1 or not app_name  :
            flash('App name required', category='error')
        elif len(app_vendor) < 1 or not app_vendor :
            flash('vendor name required.', category='error')    ##Validates the data and flashes message if invalid
        elif len(req_name) < 1 or not req_name:
            flash('Requestor name is required', category='error')
        else:
            new_req = Req(app_name=app_name, app_vendor=app_vendor, req_name=req_name, arch=arch_num, note=note, user_id=current_user.id)
            db.session.add(new_req)  ##Creates a new Req object and commits to database
            db.session.commit()
            flash('Request created.', category='success')
            return redirect(url_for('views.requests'))
    return render_template("requests.html", user=current_user, reqList = Req.query.all())

@views.route('/updateReq/<int:id>', methods=['GET', 'POST'] )
@login_required
def updateReq(id):
    if current_user.admin == False:
        logout()
    
    req_to_update = Req.query.get_or_404(id)     ##Querys the database using the passed Id
    if request.method == 'POST':
        req_to_update.app_name = request.form['appName']
        req_to_update.app_vendor = request.form['appVendor']   ##Changes the attributes of the object
        req_to_update.req_name = request.form['reqName']
        req_to_update.arch = request.form['archNum']
        req_to_update.note = request.form['note']
        db.session.commit()               ##Commits the changes
        return redirect(url_for('views.requests'))
    else:
        return render_template('update_req.html', req_to_update=req_to_update, user=current_user)


@views.route('/delete-req', methods=['POST'])
def delete_req():
    req = json.loads(request.data)
    reqId = req['reqId']
    req = Req.query.get(reqId)          ##Querys the database for the request
    if req:
        if req.user_id == current_user.id:
            db.session.delete(req)                 ##deletes the request
            db.session.commit()
            flash('Request deleted', category='success') 
        else: 
            flash('Not the current user', category='error') 
    else:
        flash('Cannot get the request', category='error') 
    return jsonify({})

@views.route('/delete-log', methods=['POST'])
def delete_log():
    post = json.loads(request.data)   ##queries the database for the log
    postId = post['postId']
    post = Log.query.get(postId)           ##deletes the log
    if post:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted', category='success') 
    else:
        flash('Cannot get the request', category='error') 
    return jsonify({})

@views.route('/updateLog/<int:id>', methods=['GET', 'POST'] )
@login_required
def updateLog(id):
    post_to_update = Log.query.get_or_404(id)        ##Queries the database and updates the log 
    if request.method == 'POST':
        post_to_update.post = request.form['post']
        db.session.commit()
        return redirect(url_for('views.postLog'))
    else:
        return render_template('update_log.html', post_to_update=post_to_update, user=current_user)
    

@views.route('/teamLog', methods=['GET', 'POST'])
@login_required
def postLog():
    if request.method == 'POST':
        post = request.form.get('log')
        
        if len(post) < 1 :
            flash('Empty posts are not accepted', category='error')   ##Validates the post before it is submitted
        else:
            new_log = Log(post=post, user_email=current_user.email)
            db.session.add(new_log)
            db.session.commit()
            flash('Log Posted.', category='success')
            return redirect(url_for('views.postLog'))
    return render_template("team_log.html", user=current_user, posts = Log.query.all())