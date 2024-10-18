from sqlalchemy.orm import Session

from schema.product import ProductBase
from models.product import Product


# 상품 등록 처리
def register(db: Session, product: ProductBase):
    product = Product(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    print(product)

    return product

# 상품 목록 조회
def productlist(db: Session):
    return db.query(Product.name, Product.price, Product.regdate, Product.pno)\
        .order_by(Product.pno.desc()).all()

# 상품 상세 조회
def productone(db: Session, pno: int):
    return db.query(Product).filter(Product.pno == pno).first()


def productdelete(db: Session, pno: int):
    # 삭제할 상품 조회
    product = db.query(Product).filter(Product.pno == pno).first()

    if product: # 삭제 할 상품이 존재한다면
        db.delete(product)
        db.commit()
    else:
        return None

        # 삭제한 상품수를 직접 return 함
        # 만일, 프로그래밍으로 삭제한 상품수를 return하려면
        # core orm을 이용할 것! (db.execute(delete)
    return 1
