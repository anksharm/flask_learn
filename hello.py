import json
from flask import Flask, request, Response


app = Flask(__name__)
#please mention the path to your images.json file
FILE_DB = <PATH TO JSON FILE>
f = open(FILE_DB)
json_ob = json.loads(f.read())

#/json lists all urls
@app.route('/json', methods=['GET'])
def all_urls():
    return '\n'.join(map(str, json_ob['images']))

#/json/n lists a specific image url
@app.route('/json/<int:n>', methods=['GET'])
def nth_url(n):
    try:
        r = json_ob['images'][n]
        if len(r) > 0:
            result = r
    except:
        result = 'Not available'
    return result

#/html shows each/all images in json
@app.route('/html', methods=['GET'])
def html():
    y = []

    def print_pics():
        l = []
        for pics in json_ob['images']:
            y.append(str(pics))
        for items in y:
            img = "<img src='%s' style='margin-left: 15px'\
                  width='300' height='194'></img>" % (items)
            l.append(img)
        return l

    return Response(print_pics())

#/submit to add urls to json
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        for img in request.form.getlist('image'):
            l = json_ob['images']
            l.append(img)
        with open(FILE_DB, 'wb') as outfile:
            wr = json.dumps({'images': l}, outfile, indent=4)
            outfile.write(wr)
            outfile.close()
    else:
        'please try curl'
    return 'successfully added'

if __name__ == '__main__':
    #customize host and port if you dont want the localhost and 5000 default
    app.run(host=<HOST>, port=<PORT>, debug=True)
