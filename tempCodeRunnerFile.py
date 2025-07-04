@socketio.on('createWorkspace')
def handle_createWorkspace(data):
    print(data)
    w = Workspace()
    w.admin_username = data['username']
    w.name = data['name']
    joining_code = random_string(4,2)
    w.joining_code = joining_code
    db.session.add(w)
    db.session.commit()
    room = Workspace.query.filter_by(name = data['name']).first()
    user = User.query.filter_by(name = data['username']).first()
    if user.workspace_list:
        user.workspace_list = user.workspace_list + str(room.id) + " "
    else:
        user.workspace_list = str(room.id) +" "
    db.session.commit()
    print("hello",user.workspace_list)
    join_room(room.name)
    data = {
        "name":data['name'],
        "admin_username": data['username'],
        "id": room.id, 
        "joining_code": joining_code,
    }
    emit('createWorkspaceJS',data, broadcast=True)
