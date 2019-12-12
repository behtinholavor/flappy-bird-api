from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_cors import CORS

db_connect = create_engine('sqlite:///flappybird.db')
app = Flask(__name__)
api = Api(app)


class Players(Resource):
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from players order by big_score desc")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return result

    def post(self):
        conn = db_connect.connect()
        name = request.json['name']
        email = request.json['email']
        big_score = request.json['big_score']
        small_score = request.json['small_score']

        sql = "insert into players (name, big_score, small_score, email) values('{0}','{1}', '{2}', '{3}')"
        sql = sql.format(name, big_score, small_score, email)
        conn.execute(sql)
        query = conn.execute('select * from players order by id desc limit 1')
        if query.cursor.lastrowid > 0:
            res = 'player registred successfully!'
        else:
            res = 'player NOT registred successfully!'

        return {"payload": res}
        # result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        # return result

    def put(self):
        conn = db_connect.connect()
        print(request)
        id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        big_score = request.json['big_score']
        small_score = request.json['small_score']

        sql = "update players set"
        sql = sql + " name        = '{0}', "
        sql = sql + " big_score   =  {1},  "
        sql = sql + " small_score =  {2},  "
        sql = sql + " email       = '{3}'  "
        sql = sql + "where"
        sql = sql + "  id        ='{4}' "
        sql = sql.format(name, big_score, small_score, email, id)
        conn.execute(sql)
        query = conn.execute("select * from players where id ='{0}' ".format(id))
        if query.cursor.lastrowid > 0:
            res = 'player updated successfully!'
        else:
            res = 'player NOT updated successfully!'
        return {"payload": res}


class PlayerById(Resource):
    def delete(self, id):
        conn = db_connect.connect()
        conn.execute("delete from players where id='{0}' ".format(id))
        query = conn.execute("select * from players where id ='{0}' ".format(id))
        if query.cursor.lastrowid <= 0:
            res = 'player deleted successfully!'
        else:
            res = 'player NOT deleted successfully!'
        return {"payload": res}

    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from players where id ='{0}' ".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return result


class PlayerByEmail(Resource):
    def get(self, email):
        conn = db_connect.connect()
        query = conn.execute("select * from players where email ='{0}' ".format(email))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return result


api.add_resource(Players, '/players')
api.add_resource(PlayerById, '/players/id/<id>')
api.add_resource(PlayerByEmail, '/players/email/<email>')

if __name__ == '__main__':
    app.run(debug=True)
