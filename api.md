# Carbonaware

Types:

```python
from carbonaware.types import RetrieveResponse
```

Methods:

- <code title="get /">client.<a href="./src/carbonaware/_client.py">retrieve</a>() -> <a href="./src/carbonaware/types/retrieve_response.py">RetrieveResponse</a></code>

# Schedule

Types:

```python
from carbonaware.types import CloudZone, ScheduleOption, ScheduleCreateResponse
```

Methods:

- <code title="post /v0/schedule/">client.schedule.<a href="./src/carbonaware/resources/schedule.py">create</a>(\*\*<a href="src/carbonaware/types/schedule_create_params.py">params</a>) -> <a href="./src/carbonaware/types/schedule_create_response.py">ScheduleCreateResponse</a></code>

# Regions

Types:

```python
from carbonaware.types import RegionListResponse
```

Methods:

- <code title="get /v0/regions/">client.regions.<a href="./src/carbonaware/resources/regions.py">list</a>() -> <a href="./src/carbonaware/types/region_list_response.py">RegionListResponse</a></code>

# Health

Types:

```python
from carbonaware.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/carbonaware/resources/health.py">check</a>() -> <a href="./src/carbonaware/types/health_check_response.py">HealthCheckResponse</a></code>
