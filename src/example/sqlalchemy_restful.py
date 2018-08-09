#coding:utf-8

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from flask import Flask, g
from flask_restful import reqparse, Api, Resource
from flask_httpauth import HTTPTokenAuth

# Flask 声明相关
app = Flask(__name__)
api = Api(app)

# token
auth = HTTPTokenAuth(scheme="token")
TOKENS = {
  "fejiasdfhu",
  "fejiuufjeh"
}

@auth.verify_token
def verify_token(token):
  if token in TOKENS:
    g.current_user = token
    return True
  return False
# 数据库相关变量声明
DB_ADRESS = "mysql+pymysql://root:wangji@127.0.0.1:3306/test"
engine = sqlalchemy.create_engine(DB_ADRESS, encoding="utf8", echo=False)
BaseModel = sqlalchemy.ext.declarative.declarative_base()

# 构建数据模型
class User(BaseModel):
  __tablename__ = 'Users'
  __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8"
  }

  # 表结构
  id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True)
  name = sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False)
  age = sqlalchemy.Column('age', sqlalchemy.Integer, nullable=False)

# 利用 Session 对象连接数据库
DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
session = DBSession()
BaseModel.metadata.drop_all(engine)
BaseModel.metadata.create_all(engine)

# RESTful API 的参数解析 -- put / post 参数解析
parser_put = reqparse.RequestParser()
parser_put.add_argument('name', type=str, required=True, help="need name data")
parser_put.add_argument('age', type=int, required=True, help="need age data")

# RESTful API 的参数解析 -- get
parser_get = reqparse.RequestParser()
parser_get.add_argument("limit", type=int, required=False)
parser_get.add_argument("offset", type=int, required=False)
parser_get.add_argument("sortby", type=StopAsyncIteration, required=False)

def get_json(user):
  return { "name": user.name, "age": user.age }

# 操作（put / get / delete）单一资源
class Todo(Resource):
  # 认证
  decorators = [auth.login_required]
  
  def put(self, user_id):
    """
    更新用户数据: curl http://127.0.0.1:5000/users/1 -X PUT -d "name=Allen&age=20" -H "Authorization: token fejiasdfhu"
    """
    args = parser_put.parse_args()
    # 这里为什么要用 session.query(User.id) 而不是 session.query(User)
    user_id_set = set([user.id for user in session.query(User).all()])
    if user_id not in user_id_set:
      return None, 404
    
    user = session.query(User).filter(User.id == user_id)[0]
    user.name = args['name']
    user.age = args['age']
    session.merge(user)
    session.commit()

    return get_json(user), 201

  def get(self, user_id):
    """
    获取用户数据: curl http://127.0.0.1:5000/users/1 -X GET -H "Authorization: token fejiasdfhu"
    """
    users = session.query(User).filter(User.id == user_id)
    if users.count() == 0:
      return None, 404
    return get_json(users[0]), 200
  
  def delete(self, user_id):
    pass
    

# 操作（post / get）资源列表
class TodoList(Resource):
  # 认证
  decorators = [auth.login_required]

  def get(self):
    """
    获取全部用户数据: curl http://127.0.0.1:5000/users -X GET -d "limit=2&offset=0&sortby=name" -H "Authorization: token fejiasdfhu"
    """
    users = session.query(User)
    args = parser_get.parse_args()

    # 按条件返回
    if 'sortby' in args:
      users = users.order_by(User.name.desc() if args['sortby'] == 'name' else User.age.desc())
    if 'limit' in args:
      users = users.limit(args['limit'])
    if 'offset' in args:
      users = users.offset(args['offset'])
    return [get_json(user) for user in users], 200

  def post(self):
    """
    添加一个新用户: curl http://127.0.0.1:5000/users -X POST -d "name=Brown&age=20" -H "Authorization: token fejiasdfhu"
    """
    args = parser_put.parse_args()

    user = User(name=args["name"], age=args["age"])
    session.add(user)
    session.commit()

    return get_json(user), 201

# 设置路由
api.add_resource(Todo, '/users/<int:user_id>')
api.add_resource(TodoList, '/users')

if __name__ == '__main__':
  app.run(debug=True)