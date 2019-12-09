import random
from flask import jsonify, request
from flask import current_app as app

from app.logger import request_log_wrapper

def _categories():

    # declare pymongo client
    mongo = app.config["MONGODB_CLIENT"]
    metadata = mongo.metadata.metadata

    data = metadata.distinct('categories')
    finallst = []

    for i in data:
        for j in i:
            if j not in finallst:
                finallst.append(j)

    outerlist = []
    for cat in finallst:
        temp = {}
        temp['category'] = cat
        outerlist.append(temp)

    finaldict = {}
    finaldict['categories'] = outerlist

    # for logging received requests
    log_msg = request_log_wrapper(request)
    app.logger.info(log_msg)

    return jsonify(finaldict)
