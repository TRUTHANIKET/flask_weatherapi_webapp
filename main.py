import requests,json,math
from flask import Flask,render_template,request
app = Flask(__name__)
apikey="78a4741ec4ee6438b4bd43a1e7cd8ba3"
apikay="796cae83f73746dda3f63937222108"
apikeynews="242cbabc943c4800ab389b2d97db6532"

base="https://api.openweathermap.org/data/2.5/weather?q="
baseurl="http://api.weatherapi.com/v1/current.json?key="
baseurlfornews="https://newsapi.org/v2/everything?q="


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def newsindex():
    return render_template('news.html')

@app.route('/',methods=['POST','GET'])
def news():
    text=request.form['info']
    compnews=baseurlfornews+text+"&from=2022-07-21&sortBy=publishedAt&apiKey="+apikeynews
    responsefornews=requests.get(compnews)
    datafornews=responsefornews.json()
    # print(datafornews['articles'][0]['author'])
    # print(datafornews['articles'][0]['title'])
    # print(datafornews['articles'][0]['description'])
    # print(datafornews['articles'][0]['urlToImage'])
    # print(text)
    titlenews=datafornews['articles'][0]['title']
    imagenews=datafornews['articles'][0]['urlToImage']
    newsdesc=datafornews['articles'][0]['description']
    content=datafornews['articles'][0]['content']
    newsurl=datafornews['articles'][0]['url']

    return render_template('news.html',text=text,imagenews=imagenews,titlenews=titlenews,newsdesc=newsdesc,newsurl=newsurl,content=content)

@app.route('/',methods=['POST','GET'])
def home():

   
    city=request.form['city']
    final=base+city+"&appid="+apikey
    fetching=requests.get(final)
    data=fetching.json()
    finalforicon=baseurl+apikay+"&q="+city+"&aqi=no"
    fetchicon=requests.get(finalforicon)
    dataicon=fetchicon.json()
    weather=data['weather'][0]['main'] 
    
    icon=(dataicon['current']['condition']['icon'])
    temp=math.ceil((data['main']['temp'])-273.15)
    # ,"° celcius in ",city 
   
    
    return render_template('index.html',weather=weather,temp=temp,city=city,icon=icon)


if __name__=="__main__":
    app.run(debug=True)
    