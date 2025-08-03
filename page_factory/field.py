from page_factory.component import Component


class Field(Component):
    @property
    def type_of(self) -> str:
        return "field"
