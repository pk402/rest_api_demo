# rest_api_demo



Django DRF POC.

# Set GEOLOCATION_KEY 

Set inside the enviroment 
```bash
export GEOLOCATION_KEY=your-secret-geolocation-key

```
Or Put [here](https://github.com/pk402/rest_api_demo/blob/dev/web/config/common.py#L202)
```bash
    GEOLOCATION_KEY = os.environ.get('GEOLOCATION_KEY') or 'this-is-not-a-valid-key'
    

```

# Initial Migrations
```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb


python manage.py makemigrations api
python manage.py migrate


```

# Active API EndPoint

```bash
{
    "users": "http://127.0.0.1:8000/api/v1/users/",
    "user/new": "http://127.0.0.1:8000/api/v1/user/new/",
    "locations": "http://127.0.0.1:8000/api/v1/locations/",
    "location/new": "http://127.0.0.1:8000/api/v1/location/new/"
}
```
