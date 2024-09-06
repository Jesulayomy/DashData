# Blockhouse Web Dev Test
This is a test for web developers applying to Blockhouse. The goal is to create a simple web application that fetches data from a django app and displays it on different graphs.

## Requirements
- Python
- Node
- Server (Apache, Nginx, etc)

### Libraries
#### Backend
- Django
- Django Rest Framework
- Django Cors Headers

#### Frontend
- Next.js
- React
- Recharts
- ApexCharts


## Setup
1. Clone this repository
2. Create Virtual environment and install requirements
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
...
```

6. Run the server
```bash
python manage.py runserver # Will run the server on localhost 3000, OR you can use a proper server
```

6.1 Run the server with Nginx
```bash
nginx.conf
server {
	listen 80;

	server_name blockhouse-api.example.com;

	location / {
		include proxy_params;
		proxy_pass http://unix:/home/jesulayomi/projects/gather_go_backend/gathergo.sock;
	}
}
```

6.2 Create a systemd service
```bash
sudo nano /etc/systemd/system/blockhouse-api.service
```

```bash
blockhouse-api.service
[Unit]
Description=Gunicorn instance to serve GatherGo
After=network.target

[Service]
User=USER
Group=GROUP
WorkingDirectory=/home/WD
Environment="PATH=/home/WD/.venv/bin"
ExecStart=/home/WD/.venv/bin/gunicorn --access-logfile access.log --error-logfile error.log --bind unix:blockhouse.sock -m 007 blockhouse.wsgi

[Install]
WantedBy=multi-user.target
```

7. Install frontend dependencies
```bash
cd ../dash-data
npm install
```

8. Run the frontend
```bash
npm build
npm start
```

9. Expose the frontend port or pass a proxy parameter.

10. Setup domain name if you have one


### Problem Process

- I need a django models, serializers and views to fetch data from the database
- Create those pages, setup CORS and allow other hosts
- Create and endpoint to create some hardcoded sample data
- Create POST request routes for new data (Postman or scripts can be used to addd data)
- Create next app with tailwind and ts enabled
- Create page 
- Created footer and header
- Created main section, added empty blocks of fixed size
- Create Moved each block to it's own Component and created Grid component which is the container for the graphs
- Moved grids to Graphs to simplify content on the home/Dashboard page
- Added Sample data for each components, mimicking API endpoints
- Created each Graph component with Recharts
- Hit block while trying to create CandleStick Graph
- Switched to ApexCharts for CandleStick Graph
- Finished components, checked some responsiveness till satisfied
- Added some more styling to the components
- Added a button to refresh the database using the endpoint created in the backend
- Wrote Django TestCases fro backend
- Wrote this README
- Off to deploying and submitting

