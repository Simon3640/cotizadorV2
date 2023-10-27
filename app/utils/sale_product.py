from functools import reduce

from app.schemas.sale_product import SaleProductResponse


def total_from(sale_product: list[SaleProductResponse]) -> float:
    return reduce(
        lambda x, y: x + y,
        map(lambda x: x.product.value * (1 + x.tax / 100), sale_product),
        0,
    )


def total_tax_from(sale_product: list[SaleProductResponse]) -> float:
    return reduce(
        lambda x, y: x + y,
        map(lambda x: x.product.value * (x.tax / 100), sale_product),
        0,
    )
