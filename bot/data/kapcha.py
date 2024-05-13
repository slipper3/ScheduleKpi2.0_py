template = {
    "groupName": "--"
}



async def kapcha(user_request, type: str):
    """
    Checks if the string contains at least one character that is not in the allowed character list.\n
    `input_string` - String need to be checked.\n
    `type` - what kinde of data need to check.\n
    Existig data:\n
        - groupName\n
        `return` True, if request dosnt contain "--", else False.\n
    """ 
    if type == "chatID":
        allowed_chars = template[type]
        return all(char in allowed_chars for char in str(user_request))
    elif type == "groupName":
        banned = template[type]
        return banned not in user_request