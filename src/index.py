from flask import Flask, json, g, request
from facebook_scraper import get_page_info, get_profile

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return json_response({ 'error': error }, 404)

@app.route("/facebook/organization/<identifier>", methods=['GET'])
def get_facebook_organization(identifier):
  # identifier = request.args.get('identifier')
  if identifier is None:
    abort({ 'error': '%s not found'.format(identifier) })
  else:
    response = get_page_info(identifier, cookies="./tmp/cookies.txt")
    return json_response(response)

@app.route("/facebook/person/<identifier>", methods=['GET'])
def get_facebook_person(identifier):
  if identifier is None:
    abort({ 'error': '%s not found'.format(identifier) })
  else:
    response = get_profile(identifier, cookies="./tmp/cookies.txt")
    return json_response(response)

def json_response(payload, status = 200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})

if __name__ == '__main__':
  # from waitress import serve
  # serve(app, host="0.0.0.0", port=8080)
  app.run(debug = True)