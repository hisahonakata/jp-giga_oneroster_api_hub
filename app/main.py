from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKey
from pydantic import BaseModel
from dotenv import load_dotenv
import sqlite3
import csv
from io import TextIOWrapper
import os

load_dotenv()

app = FastAPI()

# .envファイルからAPIキーとデータベース接続情報を取得
API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    raise ValueError("API_KEYが設定されていません。")

DATABASE_FILE = os.getenv("DATABASE_FILE")
if DATABASE_FILE is None:
    raise ValueError("DATABASE_FILEが設定されていません。")

# APIキーのパラメータ名とヘッダ名
API_KEY_NAME = "api_key"
api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)

# SQLiteデータベースを作成する関数
def create_database():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS AcademicSession(sourceId text, status text, dateLastModified text, title text, type text, startDate text, endDate text, parentSourcedId text, schoolYear text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Class(sourceId text, status text, dateLastModified text, title text, grade text, courceSourcedId text, classCode text, classType text, location text, schoolSourcedId text, termSourcedIds text, subjects text, subjectCodes text, period text, specialNeeds text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Course(sourceId text, status text, dateLastModified text, schoolYearSourcedId text, title text, courseCode text, grades text, orgSourcedId text, subjects text, subjectCodes text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Demographics(sourceId text, status text, dateLastModified text, barthDate text, sex text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Enrollment(sourceId text, status text, dateLastModified text, classSourcedId text, schoolSroucedId text, userSourcedId text, role text, primary text, beginDate text, endDate text, ShussekiNo text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Orgs(sourceId text, status text, dateLastModified text, name text, type text, identifier text, parentSourcedId text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Roles(sourceId text, status text, dateLastModified text, userSourcedId text, roleType text, beginDate text, endDate text, orgSourcedId text, userProfileSroucedId text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS UserProfile(sourceId text, status text, dateLastModified text, userSourcedId text, profileType text, venderId text, applicationId text, description text, credentialType text, username text, password text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS User(sourceId text, status text, dateLastModified text, enabledUser text, username text, userIds text, givenName text, familyName text, middleName text, identifier text, email text, sms text, phone text, agentSourcedIds text, grades text, password text, userMasterIdentifer text, resourceSourcedIds text, preferredGivenName text, preferredMiddleName text, preferredFamiliName text, primaryOrgSourcedId text, kanaGiveName text, kanaFamilyName text, kanaMiddleName text, homeClass text)")

    connection.commit()
    connection.close()

# データベースが存在しない場合に作成する
if not os.path.exists(DATABASE_FILE):
    create_database()

# SQLiteデータベースに接続するヘルパー関数
def connect_to_database():
    return sqlite3.connect(DATABASE_FILE)

# CSVファイルをデータベースに挿入するヘルパー関数
def insert_csv_data(table_name, csv_data):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.executemany(f"INSERT INTO {table_name} VALUES ({','.join(['?']*len(csv_data[0]))})", csv_data)
    conn.commit()
    conn.close()

@app.post("/upload/{table_name}")
async def upload_csv_file(table_name: str, file: UploadFile = File(...), api_key: APIKey = API_KEY):
    try:
        # 提供されたAPIキーを検証
        if not api_key_query(api_key=api_key):
            raise HTTPException(status_code=403, detail="Invalid API Key")

        # アップロードされたCSVファイルの内容を読み取り、データベースに挿入する
        content = await file.read()
        csv_data = []
        decoded_content = content.decode("utf-8")
        csv_reader = csv.reader(TextIOWrapper(content, newline=""))
        for row in csv_reader:
            csv_data.append(row)

        insert_csv_data(table_name, csv_data)

        return {"message": "CSVファイルのアップロードが成功しました。"}

    except Exception as e:
        return {"message": f"エラーが発生しました: {str(e)}"}

# ユーザー情報を取得するエンドポイント (GetAllUser API)
@app.get("/users", response_model=list[dict])
async def get_all_users(api_key: APIKey = API_KEY):
    # 提供されたAPIキーを検証
    if not api_key_query(api_key=api_key):
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # データベースからユーザー情報を取得
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    users = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    conn.close()

    return users

# 特定のユーザー情報を取得するエンドポイント (GetUser API)
@app.get("/users/{user_id}", response_model=dict)
async def get_user(user_id: str, api_key: APIKey = API_KEY):
    # 提供されたAPIキーを検証
    if not api_key_query(api_key=api_key):
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # データベースから指定されたユーザーの情報を取得
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE sourceId = ?", (user_id,))
    user = dict(zip([column[0] for column in cursor.description], cursor.fetchone()))
    conn.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
