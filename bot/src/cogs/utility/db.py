import firebase_admin
from firebase_admin import credentials, firestore

from dotenv import load_dotenv
import os

load_dotenv()

firebase_type = os.getenv("firebase_type")
firebase_project_id = os.getenv("firebase_project_id")
firebase_private_key_id = os.getenv("firebase_private_key_id")
firebase_private_key = os.getenv("firebase_private_key")
firebase_client_email = os.getenv("firebase_client_email")
firebase_client_id = os.getenv("firebase_client_id")
firebase_auth_uri = os.getenv("firebase_auth_uri")
firebase_token_uri = os.getenv("firebase_token_uri")
firebase_auth_provider_x509_cert_url = os.getenv("firebase_auth_provider_x509_cert_url")
firebase_client_x509_cert_url = os.getenv("firebase_client_x509_cert_url")


def buildJSON():
    JSONstring = (
        "{"
        + "\n"
        + '"type"'
        + ":"
        + f'"{firebase_type}"'
        + ","
        + '"project_id"'
        + ":"
        + f'"{firebase_project_id}"'
        + ","
        + '"private_key_id"'
        + ":"
        + f'"{firebase_private_key_id}"'
        + ","
        + '"private_key"'
        + ":"
        + f'"{firebase_private_key}"'
        + ","
        + '"client_email"'
        + ":"
        + f'"{firebase_client_email}"'
        + ","
        + '"client_id"'
        + ":"
        + f'"{firebase_client_id}"'
        + ","
        + '"auth_uri"'
        + ":"
        + f'"{firebase_auth_uri}"'
        + ","
        + '"token_uri"'
        + ":"
        + f'"{firebase_token_uri}"'
        + ","
        + '"auth_provider_x509_cert_url"'
        + ":"
        + f'"{firebase_auth_provider_x509_cert_url}"'
        + ","
        + '"client_x509_cert_url"'
        + ":"
        + f'"{firebase_client_x509_cert_url}"'
        + "\n"
        + "}"
    )
    f = open("firebase_config.json", "w")
    f.write(JSONstring)
    f.close()
    return "firebase_config.json"


appCredentials = credentials.Certificate(buildJSON())
firebase_admin.initialize_app(appCredentials)

db = firestore.client()

questions_solved = "questions_solved"
questions_attempted = "questions_fetched"
questions_failed = "questions_failed"
amc10_attempted = "amc10_fetched"
amc10_failed = "amc10_failed"
amc10_solved = "amc10_solved"
amc12_attempted = "amc12_fetched"
amc12_failed = "amc12_failed"
amc12_solved = "amc12_solved"
aime_attempted = "aime_fetched"
usamo_attempted = "usamo_fetched"
usajmo_attempted = "usajmo_fetched"
amc10_points = "amc10_points"
amc12_points = "amc12_points"


async def open_user_db(guild_id, user_id):
    collection_ref = db.collection(str(guild_id)).document(str(user_id))
    fetch_user_data = collection_ref.get()
    if fetch_user_data.exists:
        pass
    else:
        data = {
            questions_solved: 0,
            questions_attempted: 0,
            questions_failed: 0,
            amc10_attempted: 0,
            amc10_failed: 0,
            amc10_solved: 0,
            amc12_attempted: 0,
            amc12_failed: 0,
            amc12_solved: 0,
            aime_attempted: 0,
            usamo_attempted: 0,
            usajmo_attempted: 0,
            amc10_points: 0,
            amc12_points: 0,
        }
        db.collection(str(guild_id)).document(str(user_id)).set(data)


async def get_user_db(guild_id, user_id):
    collection_ref = db.collection(str(guild_id)).document(str(user_id))
    fetch_user_data = collection_ref.get()
    user_db_dict = {}
    if fetch_user_data.exists:
        user_db_dict = fetch_user_data.to_dict()
        return user_db_dict
    else:
        await open_user_db(guild_id, user_id)
        new_user_db_dict = {}
        new_user_db_dict = (
            (db.collection(str(guild_id)).document(str(user_id))).get()
        ).to_dict()
        return new_user_db_dict
