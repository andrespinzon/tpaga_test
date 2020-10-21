from typing import Optional, Dict
from datetime import datetime

from django.db.models import AutoField, CharField, DateTimeField, Model, PositiveIntegerField, ForeignKey, PROTECT, \
    JSONField


class Terminal(Model):
    model_name = 'Terminal'

    id: int = AutoField(primary_key=True)
    name: str = CharField('Name', max_length=255, null=False)

    created_at: datetime = DateTimeField('Created At', auto_now_add=True, db_index=True)
    updated_at: datetime = DateTimeField('Updated At', auto_now=True)


class Order(Model):
    model_name = 'Order'

    id: int = AutoField(primary_key=True)
    original_id: str = CharField('Original Id', max_length=255, null=False)
    cost: int = PositiveIntegerField('Cost')
    idempotency_token: str = CharField('Idempotency Token', max_length=255, null=False)
    terminal: Optional[Terminal] = ForeignKey(to=Terminal, on_delete=PROTECT)
    items: Dict = JSONField('Items', default=dict)

    created_at: datetime = DateTimeField('Created At', auto_now_add=True, db_index=True)
    updated_at: datetime = DateTimeField('Updated At', auto_now=True)
