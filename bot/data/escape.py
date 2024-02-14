async def pg_escape_string(user_request: str):
    """
    Return escaped string
    """ 
    escaped = user_request.translate(str.maketrans({"'": r"\'", '"': r'\"', "\\": r"\\\\",
                                                    "#": r"\#", "&": r"\&", "+": r"\+",
                                                    "-": r"\-", "=": r"\=", ";": r"\;",
                                                    ":": r"\:", "*": r"\*", "<": r"\<",
                                                    ">": r"\>", "/": r"\/",}))
    return escaped