from app.service_status import ServiceStatusChecker


def test_all_services_running():

    services = [
        {"name": "auth", "status": "running"},
        {"name": "payment", "status": "running"}
    ]

    checker = ServiceStatusChecker(services)

    assert checker.system_health() == "All services healthy"


def test_service_failure():

    services = [
        {"name": "auth", "status": "running"},
        {"name": "payment", "status": "stopped"}
    ]

    checker = ServiceStatusChecker(services)

    assert "payment" in checker.system_health()
