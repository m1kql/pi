from discord import user
import firebase_admin
from firebase_admin import credentials, firestore

path_to_json = "bot/src/firebase_config.json"
appCredentials = credentials.Certificate(path_to_json)
firebase_admin.initialize_app(appCredentials)

db = firestore.client()

questions_solved = "questions_solved"
questions_attempted = "questions_attempted"
questions_failed = "questions_failed"


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
