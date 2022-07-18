from dotmap import DotMap

SERVER_CONFIG = DotMap({
    "ip": "192.168.0.18",
    "port": 8000
})

NACOS_CONFIG = DotMap({
    "ip": "192.168.0.14",
    "port": 8848,
    "serviceName": "exApi-service",
})

