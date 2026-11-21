def migrate(cr, version):
    cr.execute(
        "INSERT INTO ir_config_parameter (key, value, create_uid, write_uid, create_date, write_date) "
        "VALUES ('pipeline.case06', %s, 1, 1, now(), now()) "
        "ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value", [version or 'none'])
