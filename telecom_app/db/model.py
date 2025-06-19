from telecom_app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DECIMAL, Boolean


class Customer(Base):
    __tablename__ = 'customer'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tenure: Mapped[int] = mapped_column(Integer)
    monthly_charges: Mapped[float] = mapped_column(DECIMAL(5, 2))
    total_charges: Mapped[float] = mapped_column(DECIMAL(5, 2))
    contract: Mapped[str] = mapped_column(String)
    internet_service: Mapped[str] = mapped_column(String)
    online_security: Mapped[str] = mapped_column(String)
    tech_support: Mapped[str] = mapped_column(String)
    churn: Mapped[bool] = mapped_column(Boolean)
