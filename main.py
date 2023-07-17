from flask import Flask,render_template,request
import requests

app=Flask(__name__,template_folder='html')

@app.route('/urls_checker',methods=['post','get'])
def checker():
    if request.method=='POST':
        old_link=request.form['first']
        new_link = request.form['second']
        urls=request.form['urls'].split()
        return urls_checker(old_link,new_link,urls)
    return render_template('index.html')


def urls_checker(old_link,new_link,urls):
    statuse_code=dict()
    for url in urls:
        if old_link in url:
            url=url.replace(old_link,new_link)
            r=requests.get(url)
            f=statuse_code.get(r.status_code,[])
            f.append(url)
            statuse_code[r.status_code]=f
    return statuse_code
app.run(debug=True,port=1337, host='0.0.0.0')