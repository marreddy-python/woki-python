from flask import request, json, Response, Blueprint ,render_template
from ..models.dataModel import Searched_queries,Query_result
from ..shared.YouTubeApi import youtube_search
from ..models.dataModel import Searched_queries,Query_result,db
from flask import jsonify,session


query_api = Blueprint('query', __name__,template_folder='templates',)

@query_api.route('/v1/<name>', methods=['POST', 'GET'])

def create(name):

    if request.method == "POST":
        name = name.lower()
        SearchString = ' '.join(name.split())
       
        fetch = Searched_queries.query.filter_by(query_name= SearchString).first()
        print(fetch)
        # if searched query is not exists then create one 
        if fetch == None:
            options={
                'max_results':50,
                'q':SearchString
            }
            results = youtube_search(options)
            if len(results) == 0: 
                    pass
            else:
                # store the results in database
                searched_names =  Searched_queries(query_name=SearchString)
                db.session.add(searched_names)
                db.session.commit()

                for i in range(len(results)):
                    res = Query_result(owner= searched_names,url = results[i])
                    db.session.add(res)
                    db.session.commit()

            return 'Stored in database succesfully'

        else :
            return 'Already exists in database'
            pass
            

    else:
        # IF REQUEST METHOD IS GET 
        name = name.lower()
        SearchString = ' '.join(name.split())
        fetch = Searched_queries.query.filter_by(query_name= SearchString).first()
        Required_Quiery = SearchString.replace(" ", "+")
        print(fetch)

        if fetch == None:
            Query_name = None
            urls = []
        else :
            Query_name = fetch.query_name
            urls = []

            for i in range(len(fetch.results)):
                urls.append(fetch.results[i].url)

            print(len(fetch.results))

        return  jsonify(Query_name = Query_name,urls = urls)




