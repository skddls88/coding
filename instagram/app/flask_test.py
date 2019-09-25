from flask import Flask, redirect, render_template, request, session, url_for , g ,jsonify , abort , Response
import pymysql
import requests
import json
from bs4 import BeautifulSoup


app = Flask(__name__)
app.secret_key ="orye603@#$asdflkasjowi52o3i5j235j%#$%5j345#$"

@app.route("/insta")
def insta():
    key_word = request.args.get("keyword")
    # key_word = "애견스타그램"
    url = 'https://www.instagram.com/explore/tags/'+key_word+'/?__a=1'
    req = requests.get(url)
    json_data = json.loads(req.text)
    return_list = []
    for item in json_data['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
        return_list.append({"short_code":"https://instagram.com/p/"+item['node']['shortcode'],"thumnail":item['node']['display_url'],
                            "like":item['node']['edge_liked_by']['count'],"owner":item['node']['owner']['id']})
                            # ,
                        #   "description":item['node']['edge_media_to_caption']['edges'][0]['node']['text']
    return render_template("use.html", return_data = return_list)
    # return jsonify(return_list)


if __name__ == "__main__":
    app.run(debug=True)