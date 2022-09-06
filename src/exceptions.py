class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class ResponseIsNoneException(Exception):
    """Вызвается, когда response - None"""
    pass
