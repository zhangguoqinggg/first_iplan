# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, Table, Unicode
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



t_m_code = db.Table(
    'm_code',
    db.Column('code', db.Unicode(20)),
    db.Column('name', db.Unicode(50)),
    db.Column('type', db.Integer, nullable=False),
    db.Column('create_time', db.DateTime, nullable=False)
)



t_m_company = db.Table(
    'm_company',
    db.Column('id', db.Integer, nullable=False),
    db.Column('company_code', db.Unicode(20)),
    db.Column('company_name', db.Unicode(20)),
    db.Column('create_time', db.DateTime),
    db.Column('company_name_english', db.Unicode(50))
)



t_m_currency = db.Table(
    'm_currency',
    db.Column('id', db.Integer, nullable=False),
    db.Column('org_currency', db.Unicode(10)),
    db.Column('target_currency', db.Unicode(10)),
    db.Column('exchangerate', db.Numeric(18, 6), nullable=False),
    db.Column('create_time', db.DateTime, nullable=False)
)



t_m_current_status = db.Table(
    'm_current_status',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cs_code', db.Unicode(10)),
    db.Column('current_status_name', db.Unicode(10)),
    db.Column('quote_precontract_flag', db.Integer),
    db.Column('create_time', db.DateTime)
)



t_m_customer = db.Table(
    'm_customer',
    db.Column('customer_id', db.Unicode(32), nullable=False),
    db.Column('customer_code', db.Unicode(32), nullable=False),
    db.Column('customer_name', db.Unicode(100)),
    db.Column('customer_short_name', db.Unicode(100)),
    db.Column('industry_type_id', db.Integer),
    db.Column('create_time', db.DateTime)
)



t_m_dept = db.Table(
    'm_dept',
    db.Column('id', db.Integer, nullable=False),
    db.Column('dep_code', db.Unicode(20)),
    db.Column('dep_name', db.Unicode(50)),
    db.Column('dep_parent_id', db.Integer),
    db.Column('create_time', db.DateTime, nullable=False)
)



t_m_employe = db.Table(
    'm_employe',
    db.Column('employe_id', db.Integer, nullable=False),
    db.Column('employe_name', db.Unicode(50)),
    db.Column('employe_code', db.Unicode(10), nullable=False),
    db.Column('phone_number', db.Unicode(20)),
    db.Column('email', db.Unicode(50)),
    db.Column('dep_id', db.Integer),
    db.Column('create_time', db.DateTime),
    db.Column('base_on', db.Unicode(20))
)



t_m_employe_level_post = db.Table(
    'm_employe_level_post',
    db.Column('employe_code', db.Unicode(20)),
    db.Column('employe_level', db.Unicode(20)),
    db.Column('employe_postl', db.Unicode(20)),
    db.Column('create_time', db.DateTime)
)



t_m_gm_order_type = db.Table(
    'm_gm_order_type',
    db.Column('id', db.Integer, nullable=False),
    db.Column('gm_code', db.Unicode(10)),
    db.Column('order_type_id', db.Integer),
    db.Column('create_time', db.DateTime),
    db.Column('approval_min_price', db.Numeric(18, 6))
)



t_m_industry_type = db.Table(
    'm_industry_type',
    db.Column('id', db.Integer, nullable=False),
    db.Column('industry_code', db.Unicode(20)),
    db.Column('industry_type_name', db.Unicode(20)),
    db.Column('flag', db.Integer),
    db.Column('create_time', db.DateTime)
)



t_m_interface_resources = db.Table(
    'm_interface_resources',
    db.Column('id', db.Integer, nullable=False),
    db.Column('interface_code', db.Unicode(20)),
    db.Column('interface_name', db.Unicode(50)),
    db.Column('create_time', db.DateTime)
)



