from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user # current_user
from .models import Comment, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    #homePage = Page(id=1, name=home)
    #db.session.add(homePage) #adicionar home a Page()
    #db.session.commit()
# ...Tentativa de simular outra base de dados para os comentários funcionarem
    comments = Comment.query.all()
    users = User.query.all()

    if request.method == 'POST':
        comment = request.form.get('comment')

        if len(comment) < 1:
            flash('Commentário é muito curto!', category='error')
        else:
            new_comment = Comment(data=comment, user_id=current_user.id, user_name=current_user.first_name) #, user_id=current_user.id , page_id=1
            db.session.add(new_comment)
            db.session.commit()
            flash('Comentário adicionado!', category='success')

    return render_template("home.html", user = current_user, comments=comments, users=users) #, user=current_user

#@views.route('/', methods=['GET'])
#@login_required
#def see_comments():


@views.route('/delete-comment', methods=['POST'])
def delete_comment():
    comment = json.loads(request.data)
    commentId = comment['commentId']
    comment = Comment.query.get(commentId)
    if comment:
        if comment.user_id == current_user.id: # current_user.id
            db.session.delete(comment)
            db.session.commit()
            flash('Comentário eliminado.', category='error')
        else:
            flash('Não pode eliminar comentários de outros utilizadores.', category='error')
    return jsonify({})


@views.route('/capital', methods=['GET', 'POST'])
def capital():
    #capitalPage = Page(id=2, name=capital)
    #db.session.add(capitalPage)  # adicionar capital a Page()
    #db.session.commit()
# ...Tentativa de simular outra base de dados para os comentários funcionarem
    return render_template('capital.html', user=current_user) #, user=current_user


@views.route('/history', methods=['GET', 'POST'])
def history():
    #historyPage = Page(id=3, name=history)
    #db.session.add(historyPage)  # adicionar history a Page()
    #db.session.commit()
# ...Tentativa de simular outra base de dados para os comentários funcionarem
    return render_template('history.html', user=current_user) #, user=current_user


@views.route('/attractions', methods=['GET', 'POST'])
def attractions():
    #attractionsPage = Page(id=4, name=attractions)
    #db.session.add(attractionsPage)  # adicionar attractions a Page()
    #db.session.commit()
# ...Tentativa de simular outra base de dados para os comentários funcionarem
    return render_template('attractions.html', user=current_user) #, user=current_user
