# from flask import Flask, request, jsonify
# from flask_cors import CORS
#
# users = {
# 'test':{'passwd':'Test2024***','cookie':'ZXCVBNM,.;LKJHG','userId':'00000003'}
# }
#
# app = Flask(__name__)
# CORS(app) # 启用 CORS，允许所有域访问
#
#
# @app.route('/api/login', methods=['POST'])
# def login():
#     req_data = request.get_json()
#     type = req_data.get('type')
#     print('Data Get :')
#     print(req_data)
#     if(type=='cookie'):
#         cookie=req_data.get('cookie')
#         try:
#             for key, val in users.items():
#                 if(val['cookie']==cookie):
#                     print('Y')
#                     return jsonify({'state':'Y','user_id':val['userId']})
#             return jsonify({'state': 'N'})
#         except KeyError:
#             return jsonify({'state': 'E'})
#     elif(type=='username'):
#         name = req_data.get('username')
#         password = req_data.get('passwd')
#         try:
#             if users[name]['passwd'] == password:
#                 print('Y')
#                 return jsonify({'state': 'Y', 'cookie': users[name]['cookie'], 'userId': users[name]['userId']})
#             else:
#                 return jsonify({'state': 'N'})
#         except KeyError:
#             return jsonify({'state': 'E'})
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=1412, debug=True)