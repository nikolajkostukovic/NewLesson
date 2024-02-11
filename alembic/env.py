from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from Models import currency
from alembic import context

target_metadata = currency.metadata

config = context.config
config.set_main_option('sqlalchemy.url', 'postgresql://postgres:postgres@localhost:5432/Python_bot')

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:

    from sqlalchemy import create_engine

    # Используйте объект bind здесь
    engine = create_engine(config.get_main_option('sqlalchemy.url'))
    connection = engine.connect()

    context.configure(
        connection=connection, target_metadata=target_metadata
    )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    from logging.config import fileConfig
    fileConfig(config.config_file_name)
    alembic_cfg = config.get_section(config.config_ini_section)
    alembic_cfg['sqlalchemy.url'] = config.get_main_option('sqlalchemy.url')
    target_metadata.reflect(engine)

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()
