@app.route('/internal-dashboard/users', methods=['GET'])
def showUsers():
    users = db.getAllUsers()
    return render_template("dashboard/users.html", users=users)
 
