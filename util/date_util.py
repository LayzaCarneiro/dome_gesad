
def format(date):

    new_date = list()

    if "-" in date:
        new_date = date.split("-")
    elif "/" in date:
        new_date = date.split("/")
    else:
        return date

    if len(new_date[0]) > 2:
        return "'" + new_date[0] + "-" + new_date[1] + "-" + new_date[2] + "'"
    elif len(new_date[2]) > 2:
        return "'" + new_date[2] + "-" + new_date[1] + "-" + new_date[0] + "'"
    else:
        return date