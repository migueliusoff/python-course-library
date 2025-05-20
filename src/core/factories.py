from core.models import Hall, Library, Rack, Shelf


class HallFactory:
    @staticmethod
    def create(library: Library) -> Hall:
        hall = Hall.objects.create(library=library)
        for _ in range(10):
            rack = Rack.objects.create(hall=hall)
            for _ in range(10):
                Shelf.objects.create(rack=rack)

        return hall
