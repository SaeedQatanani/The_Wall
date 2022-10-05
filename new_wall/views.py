from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Message, Comment
from login_app.models import User

def show_wall(request):
    try:
        # if Message.objects.all():
        context ={
            'messages' : Message.objects.all().order_by('-created_at'),
            'comments' : Comment.objects.all().order_by('-created_at')
            }
        request.session['first_name']
        return render(request, 'wall.html', context)
    except:
        return redirect('/')

def log_out(request):
    if request.session['first_name']:
        del request.session['first_name']
        del request.session['email']
    return redirect('/')

def create_message(request):
    user = User.objects.filter(email = request.session['email'])
    if user:
        logged_user = user[0]
        Message.objects.create(user = logged_user, message = request.POST['message'])
        return redirect('/wall/add_message')
    return redirect('/wall')

def add_message(request):
    return redirect('/wall')

def create_comment(request):
    user = User.objects.filter(email = request.session['email'])
    message = Message.objects.filter(id = request.POST['message_id'])
    if user and message:
        logged_user = user[0]
        this_message = message[0]
        Comment.objects.create(user = logged_user, message = this_message, comment = request.POST['comment'])
        return redirect('/wall/add_comment')
    return redirect('/wall')

def add_comment(request):
    return redirect('/wall')

def delete_comment(request):
    user = User.objects.filter(email = request.session['email'])
    logged_user = user[0]
    comment = Comment.objects.get(id = request.POST['comment_to_delete'])
    if comment.user.id == logged_user.id:
        comment.delete()
    return redirect('/wall')

def delete_message(request):
    user = User.objects.filter(email = request.session['email'])
    logged_user = user[0]
    message = Message.objects.get(id = request.POST['message_to_delete'])
    if message.user_id == logged_user.id:
        message.delete()
    return redirect('/wall')

