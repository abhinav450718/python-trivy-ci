class ServiceStatusChecker:

    def __init__(self, services):
        self.services = services

    def failed_services(self):
        return [s["name"] for s in self.services if s["status"] != "running"]

    def system_health(self):
        failed = self.failed_services()

        if not failed:
            return "All services healthy"

        return f"Failed services: {', '.join(failed)}"
