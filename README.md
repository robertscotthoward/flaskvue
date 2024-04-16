# Flask-Vue Starter Template

This site creates a python Flask web site that serves up an API and a Vue web site from the same folder and web server. Although not optimized, it has these advantages:

* Node and npm is not required
* No CORS configuration since both API and web are served from same site
* CDN references for Vue used
* No need to build/compile the site


Requirements:

* Python 3; e.g. 3.11 in this case

# Description

This site

# Usage

How this project was created
```
mkdir
npx create-react-app web
pip install flask flask_cors jinja2 jsonify
```

Test web app:
```
# Assume web folder
npm start
```

You should see the app in browser http://localhost:3000

Build web for Flask:
```
cd web
npm run build
```


