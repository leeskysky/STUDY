# import mysql.connector

# # MySQL 접속 정보 설정
# config = {
#   'user': 'root',
#   'password': 'Leehaneul12#',
#   'host': 'localhost',
#   'database': 'sky',
#   'raise_on_warnings': True
# }

# # MySQL 접속
# conn = mysql.connector.connect(**config)
# cursor = conn.cursor()


# # 데이터 조회 예제
# select_query = "SELECT * FROM customers"
# cursor.execute(select_query)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # MySQL 접속 종료
# cursor.close()
# conn.close()


# import os

# # 현재 작업 디렉토리(current working directory) 얻기
# current_dir = os.getcwd()
# print("현재 작업 디렉토리:", current_dir)

