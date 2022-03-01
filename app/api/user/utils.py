from flask_restx import marshal


def load_data(user_db_obj):
    """ Load user's data

    Parameters:
    - User db object
    """
    from app.models.schemas import user_schema
    data = marshal(user_db_obj, user_schema)

    return data
