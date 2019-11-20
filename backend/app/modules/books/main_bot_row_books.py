import random
from flask import jsonify
from flask import current_app as app
from sqlalchemy import func
import numpy as np

from .models import sqlalchem, amazonreviews


def _main_bot_row_books(start, seed):
    start = int(start)
    random.seed(int(seed))
    count = int(metadata.count())
    total_lst = random.sample(range(count), count)
    end = start+18
    lst = total_lst[start:end]
    lst = list(np.array(lst,dtype=str))

    # declare pymysql client
    db = app.config["PYMYSQL_CONNECTION"]

    # declare pymysql client
    mongo = app.config["MONGODB_CLIENT"]
    metadata = mongo.db.metadata

    finaldict = {}
    outerlist = []

    met_data = metadata.find( { 'index': { '$in' : lst } }, { '_id':0,'title':1,'asin':1,'imUrl':1,'categories':1,'related':1 } )

    for j in met_data:
        temp = {}

        if 'title' in j:
            temp['title'] = j['title']

        temp['asin'] = j['asin']

        averageRating = db.session.query(func.avg(amazonreviews.overall)).group_by(amazonreviews.asin).filter_by(asin=j['asin']).scalar()
        
        """
        temp['averageRating'] = averageRating

        if 'imUrl' in j:
            temp['imUrl'] = j['imUrl']
        else:
            temp['imUrl'] = None

        temp['categories'] = j['categories']

        final_related_list = []
        if 'related' in j:
            related = j['related']
            related_list = []

            for a in related:
                for b in related[a]:
                        related_list.append(b)

            related_results = metadata.find( { 'asin': { '$in': related_list } }, { 'asin':1, 'imUrl':1} )

            for k in related_results:
                temp = {}
                temp['asin'] = k['asin']
                temp['imUrl'] = k['imUrl']
                final_related_list.append(temp)
            temp['related'] = final_related_list

        else:
            temp['related'] = None

        outerlist.append(temp)

    finaldict['books'] = outerlist

    # print(lst)
    # print(finaldict)
    # print()
    # print(len(finaldict['books']))
    return(jsonify(finaldict))"""
    return(jsonify({"samplekey": "sampleValue"}))

