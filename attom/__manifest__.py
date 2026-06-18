{
    "name": "ATTOM",
    "version": "18.0.1.0.0",
    "summary": "Paid attomdata.com API access for US property data",
    "category": "Real Estate",
    "application": True,
    "author": "Odoo Community Association (OCA), MetricWise",
    "license": "AGPL-3",
    "maintainer": "Adam Heinz <adam.heinz@metricwise.com>",
    "website": "https://github.com/OCA/vertical-realestate",
    "depends": [
        "base",
    ],
    "data": [
        "data/attom_data.xml",
        "security/attom_security.xml",
        "security/ir.model.access.csv",
    ],
}