t_m_level = db.Table(
    'm_level',
    db.Column('id', db.Integer, nullable=False),
    db.Column('level_code', db.Unicode(10), nullable=False),
    db.Column('level_name', db.Unicode(20), nullable=False),
    db.Column('man_day_cost', db.Numeric(18, 6), nullable=False),
    db.Column('standard_man_day_cost', db.Numeric(18, 6), nullable=False),
    db.Column('create_time', db.DateTime, nullable=False)
)



t_m_order_type = db.Table(
    'm_order_type',
    db.Column('id', db.Integer, nullable=False),
    db.Column('order_type_code', db.Unicode(10)),
    db.Column('order_type_name', db.Unicode(10)),
    db.Column('order_type_type', db.Integer),
    db.Column('create_time', db.DateTime),
    db.Column('subtype_color', db.Unicode(10))
)



t_m_parent_order_type = db.Table(
    'm_parent_order_type',
    db.Column('id', db.Integer, nullable=False),
    db.Column('parent_order_type_name', db.Unicode(10)),
    db.Column('create_time', db.DateTime),
    db.Column('type_color', db.Unicode(10)),
    db.Column('sort_id', db.Integer)
)



t_m_prc_current_status = db.Table(
    'm_prc_current_status',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cs_code', db.Unicode(10)),
    db.Column('current_status_name', db.Unicode(10)),
    db.Column('create_time', db.DateTime)
)



t_m_product = db.Table(
    'm_product',
    db.Column('id', db.Unicode(32)),
    db.Column('product_id', db.Unicode(32)),
    db.Column('product_name', db.Unicode(100)),
    db.Column('Create_data', db.DateTime, nullable=False)
)



t_m_quote_precontract_post = db.Table(
    'm_quote_precontract_post',
    db.Column('id', db.Integer, nullable=False),
    db.Column('post_code', db.Unicode(10), nullable=False),
    db.Column('post_name', db.Unicode(50)),
    db.Column('create_time', db.DateTime, nullable=False)
)



t_m_sub_product = db.Table(
    'm_sub_product',
    db.Column('id', db.Unicode(32)),
    db.Column('sub_product_id', db.Unicode(32)),
    db.Column('sub_product_name', db.Unicode(100)),
    db.Column('product_id', db.Unicode(32)),
    db.Column('product_price', db.Numeric(18, 4), nullable=False),
    db.Column('create_time', db.DateTime, nullable=False)
)



t_m_user = db.Table(
    'm_user',
    db.Column('employe_id', db.Integer),
    db.Column('employe_name', db.Unicode(20)),
    db.Column('employe_code', db.Unicode(10)),
    db.Column('employe_type', db.Unicode(10)),
    db.Column('employe_type_id', db.Integer),
    db.Column('phone_number', db.Unicode(20)),
    db.Column('email', db.Unicode(50)),
    db.Column('dep_id', db.Integer),
    db.Column('create_time', db.DateTime)
)



t_m_user_gm_pe = db.Table(
    'm_user_gm_pe',
    db.Column('employe_id', db.Integer),
    db.Column('employe_name', db.Unicode(20)),
    db.Column('employe_code', db.Unicode(10)),
    db.Column('employe_type', db.Unicode(10)),
    db.Column('employe_type_id', db.Integer),
    db.Column('phone_number', db.Unicode(20)),
    db.Column('email', db.Unicode(50)),
    db.Column('dep_id', db.Integer),
    db.Column('create_time', db.DateTime)
)



t_m_user_position = db.Table(
    'm_user_position',
    db.Column('position_id', db.Integer),
    db.Column('position_code', db.Unicode(10)),
    db.Column('position_name', db.Unicode(10)),
    db.Column('create_time', db.DateTime)
)



t_m_user_privilege_interface = db.Table(
    'm_user_privilege_interface',
    db.Column('id', db.Integer, nullable=False),
    db.Column('user_position_id', db.Integer),
    db.Column('interface_resources_id', db.Integer),
    db.Column('create_time', db.DateTime)
)
