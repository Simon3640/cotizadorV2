from csv import DictReader
from typing import BinaryIO
from codecs import iterdecode

from app.services.product import product_svc
from app.schemas.product import ProductCreate


def register_products_from(file: BinaryIO):
    product_csv = DictReader(iterdecode(file, "utf-8"))
    for rows in product_csv:
        product_svc.create_or_update(
            product=ProductCreate(
                name=rows["name"], reference=rows["reference"], value=int(rows["value"])
            )
        )
