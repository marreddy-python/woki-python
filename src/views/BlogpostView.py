# API END POINTS
# import argparse
from flask import request, json, Response, Blueprint ,render_template
from ..models.dataModel import Searched_queries,Query_result
from ..shared.YouTubeApi import youtube_search
from ..models.dataModel import Searched_queries,Query_result,db
from flask import jsonify,session

user_api = Blueprint('users', __name__,template_folder='templates',)

@user_api.route('/v1/', methods=['POST', 'GET'])

def create():
    
    if request.method == "POST":
        
        SearchStrings = ['epl','fitness inspiration','positive living','mental health','depression healing','career motivation','goal motivation']
        
        for SearchString_index in range(0,len(SearchStrings)):    
            
            options={
                'max_results':50,
                'q':SearchStrings[SearchString_index].replace(" ", "+")
            }
            
            name = SearchStrings[SearchString_index].lower()
            Search_string = ' '.join(name.split())

            exists = bool(Searched_queries.query.filter_by(query_name=Search_string).first())
            print(exists)

            if exists == True:
                pass 
            else:
                # call the api to fetch the video id
                results = youtube_search(options)
                if len(results) == 0: 
                    pass
                else:
                    # store the results in database
                    searched_names =  Searched_queries(query_name=Search_string)
                    db.session.add(searched_names)
                    db.session.commit()

                    for i in range(len(results)):
                        res = Query_result(owner= searched_names,url = results[i])
                        db.session.add(res)
                        db.session.commit()

        return jsonify(a = 'Successfully stored all the results')
    
    else :
        # fetch the results 
        fetch = Searched_queries.query.all()
        print(fetch)
        print(len(fetch))
        Dict = [ ] 

        for i in range(0,len(fetch)):

            print(fetch[i].query_name)
            Query_name = fetch[i].query_name
            a = fetch[i].results
            urls = []
        
            for x in range(0,len(a)):
                urls.append(a[x].url)

            new_dict = {
                'Query_name': Query_name ,
                'urls':urls
            }

            Dict.append(new_dict)

        return jsonify(Dict = Dict)








    
     

    