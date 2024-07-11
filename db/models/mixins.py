from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime

@declarative_mixin
class Timestamp:
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
