main.py-----------------

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
    
    
    
    
    
    
    
    
    
    
    
    index.html----------------------
    
   <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Weather checkar</title>
  </head>
  <body>
    <div class="container my-5">
        <h1>Yo , wassap</h1>

    </div>
    <div class="container my-8">
        
        <form class="row g-3" action="." method="post">
            <div class="col-auto">
              <label for="staticEmail2" class="visually-hidden">Email</label>
              <input type="text" readonly class="form-control-plaintext" id="staticEmail2" value="Enter city">
            </div>
            <div class="col-auto">
              <label for="city" class="visually-hidden">City</label>
              <input type="text" name="city" class="form-control" id="city" placeholder="City">
            </div>
            <div class="col-auto">
              <button type="submit" class="btn btn-primary mb-3">Search</button>
            </div>
          </form>
    </div>
{% if city|length==0 %}
 <div class="container my-5">
  <div class="accordion accordion-flush" id="accordionFlushExample">
    <div class="accordion-item">
      <h2 class="accordion-header" id="flush-headingOne">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
         No data click to read
        </button>
      </h2>
      <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
        <div class="accordion-body">Enter the city name to get the weather data <code> Eg. Mumbai</code></div>
      </div>
    </div>
  </div>
 </div>
{% else %}
  <div class="container my-5">
<!-- <h1 class="display-6">{{city}}</h1> -->
<h1 class="display-6">the Weather report tells that there is {{weather}} in {{city}}<img src={{icon}} height="64px" width="64px"></img></h1>
<h1 class="display-6">The temprature is {{temp}}° celcius in {{city}}</h1>

    </div>
{% endif %}
    

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
  </body>
</html>











news.html--------------------------

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Cool News</title>
  </head>
  <body>
    <div class="container my-5"><center><h1>News By Aniket</h1></center></div>
    <form class="row g-3" action="." method="post">

    <div class="container">
        <div class="container">
            <label for="basic-url" class="form-label">Enter Some Topics</label>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon3">Eg. Modi Noob</span>
      <input type="text" class="form-control" id="info" name="info" aria-describedby="basic-addon3">
    </div>
        
            <center>
    
                <button type="submit" class="btn btn-outline-dark">Search</button>
            </center>
    
        </div>
    </div>
    </form>

  {% if text|length==0 %}
    <div class="container my-5">
        <center>
         <h1 class="display-4">Uh.. No , No Content to show</h1>
        <br>
        <h4 class="display-4">Try searching some News</h4>   
        </center>
          
    </div>
  {% else %}
  <div class="container my-5">
    <center>
        <img src={{imagenews}} class="img-fluid" alt="...">
        <h1 class="display-4">{{titlenews}}</h1>
        <!-- <p class="lead">
{{newsdesc}}
        </p> -->
        <p class="lead">
            {{content}}
                        </p>
        <div class="d-grid gap-2 col-6 mx-auto">
            
         <a href={{newsurl}}>  <button  class="btn btn-primary" type="button">Read Full Article</button></a> 
          </div>
          </div>
    </center>
</div>
  {% endif %}

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
  </body>
</html>










news.py-------------------------------


import requests,json,math




apikeynews="242cbabc943c4800ab389b2d97db6532"
baseurlnews="https://newsapi.org/v2/everything?q=india&from=2022-07-21&sortBy=publishedAt&apiKey=242cbabc943c4800ab389b2d97db6532"
baseurlfornews="https://newsapi.org/v2/everything?q="
cate=input("enter your cataegory\n")

compnews=baseurlfornews+cate+"&from=2022-07-21&sortBy=publishedAt&apiKey="+apikeynews
responsefornews=requests.get(compnews)
datafornews=responsefornews.json()
print(datafornews['articles'][0]['author'])
print(datafornews['articles'][0]['title'])
print(datafornews['articles'][0]['description'])
print(datafornews['articles'][0]['urlToImage'])
print(datafornews['articles'][1]['title'])
print(datafornews['articles'][3]['title'])


for i in range(10):
    print(datafornews['articles'][i]['title'])



#quotes  https://zenquotes.io/api/random/[key]
# https://winterly-backend.herokuapp.com/quote
# random image https://random.imagecdn.app/500/150 or use unsplash












weather.py-----------------
import requests,json,math

apikey="fa791aa0bc78403e28c531420d5ff78a"
cityname=input("enter the city name to get the weather data\n")
base="https://api.openweathermap.org/data/2.5/weather?q="
final=base+cityname+"&appid="+apikey
fetching=requests.get(final)
data=fetching.json()
if(data['cod']=='404'):
    print(f"the Entered city {cityname} does not exit in our data-base")
else:
    print("the Weather report tells that there is",data['weather'][0]['main']," in ",cityname )
    
    print("The temprature is ",math.ceil((data['main']['temp'])-273.15),"° celcius in ",cityname )
